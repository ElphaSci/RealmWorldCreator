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
        self.pal_id = None  # short
        self.unk_bytes_1 = None  # char[11]
        self.data_length = None  # short
        self.unk_bytes_2 = None  # char[10]
        self.first_color = None  # short
        self.unk_bytes_3 = None  # short
        self.num_colors = None  # short
        self.exfour_color = None  # char
        self.triple_color = None  # char
        self.unk_bytes_4 = None  # long
        # TODO: Test format. Weird, it seems like the dataLength short should be little endian...
        self.format = '<h11sH10shhhbbi'

    def size(self):
        return struct.calcsize(self.format)

    def unpack(self, binary_data, offset=0):
        start = offset
        end = offset + self.size()
        args = struct.unpack(self.format, binary_data[start:end])
        self.pal_id = args[0]
        self.unk_bytes_1 = args[1]
        self.data_length = args[2]  # seems to be ignored.
        self.unk_bytes_2 = args[3]
        self.first_color = args[4]
        self.unk_bytes_3 = args[5]
        self.num_colors = args[6]
        self.exfour_color = args[7]
        self.triple_color = args[8]
        self.unk_bytes_4 = args[9]


class Palette:
    def __init__(self):
        self.header: PalHeader
        self.pal_data = [PalEntry()] * 256  # [PalEntry]*256
        self._unkBytes1 = None  # [char]*11
        self._unkBytes2 = None  # [char]*10
        self._unkShort = None  # short
        self._unkLong = None  # long
        self.has_palette = None  # bool

    @property
    def pal_id(self):
        return self.header.pal_id

    @property
    def first_color(self):
        return self.header.first_color

    @property
    def num_colors(self):
        return self.header.num_colors

    @property
    def has_four_entries(self):
        return self.header.triple_color == 0

    @property
    def exfour_color(self):
        return self.header.exfour_color

    def loadPalette(self, file_data, palette_size=None, palette_offset=0):
        start = palette_offset
        end = start + struct.calcsize('h')
        tcheck = struct.unpack('h', file_data[start:end])[0]
        self.header = PalHeader()

        if tcheck != PALPATCH80 and tcheck != PALPATCH:
            self.header.unpack(file_data, start)
            palette_offset += self.header.size()

            if self.header.data_length + 15 != palette_size:
                return False
        else:
            self.header.unpack(file_data, palette_offset + 2)
            palette_offset += 2 + self.header.size()

        if self.header.triple_color:
            data = []
            offset = palette_offset
            for i in range(self.header.num_colors):
                peo = PalEntryOld(file_data, offset)
                data.append(peo)
                offset += peo.size()
        else:
            data = []
            offset = palette_offset
            for i in range(self.header.num_colors):
                pe = PalEntry(file_data, offset)
                data.append(pe)
                offset += pe.size()

        self._unkBytes1 = self.header.unk_bytes_1[:11]
        self._unkBytes2 = self.header.unk_bytes_2[:10]
        self._unkShort = self.header.unk_bytes_3
        self._unkLong = self.header.unk_bytes_4

        if self.has_four_entries:
            for i in range(self.num_colors):
                self.pal_data[i + self.first_color] = data[i]
        else:
            for i in range(self.num_colors):
                self.pal_data[i + self.first_color] = data[i]
                self.pal_data[i + self.first_color].remap = 0

        self.has_palette = True
        return offset

    def noPalette(self):
        for i in range(256):
            pe = PalEntry()
            pe.blue = 255 - i
            pe.green = 255 - i
            pe.red = 255 - i
            pe.remap = 0
            self.pal_data[i] = pe
            self.has_palette = False
