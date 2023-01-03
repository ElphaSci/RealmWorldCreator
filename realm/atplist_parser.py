from typing import TextIO


def skip_until_eol(text: TextIO):
    while (text.readable()):
        text.readline()
        return

def next_valid_char(text: TextIO):
    while text.readable():
        next = text.read(1)
        if (next == ''):
            return ''
        if next == ';':
            skip_until_eol(text)
        # elif len(next.strip()) == 0:
        #     continue
        else:
            return next


def read_closure(text: TextIO):
    contents = []
    before_cont = ""
    after_cont = ""
    while (text.readable()):
        next = text.read(1)
        if (next == "("):
            contents.append(read_closure())


class ATPList:
    def __init__(self, path: str):
        self._raw_text: str
        self._processed_text: str
        self.parse(path)

    def parse(self, path):
        lines: list[str]
        with open(path, "r") as atplist:
            self.tokens = self.process(atplist)

    def process(self, text: TextIO):
        contents = []
        cur_str = ""
        while text.readable():
            next = next_valid_char(text)
            if (next == ''):
                break
            if next == '(':
                if len(cur_str.strip()) > 0:
                    contents += [cur_str]
                    cur_str = ""
                tok = self.process(text)
                if len(tok) > 0:
                    contents += [tok]
                pass
            elif next == ')':
                strip = cur_str.strip()
                temp = []
                if (len(strip) > 0):
                    temp = [cur_str]
                if len(contents) > 0:
                    temp += [contents]
                return temp
            else:
                cur_str += next
        return contents


if __name__ == '__main__':
    atplist = ATPList("/Resources/objects/ATPLIST.SC")