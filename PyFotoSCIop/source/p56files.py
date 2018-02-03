from struct import *

from PyFotoSCIop.source.palette import Palette
from PyFotoSCIop.source.scicell import Cell, CellHeader

P56PATCH = 0x00000101
P56PATCH80 = 0x00008181
P56PATCHOLD = 0x00008081


def intFromBytes(self, bytes):
    byte_array = bytearray(bytes)
    byte_array.reverse()
    integer = int.from_bytes(byte_array, 'big')
    return integer


class P56HEAD:
    def __init__(self, binary_data=None, offset=0):
        self.new_head = P56HEAD32()
        self.old_head = None


class P56HEAD32:
    # TODO: doesn't handle old headers
    def __init__(self, binary_data=None, offset=0):
        self.cellsOffset = None
        self.numCells = None
        self.isCompressed = None
        self.cellRecSize = None
        self.palleteOffset = None
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
        args = unpack(self.format, binary_data[start_idx:end_idx])
        self.cellsOffset = args[0]
        self.numCells = args[1]
        self.isCompressed = args[2]
        self.cellRecSize = args[3]
        self.palleteOffset = args[4]
        self.width = args[5]
        self.height = args[6]


class p56file32:
    def __init__(self, file_name: str):
        self.id = os.path.splitext(os.path.split(file_name)[-1])[0]
        self._cellsCount = None
        self._cells = []
        self._palSCI = Palette()
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
        self._myHwnd = None  # TODO: Do I even plan on using this?

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

        pheader = P56HEAD()
        if self._isOldFormat:
            # old_header = P56HEADOLD(binary_data, offset)
            # pheader.old_head = header
            # self._cellsCount =
            pass
        else:
            new_head = P56HEAD32(binary_data, offset)
            pheader.new_head = new_head

            self._cellsCount = new_head.numCells
            self._cells = []
            for i in range(self._cellsCount):
                self._cells.append(Cell())
            self._isCompressed = new_head.isCompressed
            self._cellRecSize = new_head.cellRecSize
            self.maxWidth = new_head.width
            self.maxHeight = new_head.height

        pallete_offset = offset - 6 + new_head.palleteOffset
        t_tag = unpack('h', binary_data[pallete_offset:pallete_offset + calcsize('h')])[0]
        if t_tag != 0x0300:
            raise (Exception('ID_WRONGPALLETELOC'))

        pal_size_offset = pallete_offset + calcsize('h')
        t_pal_size = unpack('i', binary_data[pal_size_offset: pal_size_offset + calcsize('i')])[0]

        new_offset = self._palSCI.loadPalette(binary_data, t_pal_size, pal_size_offset + 4)  # TODO: TEST

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
                cell_header_offset = offset + pheader.new_head.cellsOffset
                for i, cellHeader in enumerate(tcellHeader):
                    pk = 0
                    ln = 0
                    cellHeader.unpack(binary_data, cell_header_offset)
                    cell_header_offset += cellHeader.size()
                    if cellHeader.compression == 0:
                        im_size = cellHeader.width * cellHeader.height
                    else:
                        im_size = cellHeader.imageSize
                    im_offset = offset + cellHeader.imageOffs
                    im = unpack(im_size * 'B', binary_data[im_offset:im_offset + calcsize(im_size * 'b')])
                    if cellHeader.compression != 0:
                        pack_data_offset = cellHeader.packDataOffs
                        pk_size = cellHeader.imageandPackSize - cellHeader.imageSize
                        # TODO: compression
                        print("Compressed! Do This!")
                        pass
                    temp_cell = Cell()
                    temp_cell.setPalette(self._palSCI)
                    temp_cell.LoadCell(cellHeader, im, pk, ln, False)
                    self._cells[i] = temp_cell


if __name__ == '__main__':
    import os

    for f in [x for x in os.listdir('../p56_files') if '.p56' in x]:
        print(f)
        p = p56file32('../p56_files/' + f)  # '../p56_files/3.p56')
        c = p._cells[0]
        c.get_pil_image(draw=True)
        #     c.displayPalette()
