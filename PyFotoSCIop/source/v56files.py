import os
import struct
import sys
from os.path import realpath

import PIL
from PIL import ImageOps

sys.path.append('../../')

from PyFotoSCIop.source.palette import Palette
from PyFotoSCIop.source.scicell import ViewCellHeader, Cell
from PyFotoSCIop.source.sciloop import Loop, LOOPHEADER

V56PATCH = 0x008080
V56PATCH84 = 0x008480


class V56HEAD:
    def __init__(self, binary_data=None, offset=0):
        self.LoopTblOff = None  # unsigned short
        self.LoopCount = None  # unsigned char
        self.Unk1 = None  # char
        self.Compressed = None  # bool
        self.ViewSize = None  # char
        self.CellsCount = None  # unsigned short
        self.PalOffset = None  # unsigned long
        self.LoopRecSize = None  # unsigned char
        self.CellRecSize = None  # unsigned char
        self.ResolutionX = None  # unsigned short
        self.ResolutionY = None  # unsigned short

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
        self.LoopTblOff = args[0]
        self.LoopCount = args[1]
        self.Unk1 = args[2]
        self.Compressed = args[3]
        self.ViewSize = args[4]
        self.CellsCount = args[5]
        self.PalOffset = args[6]
        self.LoopRecSize = args[7]
        self.CellRecSize = args[8]
        self.ResolutionX = args[9]
        self.ResolutionY = args[10]


class V56file:
    def __init__(self, file_name: str):
        self.id = os.path.splitext(os.path.split(file_name)[-1])[0]
        self._loops = []  # list of the loops
        self._loopsCount = None  # unsigned char
        self._selectedLoop = None  # unsigned char
        self._unk1 = None  # char
        self._isCompressed = None  # bool
        self._viewSize = None  # char
        self._cellsCount = None  # unsigned short
        self._palSCI = Palette()  # Palette *
        self._cellRecSize = None  # unsigned char
        self._loopRecSize = None  # unsigned char
        self._maxWidth = None  # unsigned short
        self._maxHeight = None  # unsigned short
        self._hasLinks = None  # bool

        self.LoadFile(file_name)

    def AddLoop(self, loop):
        self._loops.append(loop)

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

        looprecsize = struct.unpack_from('B', binary_data, offset + 12)[0]
        if looprecsize != 0x10:
            raise (Exception("WRONG_LOOPRECSIZE"))

        cellrecsize = struct.unpack_from('B', binary_data, offset + 13)[0]
        if cellrecsize == 0x24:
            pass
        elif cellrecsize == 0x34:
            self._hasLinks = True
        else:
            raise (Exception('WRONG_CELLRECSIZE'))

        v_header = V56HEAD(binary_data, offset)
        self._loopsCount = v_header.LoopCount
        self._loops = []
        self._isCompressed = v_header.Compressed
        self._cellRecSize = v_header.CellRecSize
        self._loopRecSize = v_header.LoopRecSize
        self._maxWidth = v_header.ResolutionX
        self._maxHeight = v_header.ResolutionY
        self._viewSize = v_header.ViewSize
        self._cellsCount = v_header.CellsCount
        self._unk1 = v_header.Unk1

        if v_header.PalOffset != 0:
            pallete_offset = offset - 6 + v_header.PalOffset
            t_tag = struct.unpack('h', binary_data[pallete_offset:pallete_offset + struct.calcsize('h')])[0]
            if t_tag != 0x0300:
                raise (Exception('ID_WRONGPALLETELOC'))

            pal_size_offset = pallete_offset + struct.calcsize('h')
            t_pal_size = struct.unpack('i', binary_data[pal_size_offset: pal_size_offset + struct.calcsize('i')])[0]
            new_offset = self._palSCI.loadPalette(binary_data, t_pal_size, pal_size_offset + 4)
        else:
            self._palSCI = Palette()
            self._palSCI.noPalette()
        loop_header_list = []
        loop_offset = offset + v_header.LoopTblOff + 2
        for i in range(v_header.LoopCount):
            loop_header = LOOPHEADER(binary_data, loop_offset)
            loop_offset += loop_header.size()
            loop_header_list.append(loop_header)
            loop = Loop()
            loop.LoadLoop(loop_header)
            loop_cells_offset = offset + loop_header.CellsOffs
            v_cell_headers = []
            for j in range(loop_header.NumberOfCells):
                v_cell_header = ViewCellHeader()
                v_cell_header.unpack(binary_data, loop_cells_offset)
                v_cell_headers.append(v_cell_header)
                loop_cells_offset += self._cellRecSize
                if v_cell_header.compression == 0:
                    t_im_size = v_cell_header.width * v_cell_header.height
                else:
                    t_im_size = v_cell_header.imageSize

                im_offset = offset + v_cell_header.imageOffs
                im = struct.unpack(t_im_size * 'B', binary_data[im_offset:im_offset + struct.calcsize(t_im_size * 'B')])
                pk = 0
                ln = 0
                if v_cell_header.compression != 0:
                    pk_offset = offset + v_cell_header.packDataOffs
                    pk_size = v_cell_header.imageandPackSize - v_cell_header.imageSize
                    pk = struct.unpack_from(pk_size * 'B', binary_data[pk_offset:])
                    if v_cell_header.linesOffs != 0:
                        ln_offset = offset + v_cell_header.linesOffs
                        ln_size = v_cell_header.height * 4 * 2
                        ln = struct.unpack_from(ln_size * 'B', binary_data[ln_offset:])
                links = []
                if v_cell_header.linkNumber not in [None, 0]:
                    link_table_offset = offset + v_cell_header.linkTableOffset
                    link_point_fmt = "2h2b"
                    fmt_size = struct.calcsize(link_point_fmt)
                    for table_offset in range(link_table_offset, link_table_offset + fmt_size*v_cell_header.linkNumber, fmt_size):
                        link = struct.unpack(link_point_fmt, binary_data[table_offset:table_offset+fmt_size])
                        _link= {'link_x': link[0], 'link_y': link[1], 'position_type': link[2], 'priority': link[3]}
                        links.append(_link)
                temp_cell = Cell()
                temp_cell.setPalette(self._palSCI)
                temp_cell.setLinks(links)
                temp_cell.LoadCell(v_cell_header, im, pk, ln, True)
                loop._cells[j] = temp_cell
            self._loops.append(loop)
            # The following wont work atm, but it's more or less what Enrico's code does. Why? Ignoring for now.
            # self._cellRecSize = ViewCellHeader.size()


    def displayPalette(self, draw=True):
        # TODO: This has been changed, so it doesn't require numpy
        # however, it isn't used atm, so I have not tested it since it's been changed
        flat_rgb_list = [[x.red, x.green, x.blue] for x in self._palSCI._palData]
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


if __name__ == '__main__':
    import json

    in_dir = '../../Resources/56_Files'
    out_dir = '../../Resources/views'
    try:
        os.mkdir(realpath(out_dir))
    except FileExistsError:
        pass

    v56Files = [os.path.join(in_dir, x) for x in os.listdir(in_dir) if x.lower().endswith('.v56')]
    # v56Files = [os.path.join(in_dir, x) for x in os.listdir(in_dir) if x.lower() == '101.v56']
    for count, file_name in enumerate(v56Files):
        print(f"{count+1}/{len(v56Files)}")
        # loop = 0 #(0 if len(argv) < 3 else int(argv[2]))
        # cell = 0 #(0 if len(argv) < 4 else int(argv[3]))
        v : V56file = V56file(file_name)
        info = {}
        combined_height = 0
        combined_width = 0
        all_loops = []
        info['loops'] = {}
        valid_loops = []
        for loop_idx, loop in enumerate(v._loops):
            all_cells = []
            loop_cells = loop._cells
            loop_info = {"cells":{}}
            if loop._mirror:
                loop_cells = v._loops[loop._basedOnLoop]._cells
                loop_info['mirror'] = True
                loop_info['basedOn'] = loop._basedOnLoop
            if len(loop_cells) == 0:
                continue
            for cell_idx, cell in enumerate(loop_cells):
                if loop._mirror:
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
        v.displayPalette(False).save(f"{out_dir}/{view_name}_pal.png")
        with open(f"{out_dir}/{view_name}.json", "w") as json_out:
            json.dump(info, json_out, indent=2)


        # TODO: handle _basedOnLoop and _mirror
        # sci_loop = v._loops[loop]
        # sci_cell = sci_loop._cells[cell]
        # im = sci_cell.get_pil_image(draw=False)
