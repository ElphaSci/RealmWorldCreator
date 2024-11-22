import textwrap

global StockObjList

StockObjList = []


class StockObject(object):
    _name = ""
    _pName = None
    pBaseView = None
    pAction = None

    @property
    def view(self):
        return self.pBaseView + self.pAction

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def pName(self):
        return self._pName if self._pName != None else self.name

    @pName.setter
    def pName(self, pName):
        self._pName = pName


def stk_to_obj(lines):
    for i, line_str in enumerate(lines):
        if isinstance(line_str, list):
            continue
        line = line_str.split()
        if 'instance' in line_str:
            old_lines = line
            try:
                names = [x for x in old_lines if 'instance' not in x and x != 'of']
                name, c_name = names[0], names[1]
                c_name = 'StockObject'
            except Exception as e:
                print(old_lines)
                raise (e)
            lines[i] = ''.join(['class ', name, '(', c_name, '):']) + '\n'
        elif line == ['('] or line == [')']:
            lines[i] = []
        elif 'method (doit aWhatObj' in line_str:
            lines[i] = '\tdef __init__(self):\n\t\tself.bases = []\n'
        elif 'properties' in line_str and 'name ""' in lines[i + 1]:
            lines[i] = []
            lines[i + 1] = '\tname = ""\n'
        elif '(aWhatObj' in line_str and ':' in lines[i + 1]:
            if 'addBase' in line_str:
                l = line_str.replace(')', '').split()[-1]
                lines[i] = '\t\tself.bases.append("{}")\n'.format(l)
            else:
                lines[i] = []
            t = i + 1
            while lines[t].strip() != ')':
                l = lines[t].replace(':', ' =').replace(',', '').strip()
                lines[t] = '\t\tself.' + l + '\n'
                t += 1
            lines[t] = []
        elif 'StockObjList add:' in line_str:
            obj = lines[i].replace(')', '').split()[-1]
            lines[i] = 'StockObjList.append(' + obj + '())\n'
        elif '(method (init)' in line_str:
            comment = '# This is where the .sc file creates the list, but we use a global reference'
            lines[i] = f'#StockObjList = [] {comment}\n'
            t = i + 1
            while lines[t].strip() != ')':
                l = 'StockObjList.append(' + lines[t].replace(')', '').split()[-1] + '())\n'
                lines[t] = l
                t += 1
        elif 'addBase' in line_str:
            l = line_str.replace(')', '').split()[-1]
            lines[i] = '\t\tself.bases.append("{}")\n'.format(l)
        elif 'aWhatObj' in line_str:
            lines[i] = []
        elif line_str.strip() != '':
            line_str = line_str.strip()
            if line_str[0] == '(' and line_str[-1] == ')':
                lines[i] = []
    lines = [x.replace(';', '#').replace('\t', '    ') for x in lines if
             x != [] and
             (x.strip()[0] != ';' if len(x.strip()) > 0 else True) and
             'doit' not in x and
             '_STATE' not in x and
             'Initter' not in x and
             'class StockObjList(StockObject):' not in x]
    return lines


def generate_python_stock_objects():
    from pathlib import Path

    obj_dir = Path("Resources/objects/sci")
    py_obj_dir = Path("Resources/objects/python")
    obj_dir.mkdir(mode=0o755, parents=True, exist_ok=True)
    py_obj_dir.mkdir(mode=0o755, parents=True, exist_ok=True)

    for sc_path in Path(obj_dir).glob("*.sc"):
        with open(sc_path, 'r') as ff:
            lines = ff.readlines()
        py_path = py_obj_dir.joinpath(f"{sc_path.stem}.py")
        with open(py_path, 'w') as ff:
            py_lines = stk_to_obj(lines)
            # TODO detect *.sc changes and re-generate
            py_lines.insert(0, textwrap.dedent(
                f'''
                # Generated Automatically from {sc_path}
                # Don't Manually edit this file
                
                from stock_objects import StockObjList,StockObject
                global StockObjList
                '''))
            ff.writelines(py_lines)
            ff.flush()


if __name__ == '__main__':
    generate_python_stock_objects()
