import struct

PALPATCH80 = 0x008B
PALPATCH = 0x000B


class PalEntryOld:
    def __init__(self, binary_data=None, offset=0):
        self.red = None  # unsigned char
        self.green = None  # unsigned char
        self.blue = None  # unsigned char

        self.format = 'BBB'
        if binary_data:
            self.unpack(binary_data, offset)

    def size(self):
        return struct.calcsize(self.format)

    def unpack(self, binary_data, offset=0):
        start = offset
        end = start + self.size()
        binary_slice = binary_data[start:end]
        args = struct.unpack(self.format, binary_data[start:end])
        self.red = args[0]
        self.green = args[1]
        self.blue = args[2]


class PalEntry(list):
    def __init__(self, binary_data=None, offset=0):
        self.remap = 0  # unsigned char this is only set by the very first PalEntry in _palData!
        self.red = 0  # unsigned char
        self.green = 0  # unsigned char
        self.blue = 0  # unsigned char
        super(PalEntry, self).__init__([0, 0, 0])

        self.format = 'BBBB'
        if binary_data:
            self.unpack(binary_data, offset)

    def size(self):
        return struct.calcsize(self.format)

    def unpack(self, binary_data, offset=0):
        start = offset
        end = start + self.size()
        binary_slice = binary_data[start:end]
        args = struct.unpack(self.format, binary_data[start:end])
        self.remap = args[0]
        self[0] = self.red = args[1]
        self[1] = self.green = args[2]
        self[2] = self.blue = args[3]
        pass


class PalHeader:
    def __init__(self, binary_data=None, offset=0):
        self.palID = None  # short
        self.unkBytes1 = None  # char[11]
        self.dataLength = None  # short
        self.unkBytes2 = None  # char[10]
        self.firstColor = None  # short
        self.unkShort = None  # short
        self.numColors = None  # short
        self.exfourColor = None  # char
        self.tripleColor = None  # char
        self.unkLong = None  # long
        # TODO: Test format. Weird, it seems like the dataLength short should be little endian...
        self.format = '<h11sH10shhhbbi'

    def size(self):
        return struct.calcsize(self.format)

    def unpack(self, binary_data, offset=0):
        start = offset
        end = offset + self.size()
        args = struct.unpack(self.format, binary_data[start:end])
        self.palID = args[0]
        self.unkBytes1 = args[1]
        self.dataLength = args[2]  # seems to be ignored.
        self.unkBytes2 = args[3]
        self.firstColor = args[4]
        self.unkShort = args[5]
        self.numColors = args[6]
        self.exfourColor = args[7]
        self.tripleColor = args[8]
        self.unkLong = args[9]


class Palette:
    def __init__(self):
        self._palID = None  # short
        self._firstColor = None  # short
        self._numColors = None  # short
        self._hasFourEntries = None  # bool
        self._exfourColor = None  # char
        self._palData = [PalEntry()] * 256  # [PalEntry]*256
        self._unkBytes1 = None  # [char]*11
        self._unkBytes2 = None  # [char]*10
        self._unkShort = None  # short
        self._unkLong = None  # long
        self._hasPalette = None  # bool

    def loadPalette(self, file_data, palette_size, palette_offset=0):
        start = palette_offset
        end = start + struct.calcsize('h')
        tcheck = struct.unpack('h', file_data[start:end])[0]
        head = PalHeader()

        if tcheck != PALPATCH80 and tcheck != PALPATCH:
            head.unpack(file_data, start)
            # TODO: I don't understand. when loading some files, this needs to be ( -4) (3.p56 ,for example) but for other (3000.p56) it needs to be -3?
            # TODO: JK^^^ I think It's always 3 now? but the original code uses 2... hmm
            # palette_offset += head.size() - 4
            palette_offset += head.size()

            # TODO: What does this do? Doesn't seem to be used at all in the original source. Ignoring.
            # Er.... this only works if you read the dataLength as little endian? Gonna ignore for now...
            if head.dataLength + 15 != palette_size:
                return False
        else:
            head.unpack(file_data, palette_offset + 2)
            palette_offset += 2 + head.size()

        if head.tripleColor:
            data = []
            offset = palette_offset
            for i in range(head.numColors):
                peo = PalEntryOld(file_data, offset)
                data.append(peo)
                offset += peo.size()
        else:
            data = []
            offset = palette_offset
            for i in range(head.numColors):
                pe = PalEntry(file_data, offset)
                data.append(pe)
                offset += pe.size()

        self._palID = head.palID
        self._firstColor = head.firstColor
        self._numColors = head.numColors
        self._hasFourEntries = (head.tripleColor == 0)
        self._exfourColor = head.exfourColor
        self._unkBytes1 = head.unkBytes1[:11]
        self._unkBytes2 = head.unkBytes2[:10]
        self._unkShort = head.unkShort
        self._unkLong = head.unkLong

        if self._hasFourEntries:
            for i in range(self._numColors):
                self._palData[i + self._firstColor] = data[i]
        else:
            for i in range(self._numColors):
                self._palData[i + self._firstColor] = data[i]
                self._palData[i + self._firstColor].remap = 0

        self._hasPalette = True
        return offset

    def noPalette(self):
        for i in range(256):
            pe = PalEntry()
            pe.blue = 255 - i
            pe.green = 255 - i
            pe.red = 255 - i
            pe.remap = 0
            self._palData[i] = pe
            self._hasPalette = False
