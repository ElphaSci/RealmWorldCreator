import struct

from PyFotoSCIop.source.scicell import Cell


class LOOPHEADER:
    def __init__(self, binary_data, offset=0):
        self.BasedOnLoop = None  # char
        self.Mirror = None  # bool
        self.NumberOfCells = None  # unsigned char
        self.UnkLong1 = None  # long
        self.UnkByte = None  # char
        self.UnkLong2 = None  # long
        self.CellsOffs = None  # unsigned long
        # 'b?Bibii is correct, and should have size of 16, but for some reason why you calculate the size it asks for 20 bytes? I have to read each one individually..
        self.format = 'b?Bibii'
        if binary_data:
            self.unpack(binary_data, offset)

    def size(self):
        indiv_sum = 0
        for c in self.format:
            indiv_sum += struct.calcsize(c)
        return indiv_sum

    def unpack(self, binary_data, offset=0):
        start = offset
        end = start + self.size()
        binary_slice = binary_data[start:end]
        args = []
        t_offset = 0
        for f in self.format:
            s = struct.calcsize(f)
            args.append(struct.unpack_from(f, binary_slice[t_offset:])[0])
            t_offset += s
        # args = struct.unpack(self.format, binary_slice)
        self.BasedOnLoop = args[0]
        self.Mirror = args[1]
        self.NumberOfCells = args[2]
        self.UnkLong1 = args[3]
        self.UnkByte = args[4]
        self.UnkLong2 = args[5]
        self.CellsOffs = args[6]
        pass


class Loop:
    def __init__(self):
        self._cells = None
        self._cellsCount = None
        self._selectedCell = None
        self._basedOnLoop = None
        self._mirror = None
        self._unkLonk1 = None
        self._unkByte = None
        self._unkLong2 = None
        self.loopHeader = None

    def LoadLoop(self, loopheader: LOOPHEADER):
        self._cellsCount = loopheader.NumberOfCells
        self._cells = [Cell()] * self._cellsCount
        self._basedOnLoop = loopheader.BasedOnLoop
        self._mirror = loopheader.Mirror
        self._unkByte = loopheader.UnkByte
        self._unkLonk1 = loopheader.UnkLong1
        self._unkLong2 = loopheader.UnkLong2
        self.loopHeader = loopheader

    def RestoreLoopHeader(self):
        return self.loopHeader

    def AddCell(self, cell):
        self._cells.append(cell)
