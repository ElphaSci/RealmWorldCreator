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
                c_name = 'object'
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
            lines[i] = 'StockObjList = []\n'
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
             x != [] and 'doit' not in x and '_STATE' not in x and 'Initter' not in x and 'class StockObjList(object):' not in x]
    return lines


'''
#files = [stkobj_files]
for f in [x.lower() for x in files]:
       with open(f, 'r') as ff:
           lines = ff.readlines()
       with open(f.replace('.sc', '.py').lower(), 'w') as ff:
           py_lines = stk_to_obj(lines)
           print(len(py_lines))
           if f == 'stkobj0.sc':
               py_lines.insert(0, 'global StockObjList\n\n')
           else:
               num = int(f.replace('stkobj', '').replace('.sc', ''))
               py_lines.insert(0, 'from Resources.stock_objects.stkobj{} import StockObjList\n\n'.format(num-1))
           if f == 'stkobj7.sc':
               py_lines.append('\nfor obj in StockObjList:\n\tobj.view = obj.pBaseView + obj.pAction\nstkObjDict = {obj.name:obj for obj in StockObjList}')
           ff.writelines(py_lines)
'''
