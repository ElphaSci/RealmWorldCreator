class BITMAPINFOHEADER:
    def __init__(self):
        self.biSize = None
        self.biWidth = None
        self.biHeight = None
        self.biPlanes = None
        self.biBitCount = None
        self.biCompression = None
        self.biSizeImage = None
        self.biXPelsPerMeter = None
        self.biYPelsPerMeter = None
        self.biClrUsed = None
        self.biClrImportant = None


class BITMAPINFO:
    def __init__(self):
        self.bmiHeader = None  # TODO: RGBQUAD
        self.bmiColors = None
