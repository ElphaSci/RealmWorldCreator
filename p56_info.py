class PicInfo:
    def __init__(self, number=0, roomtype='', picture=0, vanishing_x=160, vanishing_y=0, frontsize=128, backsize=40,
                 front_y=310, back_y=140, horizon=130, scaled=True, polylist=0, scalebase=128):
        attributes = ['number', 'roomtype', 'picture', 'vanishing_x', 'vanishing_y', 'frontsize', 'backsize', 'front_y',
                      'back_y', 'horizon', 'scaled', 'polylist', 'scalebase']
        for attr in attributes:
            setattr(self, attr, eval(attr))

    def frontPercent(self):
        return self.frontsize / self.scalebase

    def backPercent(self):
        return self.backsize / self.scalebase

    def slopeNum(self):
        return self.frontPercent() - self.backPercent()

    def slopeDenom(self):
        return self.front_y - self.back_y

    def slope(self):
        return self.slopeNum() / self.slopeDenom()

    def scale_constant(self):
        return self.backPercent() - self.slope() * self.back_y


pics = [PicInfo(picture=3000, roomtype='FOREST'), PicInfo(picture=3001, roomtype='FOREST'),
        PicInfo(picture=3009, roomtype='FOREST', horizon=130, back_y=1, backsize=80),
        PicInfo(picture=3404, roomtype='DESERT'), PicInfo(picture=3405, roomtype='DESERT'),
        PicInfo(picture=3030, roomtype='BEACH'), PicInfo(picture=3031, roomtype='BEACH'),
        PicInfo(picture=3032, roomtype='BEACH'),
        PicInfo(picture=3500, roomtype='TOWN1', horizon=100, back_y=160, backsize=80, front_y=320, frontsize=80),
        PicInfo(picture=4000, roomtype='TOWN1INT', horizon=90, back_y=160, backsize=80, front_y=320, frontsize=80),
        PicInfo(picture=4001, roomtype='TOWN1INT', horizon=90, back_y=160, backsize=80, front_y=320, frontsize=80),
        PicInfo(picture=3201, roomtype='HOUSE1', horizon=90, back_y=160, backsize=80, front_y=320, frontsize=80),
        PicInfo(picture=3300, roomtype='HOUSE1INT', horizon=90, back_y=160, backsize=80, front_y=320, frontsize=80),
        PicInfo(picture=3071, roomtype='DUNGEON', back_y=160, backsize=112, front_y=320, frontsize=112),
        PicInfo(picture=6500, roomtype='SWAMP', horizon=130, back_y=1, backsize=80),
        PicInfo(picture=6501, roomtype='SWAMP')]

global PIC_INFO
PIC_INFO = {}
for pic in pics:
    PIC_INFO[pic.picture] = pic
