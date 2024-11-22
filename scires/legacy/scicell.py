import struct

from PIL import Image

from scires.legacy.palette import Palette


class CellHeader:
    def __init__(self, binary_data=None, offset=0):
        self.width = None  # short
        self.height = None  # short
        self.x_shift = None  # short
        self.y_shift = None  # short
        self.transparent_color = None  # char
        self.compression = None  # char
        self.flags = None  # short
        self.image_and_pack_size = None  # unsigned long
        self.image_size = None  # unsigned long
        self.palette_offset = None  # unsigned long

        # IMPORTANT WHEN EDITING OR LOADING CHECK IF != 0
        self.image_offset = None  # unsigned long
        self.pack_data_offset = None  # unsigned long; color offset?
        self.lines_offset = None  # unsigned long; row table offest?
        self.z_depth = None  # short; priority?
        self.x_pos = None  # short
        self.y_pos = None  # short

        # format to use to unpack this data from bytes:
        # TODO: Test this, I use unsigned int here, even though c++ struct used ulong. I think uint is right.
        # TODO: I use unsigned char here (B) I am pretty sure it's right, but should verify
        self.format = '4h2Bh6I3h'

        if binary_data is not None:
            self.unpack(binary_data, offset)

    def size(self):
        return struct.calcsize(self.format)

    def unpack(self, binary_data, offset=0):
        start_idx = offset
        end_idx = offset + self.size()
        args = struct.unpack(self.format, binary_data[start_idx:end_idx])
        self.width = args[0]
        self.height = args[1]
        self.x_shift = args[2]
        self.y_shift = args[3]
        self.transparent_color = args[4]
        self.compression = args[5]
        self.flags = args[6]
        self.image_and_pack_size = args[7]
        self.image_size = args[8]
        self.palette_offset = args[9]

        # IMPORTANT WHEN EDITING args
        self.image_offset = args[10]
        self.pack_data_offset = args[11]
        self.lines_offset = args[12]
        self.z_depth = args[13]
        self.x_pos = args[14]
        self.y_pos = args[15]
        pass


class ViewCellHeader:
    def __init__(self, binary_data=None, offset=0):
        self.cellOffset = None
        self.width = None  # short
        self.height = None  # short
        self.x_shift = None  # short
        self.y_shift = None  # short
        self.transparent_color = None  # char
        self.compression = None  # char
        self.flags = None  # short
        self.image_and_pack_size = None  # unsigned long
        self.image_size = None  # unsigned long
        self.palette_offset = None  # unsigned long

        # IMPORTANT WHEN EDITING OR LOADING CHECK IF != 0
        self.image_offset = None  # unsigned long
        self.pack_data_offset = None  # unsigned long
        self.lines_offset = None  # unsigned long
        self.link_table_offset = None  # Int32
        self.link_number = None  # UInt16

        # format to use to unpack this data from bytes:
        # TODO: Test this, I use unsigned int here, even though c++ struct used ulong. I think uint is right.
        # self.format = 'hhhhbbhIIIIII'
        self.format = '4h2Bh6IIh'

        if binary_data is not None:
            self.unpack(binary_data, offset)

    def size(self):
        return struct.calcsize(self.format)

    def unpack(self, binary_data, offset=0):
        self.cellOffset = offset
        start_idx = offset
        end_idx = offset + self.size()
        args = struct.unpack(self.format, binary_data[start_idx:end_idx])
        self.width = args[0]
        self.height = args[1]
        self.x_shift = args[2]
        self.y_shift = args[3]
        self.transparent_color = args[4]
        self.compression = args[5]
        self.flags = args[6]
        self.image_and_pack_size = args[7]
        self.image_size = args[8]
        self.palette_offset = args[9]

        # IMPORTANT WHEN EDITING args
        self.image_offset = args[10]
        self.pack_data_offset = args[11]
        self.lines_offset = args[12]
        self.link_table_offset = args[13]
        self.link_number = args[14]
        pass


class Cell:
    def __init__(self):
        self._isView: bool = False
        self.links = []
        self.header: ViewCellHeader = None
        self.image = None  # uchar
        self.pack = None  # uchar
        self.lines = None  # uchar
        self.cached = None  # uchar
        self.changed = None  # bool
        self.palette = Palette()
        self.new_cell = None  # CellHeader
        self.old_cell = None  # ViewCellHeader

    def setLinks(self, links):
        self.links = links

    def serialize(self) -> dict:
        info = {}
        info["width"] = self.width
        info["height"] = self.height
        info["left"] = self.x_shift
        info["top"] = self.y_shift
        info["transparentPalIdx"] = self.skip_color
        info["zDepth"] = self.z_depth
        info["xPos"] = self.x_pos
        info["yPos"] = self.y_pos
        if len(self.links) > 0:
            info['links'] = self.links
        return info

    def setPalette(self, palette):
        self.palette = palette
        if self.cached and self.image != self.cached:
            self.cached = None

    @property
    def width(self):
        return self.header.width

    @property
    def height(self):
        return self.header.height

    @property
    def y_shift(self):
        return self.header.y_shift

    @property
    def x_shift(self):
        return self.header.x_shift

    @property
    def skip_color(self):
        return self.header.transparent_color

    @property
    def compression(self):
        return self.header.compression


    @property
    def flags(self):
        return self.header.flags

    @property
    def z_depth(self):
        if (self._isView):
            return 0
        return self.header.z_depth

    @property
    def x_pos(self):
        if (self._isView):
            return 0
        return self.header.x_pos


    @property
    def y_pos(self):
        if (self._isView):
            return 0
        return self.header.y_pos

    @property
    def image_size(self):
        if (self.compression):
            return self.header.image_size
        return self.height * self.width

    @property
    def pack_size(self):
        if (self.compression):
            return self.header.image_and_pack_size - self.header.image_size
        return 0


    def LoadCell(self, cell_header: ViewCellHeader, image, pack, lines, isView):
        self.header = cell_header
        self._isView = isView
        self.image = image
        self.pack = pack
        self.lines = lines

    def get_pil_image(self, draw=False, transparent=True) -> Image:
        if self.compression != 0:
            ptags = iter(self.image)
            pdata = iter(self.pack)
            pal_data = self.palette.pal_data
            rgba_im = []
            last_pal_entry = pal_data[255]
            # this is typically the transparent color, if not, it will set that below
            last_rgba = [last_pal_entry.red, last_pal_entry.green, last_pal_entry.blue, 0]
            last_rgba_opaque = [last_pal_entry.red, last_pal_entry.green, last_pal_entry.blue, 255]
            for i in range(self.height):
                cur_width = 0
                while cur_width < self.width:
                    switch = next(ptags)
                    if switch >> 6 == 2:
                        color = next(pdata)
                        pal_entry = pal_data[color]
                        if color == self.skip_color and transparent:
                            rgba_im.extend([pal_entry.red, pal_entry.green, pal_entry.blue, 0] * (switch - 0x80))
                        else:
                            rgba_im.extend([pal_entry.red, pal_entry.green, pal_entry.blue, 255] * (switch - 0x80))
                        cur_width += switch - 0x80
                    elif switch >> 6 == 3:
                        if 255 != self.skip_color or not transparent:
                            rgba_im.extend(last_rgba_opaque * (switch - 0xC0))
                        else:
                            rgba_im.extend(last_rgba * (switch - 0xC0))
                        cur_width += switch - 0xC0
                    else:
                        for j in range(switch):
                            col = next(pdata)
                            pal_entry = pal_data[col]
                            if col == self.skip_color and transparent:
                                rgba_im.extend([pal_entry.red, pal_entry.green, pal_entry.blue, 0])
                            else:
                                rgba_im.extend([pal_entry.red, pal_entry.green, pal_entry.blue, 255])
                        cur_width += switch
            pil_im = Image.frombuffer('RGBA', (self.width, self.height), bytes(rgba_im), 'raw', 'RGBA', 0, 1)
            if draw:
                import matplotlib.pyplot as plt
                plt.imshow(pil_im, interpolation='none')
                plt.show()
            return pil_im
        else:
            image = self.image
            pal_data = self.palette.pal_data
            rgba_im = []
            for x in image:
                color = [pal_data[x].red, pal_data[x].green, pal_data[x].blue, 255]
                if transparent and x == self.skip_color:
                    color[-1] = 0
                rgba_im += color
            width = int(len(rgba_im) / (self.height * 4))
            pil_im = Image.frombuffer('RGBA', (width, self.height), bytes(rgba_im), 'raw', 'RGBA', 0, 1)
            if draw:
                import matplotlib.pyplot as plt
                plt.imshow(pil_im, interpolation='none')
                plt.show()
            return pil_im

    def displayPalette(self, draw=True):
        # TODO: This has been changed, so it doesn't require numpy
        # however, it isn't used atm, so I have not tested it since it's been changed
        flat_rgb_list = [[x.red, x.green, x.blue] for x in self.palette.pal_data]
        rgba_im = []
        for x in flat_rgb_list:
            rgba_im.extend(x)
        pil_im = Image.frombuffer('RGB', (16, 16), bytes(rgba_im), 'raw', 'RGB', 0, 1)
        if draw:
            import matplotlib.pyplot as plt
            plt.imshow(pil_im, interpolation='none')
            plt.show()
        else:
            return pil_im
