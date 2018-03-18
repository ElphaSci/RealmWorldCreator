import struct


from PIL import Image

from PyFotoSCIop.source.bmp import BITMAPINFO
from PyFotoSCIop.source.palette import Palette


class CellHeader:
    def __init__(self, binary_data=None, offset=0):
        self.width = None  # short
        self.height = None  # short
        self.xShift = None  # short
        self.yShift = None  # short
        self.transparentClr = None  # char
        self.compression = None  # char
        self.flags = None  # short
        self.imageandPackSize = None  # unsigned long
        self.imageSize = None  # unsigned long
        self.paletteOffs = None  # unsigned long

        # IMPORTANT WHEN EDITING OR LOADING CHECK IF != 0
        self.imageOffs = None  # unsigned long
        self.packDataOffs = None  # unsigned long
        self.linesOffs = None  # unsigned long
        self.zDepth = None  # short
        self.xPos = None  # short
        self.yPos = None  # short

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
        self.xShift = args[2]
        self.yShift = args[3]
        self.transparentClr = args[4]
        self.compression = args[5]
        self.flags = args[6]
        self.imageandPackSize = args[7]
        self.imageSize = args[8]
        self.paletteOffs = args[9]

        # IMPORTANT WHEN EDITING args
        self.imageOffs = args[10]
        self.packDataOffs = args[11]
        self.linesOffs = args[12]
        self.zDepth = args[13]
        self.xPos = args[14]
        self.yPos = args[15]
        pass


class ViewCellHeader:
    def __init__(self, binary_data=None, offset=0):
        self.width = None  # short
        self.height = None  # short
        self.xShift = None  # short
        self.yShift = None  # short
        self.transparentClr = None  # char
        self.compression = None  # char
        self.flags = None  # short
        self.imageandPackSize = None  # unsigned long
        self.imageSize = None  # unsigned long
        self.paletteOffs = None  # unsigned long

        # IMPORTANT WHEN EDITING OR LOADING CHECK IF != 0
        self.imageOffs = None  # unsigned long
        self.packDataOffs = None  # unsigned long
        self.linesOffs = None  # unsigned long

        # format to use to unpack this data from bytes:
        # TODO: Test this, I use unsigned int here, even though c++ struct used ulong. I think uint is right.
        # self.format = 'hhhhbbhIIIIII'
        self.format = '4h2Bh6I'

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
        self.xShift = args[2]
        self.yShift = args[3]
        self.transparentClr = args[4]
        self.compression = args[5]
        self.flags = args[6]
        self.imageandPackSize = args[7]
        self.imageSize = args[8]
        self.paletteOffs = args[9]

        # IMPORTANT WHEN EDITING args
        self.imageOffs = args[10]
        self.packDataOffs = args[11]
        self.linesOffs = args[12]
        # self.zDepth = args[13]


class Cell:
    def __init__(self):
        self._width = None  # ushort
        self._height = None  # ushort
        self._left = None  # short
        self._top = None  # short
        self._skpColor = None  # uchar
        self._compression = None  # uchar
        self._flags = None  # ushort
        self._image = None  # uchar
        self._imageSize = None  # ulong (int?)
        self._pack = None  # uchar
        self._packSize = None  # ulong(int?)
        self._lines = None  # uchar
        self._cachedHeader = BITMAPINFO()
        self._cached = None  # uchar
        self._changed = None  # bool
        self._zDepth = None  # short
        self._xPos = None  # ushort
        self._yPos = None  # ushort
        self._palette = Palette()
        self.new_cell = None  # CellHeader
        self.old_cell = None  # ViewCellHeader

    def union(self, new_cell_header, old_cell_header):
        self.new_cell = new_cell_header
        self.old_cell = old_cell_header

    def makeSCI(self):
        if self._cached and self._cachedHeader:
            self_width = self._cachedHeader

    def makeBitmap(self):
        image_size = self._width * self._height
        dw_remaineder = self._width % 4
        if dw_remaineder:
            image_size += self._height * (4 - dw_remaineder)

        biBitCount = 9
        biClrImportant = 256
        biClrUsed = 256
        # biCompression = BI_RGB
        biHeight = self._height
        biPlane = 1
        # biSize = sizeof(BITMAPINFOHEADER)
        biSizeImage = image_size
        biWidth = self._width
        biXPelsPerMeter = 0
        biYPelsPerMeter = 0
        bmiColors = [] * 256

        for i in range(256):
            try:
                t_pal = self._palette[i]
            except:
                pass
            if t_pal:
                pass

    def setPalette(self, palette):
        self._palette = palette
        if self._cached and self._image != self._cached:
            self._cached = None
        if self._cachedHeader:
            self._cachedHeader = None
            self._cached = None

    def LoadCell(self, cell_header, image, pack, lines, isView):
        self._image = image
        self._pack = pack
        self._lines = lines

        self._width = cell_header.width
        self._height = cell_header.height
        self._left = cell_header.xShift
        self._top = cell_header.yShift
        self._skpColor = cell_header.transparentClr
        self._compression = cell_header.compression
        self._flags = cell_header.flags

        if isView:
            self._zDepth = 0
            self._xPos = 0
            self._yPos = 0
        else:
            self._zDepth = cell_header.zDepth
            self._xPos = cell_header.xPos
            self._yPos = cell_header.yPos

        if self._compression:
            self._imageSize = cell_header.imageSize
            self._packSize = cell_header.imageandPackSize - self._imageSize
        else:
            self._imageSize = cell_header.height * cell_header.width
            self._packSize = 0

    def get_pil_image(self, draw=False, transparent=True):
        if self._compression != 0:
            ptags = iter(self._image)
            pdata = iter(self._pack)
            pal_data = self._palette._palData
            rgba_im = []
            last_pal_entry = pal_data[255]
            # this is typically the transparent color, if not, it will set that below
            last_rgba = [last_pal_entry.red, last_pal_entry.green, last_pal_entry.blue, 0]
            last_rgba_opaque = [last_pal_entry.red, last_pal_entry.green, last_pal_entry.blue, 255]
            for i in range(self._height):
                cur_width = 0
                while cur_width < self._width:
                    switch = next(ptags)
                    if switch >> 6 == 2:
                        color = next(pdata)
                        pal_entry = pal_data[color]
                        if color == self._skpColor and transparent:
                            rgba_im.extend([pal_entry.red, pal_entry.green, pal_entry.blue, 0] * (switch - 0x80) )
                        else:
                            rgba_im.extend([pal_entry.red, pal_entry.green, pal_entry.blue, 255] * (switch - 0x80) )
                        cur_width += switch - 0x80
                    elif switch >> 6 == 3:
                        if 255 != self._skpColor or not transparent:
                            rgba_im.extend(last_rgba_opaque * (switch - 0xC0))
                        else:
                            rgba_im.extend(last_rgba * (switch - 0xC0))
                        cur_width += switch - 0xC0
                    else:
                        for j in range(switch):
                            col = next(pdata)
                            pal_entry = pal_data[col]
                            if col == self._skpColor and transparent:
                                rgba_im.extend([pal_entry.red, pal_entry.green, pal_entry.blue, 0])
                            else:
                                rgba_im.extend([pal_entry.red, pal_entry.green, pal_entry.blue, 255])
                        cur_width += switch
            pil_im = Image.frombuffer('RGBA', (self._width, self._height), bytes(rgba_im), 'raw', 'RGBA', 0, 1)
            if draw:
                import matplotlib.pyplot as plt
                plt.imshow(pil_im, interpolation='none')
                plt.show()
            return pil_im
        else:
            image = self._image
            pal_data = self._palette._palData
            rgba_im = []
            for x in image:
                color = [pal_data[x].red, pal_data[x].green, pal_data[x].blue, 255]
                if transparent and x == self._skpColor:
                    color[-1] = 0
                rgba_im += color
            width = int(len(rgba_im) / (self._height * 4))
            pil_im = Image.frombuffer('RGBA', (width, self._height), bytes(rgba_im), 'raw', 'RGBA', 0, 1)
            if draw:
                import matplotlib.pyplot as plt
                plt.imshow(pil_im, interpolation='none')
                plt.show()
            return pil_im

    def displayPalette(self, draw=True):
        # TODO: This has been changed, so it doesn't require numpy
        # however, it isn't used atm, so I have not tested it since it's been changed
        flat_rgb_list = [[x.red, x.green, x.blue] for x in self._palette._palData]
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
