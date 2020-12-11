import os
from struct import *
from os.path import realpath

from PIL.Image import Image

from scires.legacy.palette import Palette
from scires.legacy.scicell import Cell, CellHeader

P56PATCH = 0x00000101
P56PATCH80 = 0x00008181
P56PATCHOLD = 0x00008081

class P56HEAD:
    def __init__(self, binary_data=None, offset=0):
        self.new_head = P56HEAD32()
        self.old_head = None


class P56HEAD32:
    # TODO: doesn't handle old headers
    def __init__(self, binary_data=None, offset=0):
        self.cell_offset = None
        self.num_cells = None
        self.is_compressed = None
        self.cell_rec_size = None
        self.pallete_offset = None
        self.width = None
        self.height = None

        self.format = 'Hb?hhxxhh'

        if binary_data is not None:
            self.unpack(binary_data, offset)

    def size(self):
        return calcsize(self.format)

    def unpack(self, binary_data, offset=0):
        start_idx = offset
        end_idx = offset + self.size()
        binary_blob = binary_data[start_idx:end_idx]
        args = unpack(self.format, binary_blob)
        self.cell_offset = args[0]
        self.num_cells = args[1]
        self.is_compressed = args[2]
        self.cell_rec_size = args[3]
        self.pallete_offset = args[4]
        self.width = args[5]
        self.height = args[6]


class p56file32:
    def __init__(self, file_name: str):
        self.id = os.path.splitext(os.path.split(file_name)[-1])[0]
        self._cellsCount = None
        self.cells = []
        self.palette = Palette()
        self._isOldFormat = False
        self._isCompressed = None
        self._cellRecSize = None
        self.maxWidth = None
        self.maxHeight = None
        self._unkShort = None
        self._unkByte = None
        self._tDepth = None
        self._vectorSize = None
        self._vector = None
        self._unkLong1 = None
        self._unkLong2 = None
        self._unkLong3 = None
        self._priBars = None
        self._unkShort1 = None
        self._unkShort2 = None

        self.p56 = self.loadFile(file_name)

    def loadFile(self, file_name: str):
        with open(file_name, 'rb') as p56_file:
            binary_data = p56_file.read()
        patch_info = unpack('i', binary_data[:4])[0]
        if patch_info in [P56PATCH80, P56PATCH]:
            offset = 4
        elif patch_info == P56PATCHOLD:
            offset = 26

        hsize = unpack('h', binary_data[offset:offset + 2])[0]
        if hsize == 14:
            self._isOldFormat = False
        elif hsize == 38:
            self._isOldFormat = True
        else:
            raise (Exception("ID_WRONGHEADER"))

        if not self._isOldFormat:
            cellRecSize = unpack('h', binary_data[offset + 4:offset + 6])[0]
            if cellRecSize != 42:
                raise (Exception("ID_WRONGHEADER"))

        if self._isOldFormat:
            raise Exception("Unsupported Picture Version")

        pheader = P56HEAD32(binary_data, offset)

        self._cellsCount = pheader.num_cells
        self.cells = []
        for i in range(self._cellsCount):
            self.cells.append(Cell())
        self._isCompressed = pheader.is_compressed
        self._cellRecSize = pheader.cell_rec_size
        self.maxWidth = pheader.width
        self.maxHeight = pheader.height

        pre_palette_tag_offset = offset + pheader.pallete_offset - 6
        t_tag = unpack('h', binary_data[pre_palette_tag_offset:pre_palette_tag_offset + calcsize('h')])[0]
        if t_tag != 0x0300:
            raise (Exception('ID_WRONGPALLETELOC'))

        absolute_pal_offset = pre_palette_tag_offset + calcsize('h')
        t_pal_size = unpack('i', binary_data[absolute_pal_offset: absolute_pal_offset + calcsize('i')])[0]

        new_offset = self.palette.loadPalette(binary_data, t_pal_size, absolute_pal_offset + 4)

        if self._isOldFormat and self._cellsCount > 0:
            self._unkShort1 = unpack('h', binary_data[new_offset:new_offset + 2])[1]
            self._unkShort2 = unpack('h', binary_data[new_offset + 2:new_offset + 4])[1]
            new_offset += 4
        if self._cellsCount > 0:
            if self._isOldFormat:
                # TODO: old format
                pass
            else:
                tcellHeader = [CellHeader()] * self._cellsCount
                cell_header_offset = offset + pheader.cell_offset
                for i, cellHeader in enumerate(tcellHeader):
                    pk = 0
                    ln = 0
                    cellHeader.unpack(binary_data, cell_header_offset)
                    cell_header_offset += cellHeader.size()
                    if cellHeader.compression == 0:
                        im_size = cellHeader.width * cellHeader.height
                    else:
                        im_size = cellHeader.image_size
                    im_offset = offset + cellHeader.image_offset
                    im = unpack(im_size * 'B', binary_data[im_offset:im_offset + calcsize(im_size * 'b')])
                    if cellHeader.compression != 0:
                        pack_data_offset = cellHeader.pack_data_offset
                        pk_size = cellHeader.image_and_pack_size - cellHeader.image_size
                        # TODO: compression
                        print("Compressed! Do This!")
                        pass
                    temp_cell = Cell()
                    temp_cell.header = cellHeader
                    temp_cell.setPalette(self.palette)
                    temp_cell.LoadCell(cellHeader, im, pk, ln, False)
                    self.cells[i] = temp_cell


def serializeToJson(picture: p56file32):
    c = picture.cells[0]
    info = {"cells": {}}
    info['cells'][0] = c.serialize()
    cell_info = info['cells'][0]
    cell_info['spriteX'] = 0
    cell_info['spriteY'] = 0
    img: Image = c.get_pil_image(draw=False)
    img.save(f"{out_dir}/{f[:f.find('.p56')]}.png")
    pal: Image = c.display_palette(False)
    pal.save(f"{out_dir}/{f[:f.find('.p56')]}_pal.png")
    with open(f"{out_dir}/{f[:f.find('.p56')]}.json_output", "w") as json_out:
        json.dump(info, json_out, indent=2)


if __name__ == '__main__':
    in_dir = '../../Resources/56_Files'
    out_dir = '../../Resources/json_output/pictures'
    import json
    try:
        os.mkdir(realpath(out_dir))
    except FileExistsError:
        pass
    sum_old = 0.0
    sum_new = 0.0
    for f in [x for x in os.listdir(in_dir) if x.lower().endswith('.p56')]:
        filename = f"{in_dir}/{f}"
        p : p56file32 = p56file32(filename)
        serializeToJson(p)
