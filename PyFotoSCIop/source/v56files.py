import os
import struct
import sys

sys.path.append('../../')

from PyFotoSCIop.source.palette import Palette
from PyFotoSCIop.source.scicell import ViewCellHeader, Cell
from PyFotoSCIop.source.sciloop import Loop, LOOPHEADER

V56PATCH = 0x008080
V56PATCH84 = 0x008480


class V56HEAD:
    def __init__(self, binary_data=None, offset=0):
        self._attribute_fields = ["LoopTblOff", "LoopCount", "Unk1", "Compressed", "ViewSize", "CellsCount",
                                  "PalOffset", "LoopRecSize", "CellRecSize", "ResolutionX", "ResolutionY"]

        self._format = 'HBb?BHIBBHH'
        if binary_data:
            self.unpack(binary_data, offset)

    def size(self):
        return struct.calcsize(self._format)

    def unpack(self, binary_data, offset=0):
        start = offset
        end = start + self.size()
        binary_slice = binary_data[start:end]
        args = struct.unpack(self._format, binary_slice)
        for i,x in enumerate(self._attribute_fields):
            self.__setattr__(x, args[i])


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
                temp_cell = Cell()
                temp_cell.setPalette(self._palSCI)
                temp_cell.LoadCell(v_cell_header, im, pk, ln, True)
                loop._cells[j] = temp_cell
            self._loops.append(loop)
            # The following wont work atm, but it's more or less what Enrico's code does. Why? Ignoring for now.
            # self._cellRecSize = ViewCellHeader.size()


if __name__ == '__main__':
    from sys import argv

    files = [os.path.join(argv[1], x) for x in os.listdir(argv[1])]
    for file_name in files:
        loop = 0  # (0 if len(argv) < 3 else int(argv[2]))
        cell = 0  # (0 if len(argv) < 4 else int(argv[3]))
        v = V56file(file_name)
        # TODO: handle _basedOnLoop and _mirror
        sci_loop = v._loops[loop]
        sci_cell = sci_loop._cells[cell]
        im = sci_cell.get_pil_image(draw=False)
