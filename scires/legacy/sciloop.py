import struct

from scires.legacy.scicell import Cell


class LOOPHEADER:
    def __init__(self, binary_data, offset=0):
        self.based_on_loop = None  # char
        self.mirror = None  # bool
        self.num_cells = None  # unsigned char
        self.unk_long_1 = None  # long
        self.unk_byte = None  # char
        self.unk_long_2 = None  # long
        self.cells_offset = None  # unsigned long
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
        self.based_on_loop = args[0]
        self.mirror = args[1]
        self.num_cells = args[2]
        self.unk_long_1 = args[3]
        self.unk_byte = args[4]
        self.unk_long_2 = args[5]
        self.cells_offset = args[6]
        pass


class Loop:
    def __init__(self):
        self.loopHeader = None
        self.cells = None
        self._selectedCell = None

    @property
    def num_cells(self):
        return self.loopHeader.num_cells

    @property
    def based_on_loop(self):
        return self.loopHeader.based_on_loop

    @property
    def mirror(self):
        return self.loopHeader.mirror

    def LoadLoop(self, loopheader: LOOPHEADER):
        self.loopHeader = loopheader
        self.cells = [Cell()] * self.num_cells

    def RestoreLoopHeader(self):
        return self.loopHeader

    def AddCell(self, cell):
        self.cells.append(cell)
