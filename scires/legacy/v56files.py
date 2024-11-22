import os
import struct
import sys
from os.path import realpath

import PIL
from PIL import ImageOps

from scires.legacy.scicell import ViewCellHeader, Cell

sys.path.append('../')

from scires.legacy.palette import Palette
from scires.legacy.sciloop import Loop, LOOPHEADER

V56PATCH = 0x008080
V56PATCH84 = 0x008480


class V56HEAD:
    def __init__(self, binary_data=None, offset=0):
        self.loop_table_offset = None  # unsigned short
        self.loop_count = None  # unsigned char
        self.unknown_byte = None  # char
        self.compressed = None  # bool
        self.view_size = None  # char
        self.num_cells = None  # unsigned short
        self.palette_offset = None  # unsigned long
        self.loop_rec_size = None  # unsigned char
        self.cell_rec_size = None  # unsigned char
        self.x_res = None  # unsigned short
        self.y_res = None  # unsigned short

        self.format = 'HBb?BHIBBHH'
        if binary_data:
            self.unpack(binary_data, offset)

    def size(self):
        return struct.calcsize(self.format)

    def unpack(self, binary_data, offset=0):
        start = offset
        end = start + self.size()
        binary_slice = binary_data[start:end]
        args = struct.unpack(self.format, binary_slice)
        self.loop_table_offset = args[0]
        self.loop_count = args[1]
        self.unknown_byte = args[2]
        self.compressed = args[3]
        self.view_size = args[4]
        self.num_cells = args[5]
        self.palette_offset = args[6]
        self.loop_rec_size = args[7]
        self.cell_rec_size = args[8]
        self.x_res = args[9]
        self.y_res = args[10]


class V56file:
    def __init__(self, file_name: str):
        self.id = os.path.splitext(os.path.split(file_name)[-1])[0]
        self.header: V56HEAD
        self.loops = []  # list of the loops
        self._selectedLoop = None  # unsigned char
        self._palSCI = Palette()  # Palette *
        self._hasLinks = None  # bool

        self.LoadFile(file_name)

    @property
    def num_loops(self):
        return self.header.loop_count
    @property
    def compressed(self):
        return self.header.compressed
    @property
    def cell_rec_size(self):
        return self.header.cell_rec_size
    @property
    def loop_rec_size(self):
        return self.header.loop_rec_size
    @property
    def x_res(self):
        return self.header.x_res
    @property
    def y_res(self):
        return self.header.y_res
    @property
    def view_size(self):
        return self.header.view_size
    @property
    def num_cells(self):
        return self.header.num_cells
    @property
    def unknown_byte(self):
        return self.header.unknown_byte

    @property
    def has_links(self):
        if self.header.cell_rec_size == 0x34:
            return True
        return None

    def AddLoop(self, loop):
        self.loops.append(loop)

    def LoadFile(self, file_name: str):
        with open(file_name, 'rb') as v56_file:
            binary_data = v56_file.read()
        patchID = struct.unpack('i', binary_data[:3] + b"\x00")[0]
        if patchID == V56PATCH84 or patchID == V56PATCH:
            offset = struct.unpack('B', binary_data[4:5])[0]
            offset += 26
        elif patchID & 0xFFF == 16 or patchID & 0xFFFF == 18:
            offset = 0
        else:
            raise (Exception("WRONG_HEADER"))

        self.header = V56HEAD(binary_data, offset)
        if self.header.loop_rec_size != 0x10:
            raise (Exception("WRONG_LOOPRECSIZE"))

        if self.header.cell_rec_size not in [0x24, 0x34]:
            raise (Exception('WRONG_CELLRECSIZE'))

        self.loops = []
        if self.header.palette_offset != 0:
            pallete_offset = offset + self.header.palette_offset - 6
            t_tag = struct.unpack('h', binary_data[pallete_offset:pallete_offset + struct.calcsize('h')])[0]
            if t_tag != 0x0300:
                raise (Exception('ID_WRONGPALLETELOC'))

            pal_size_offset = pallete_offset + struct.calcsize('h')
            t_pal_size = struct.unpack('i', binary_data[pal_size_offset: pal_size_offset + struct.calcsize('i')])[0]
            self._palSCI.loadPalette(binary_data, t_pal_size, pal_size_offset + 4)
        else:
            self._palSCI = Palette()
            self._palSCI.noPalette()
        loop_header_list = []
        loop_offset = offset + self.header.loop_table_offset + 2
        for i in range(self.header.loop_count):
            loop_header = LOOPHEADER(binary_data, loop_offset)
            loop_offset += loop_header.size()
            loop_header_list.append(loop_header)
            loop = Loop()
            loop.LoadLoop(loop_header)
            loop_cells_offset = offset + loop_header.cells_offset
            v_cell_headers = []
            for j in range(loop_header.num_cells):
                v_cell_header = ViewCellHeader()
                v_cell_header.unpack(binary_data, loop_cells_offset)
                v_cell_headers.append(v_cell_header)
                loop_cells_offset += self.cell_rec_size
                if v_cell_header.compression == 0:
                    t_im_size = v_cell_header.width * v_cell_header.height
                else:
                    t_im_size = v_cell_header.image_size

                im_offset = offset + v_cell_header.image_offset
                im = struct.unpack(t_im_size * 'B', binary_data[im_offset:im_offset + struct.calcsize(t_im_size * 'B')])
                pk = 0
                ln = 0
                if v_cell_header.compression != 0:
                    pk_offset = offset + v_cell_header.pack_data_offset
                    pk_size = v_cell_header.image_and_pack_size - v_cell_header.image_size
                    pk = struct.unpack_from(pk_size * 'B', binary_data[pk_offset:])
                    if v_cell_header.lines_offset != 0:
                        ln_offset = offset + v_cell_header.lines_offset
                        ln_size = v_cell_header.height * 4 * 2
                        ln = struct.unpack_from(ln_size * 'B', binary_data[ln_offset:])
                links = []
                if v_cell_header.link_number not in [None, 0]:
                    link_table_offset = offset + v_cell_header.link_table_offset
                    link_point_fmt = "2h2b"
                    fmt_size = struct.calcsize(link_point_fmt)
                    for table_offset in range(link_table_offset, link_table_offset + fmt_size*v_cell_header.link_number, fmt_size):
                        link = struct.unpack(link_point_fmt, binary_data[table_offset:table_offset+fmt_size])
                        _link= {'link_x': link[0], 'link_y': link[1], 'position_type': link[2], 'priority': link[3]}
                        links.append(_link)
                temp_cell = Cell()
                temp_cell.setPalette(self._palSCI)
                temp_cell.setLinks(links)
                temp_cell.LoadCell(v_cell_header, im, pk, ln, True)
                loop.cells[j] = temp_cell
            self.loops.append(loop)
            # The following wont work atm, but it's more or less what Enrico's code does. Why? Ignoring for now.
            # self._cellRecSize = ViewCellHeader.size()


    def displayPalette(self, draw=True):
        flat_rgb_list = [[x.red, x.green, x.blue] for x in self._palSCI.pal_data]
        rgba_im = []
        for x in flat_rgb_list:
            rgba_im.extend(x)
        pil_im = PIL.Image.frombuffer('RGB', (16, 16), bytes(rgba_im), 'raw', 'RGB', 0, 1)
        if draw:
            import matplotlib.pyplot as plt
            plt.imshow(pil_im, interpolation='none')
            plt.show()
        else:
            return pil_im


def serializerToJson(view : V56file):
    global loop, x, loops
    info = {}
    combined_height = 0
    combined_width = 0
    all_loops = []
    info['loops'] = {}
    valid_loops = []
    for loop_idx, loop in enumerate(view.loops):
        all_cells = []
        loop_cells = loop.cells
        loop_info = {"cells": {}}
        if loop.mirror:
            loop_cells = view.loops[loop.based_on_loop].cells
            loop_info['mirror'] = True
            loop_info['basedOn'] = loop.based_on_loop
        if len(loop_cells) == 0:
            continue
        for cell_idx, cell in enumerate(loop_cells):
            if loop.mirror:
                all_cells.append(ImageOps.mirror(cell.get_pil_image(draw=False)))
            else:
                all_cells.append(cell.get_pil_image(draw=False))
            loop_info['cells'][cell_idx] = cell.serialize()
        combined_height += max([x.height for x in all_cells])
        combined_width = max(combined_width, sum([x.width for x in all_cells]))
        all_loops.append(all_cells)
        info['loops'][loop_idx] = loop_info
        valid_loops.append(loop_idx)
    img = PIL.Image.new("RGB", (combined_width, combined_height))
    cur_width = 0
    cur_height = 0
    for loop_num, loops in zip(valid_loops, all_loops):
        max_height = 0
        for cnum, cell in enumerate(loops):
            cell_info = info['loops'][loop_num]['cells'][cnum]
            cell_info['spriteX'] = cur_width
            cell_info['spriteY'] = cur_height
            img.paste(cell, (cur_width, cur_height))
            cur_width += cell.width
            max_height = max(max_height, cell.height)
        cur_height += max_height
        cur_width = 0
        max_height = 0
    view_name = file_name[file_name.rfind('/'):file_name.lower().rfind('.v56')]
    img.save(f"{out_dir}/{view_name}.png")
    view.displayPalette(False).save(f"{out_dir}/{view_name}_pal.png")
    with open(f"{out_dir}/{view_name}.json_output", "w") as json_out:
        json.dump(info, json_out, indent=2)
    # TODO: handle _basedOnLoop and _mirror
    # sci_loop = v._loops[loop]  # sci_cell = sci_loop._cells[cell]
    # im = sci_cell.get_pil_image(draw=False)


if __name__ == '__main__':
    import json

    in_dir = '../../Resources/56_Files'
    out_dir = '../../Resources/json_output/views'
    try:
        os.mkdir(realpath(out_dir))
    except FileExistsError:
        pass

    # v56Files = [os.path.join(in_dir, x) for x in os.listdir(in_dir) if x.lower().endswith('.v56')]
    v56Files = [os.path.join(in_dir, x) for x in os.listdir(in_dir) if x.lower() == '8264.v56']
    for count, file_name in enumerate(v56Files):
        v : V56file = V56file(file_name)
        v.loops[0].cells[0].get_pil_image(draw=True)
        serializerToJson(v)
