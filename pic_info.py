class PicInfo:
    def __init__(self, number=0, room_type='', picture=0, vanishing_x=160, vanishing_y=0, front_size=128, back_size=40,
                 front_y=310, back_y=140, horizon=130, scaled=True, polylist=0, scalebase=128):
        attributes = ['number', 'room_type', 'picture', 'vanishing_x', 'vanishing_y', 'front_size', 'back_size', 'front_y',
                      'back_y', 'horizon', 'scaled', 'polylist', 'scalebase']
        for attr in attributes:
            setattr(self, attr, eval(attr))

    def frontPercent(self):
        return self.front_size / self.scalebase

    def backPercent(self):
        return self.back_size / self.scalebase

    def slopeNum(self):
        return self.frontPercent() - self.backPercent()

    def slopeDenom(self):
        return self.front_y - self.back_y

    def slope(self):
        return self.slopeNum() / self.slopeDenom()

    def scale_constant(self):
        return self.backPercent() - self.slope() * self.back_y

    def __repr__(self) -> str:
        return f"{self.room_type}: {self.picture}"


def parse_pic_info_entry(pic_info_sc : str) -> PicInfo:
    import re
    params = {}
    for line in pic_info_sc.splitlines():
        info = line.replace(")", "").replace("(", "").replace(":", "").replace(",", "").strip()
        if len(info) == 0 or re.match(r".*:.*,.*", line) is None:
            continue
        kv = info.split()
        k = camel_to_snake_case(kv[0]).replace("p_", "")
        v = kv[1]
        try:
            v = int(kv[1])
        except:
            pass
        params[k] = v
    return PicInfo(**params)


def camel_to_snake_case(str):
    import re
    s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', str)
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).lower()

def parse_pic_info_file(pic_info_file):
    import re
    with open(pic_info_file, "r") as picinfo:
        data = picinfo.read()
    polylist_match = r"\s*polyList\s*:\s*\(.*?\),"
    num_polys = len(re.findall(polylist_match, data))
    no_polylist = re.subn(polylist_match, '', data, num_polys, re.DOTALL)[0]
    picinfo_match = r"\s*\(\(\s*PicInfo\s*new\s*:\s*\).*?\)"
    matches = re.findall(picinfo_match, no_polylist, re.DOTALL)
    return [parse_pic_info_entry(x) for x in matches]

