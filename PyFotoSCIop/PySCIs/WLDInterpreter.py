import os

procedure_keys = ['room', 'properties', 'atpinfo', 'objects', 'object', 'base', 'inventory', 'category', 'actions', 'special']

def parse_wld_data(input_data=None, parent=None):
    # Now process all the lines
    data_list = []
    line, wld = get_next_line(input_data)
    try:
        while 'end' not in line:
            if len(wld) == 0:
                break
            if len(line) > 0:
                if line[0] in procedure_keys and not (line[0] == 'object' and len(line) == 2) and parent != ['base', 'entry']:
                    wld, data = parse_wld_data(input_data=wld, parent=line)
                    data = [(''.join(line) if len(line) == 1 else ' '.join(line)), data]
                    # data.insert(0, (''.join(line) if len(line) == 1 else ' '.join(line)))
                    data_list.append(data)
                else:
                    if line in [['drop'], ['mana']]:
                        line += 'True'
                    data_list.append(line)
                if len(wld) == 0:
                    break
            line, wld = get_next_line(wld)
    except Exception as e:
        print (e)
    return wld, data_list



def get_next_line(wld):
    # Get next line
    # if len(wld) == 0:
    #     print('hu')
    try:
        line = wld.pop(0).strip()
    except Exception as e:
        print(e)
    # remove comment
    while True:
        if '#' in line:
            line = line[:line.index('#')]
        if len(line) <= 0 and len(wld) > 0:
            line = wld.pop(0).strip()
        else:
            break
    # split by whitespace, unless enclosed in quotes:
    line = line.replace('"', ' " ')
    line = line.split()
    while '"' in line:
        first = line.index('"')
        second = line.index('"', first + 1)
        line[first:second + 1] = [' '.join(line[first:second + 1]).replace('" ', '"').replace(' "', '"')]
    return line, wld

def process_wld_file(filename):

    with open(filename, 'r') as f:
        wld = f.readlines()
    if len(wld) == 0:
        print("WLD File is empty!")
    wld, parsed_wld_data = parse_wld_data(wld)
    return parsed_wld_data

def create_room(room_list, parnet=None):
    room_dict = {}
    for i, line in enumerate(room_list):
        try:
            if isinstance(line[0], str) and isinstance(line[1], list):
                if line[0] == 'atpinfo':
                    room_dict[line[0]] = line[1]
                else:
                    room_dict[line[0]] = create_room(line[1])
            else:
                if isinstance(line, str):
                    line = line.split()
                    room_dict[line[0]] = line[1:]
                elif isinstance(line, list):
                    if line[0] in room_dict.keys():
                        if not isinstance(room_dict[line[0]], list):
                            room_dict[line[0]] = [room_dict[line[0]]]
                        room_dict[line[0]] += line[1:]
                    else:
                        if len(line[1:]) == 1:
                            room_dict[line[0]] = line[1]
                        else:
                            room_dict[line[0]] = line[1:]
                else:
                    print("what's going on?")
        except Exception as e:
            print(e)
    return room_dict

def get_room(room_list):
    header = room_list[0]
    room_info = room_list[1]
    room_dict = {header.split()[0]: header.split()[1]}
    room_data = create_room(room_info)
    return {**room_dict, **room_data}


class Room:
    def __init__(self, room_info: dict=None):
        self.number = None
        self.picture = None
        self.properties = {}
        self.atpinfo = []
        self.objects = []
        if room_info:
            self.number = int(room_info['room'])
            if 'properties' in room_info.keys():
                self.properties = self.set_properties(room_info['properties'])
            if 'atpinfo' in room_info.keys():
                self.atpinfo = [ATP(*x) for x in room_info['atpinfo']]
            if 'objects' in room_info.keys():
                self.objects = self.set_objects(room_info['objects'])

    def set_properties(self, properties):
        props = {}
        exits = {'north':None, 'east':None, 'south':None, 'west':None}
        for x in properties.keys():
            if x in exits.keys():
                # TODO: sometimes an exit is recorded as a list of number. not usre what this means, but atm i only use the first number
                exits[x] = (int(properties[x]) if isinstance(properties[x], str) else int(properties[x][0]))
            else:
                props[x] = properties[x]
                if x == 'picture':
                    self.picture = properties[x]
        props['exits'] = exits
        return props

    def set_objects(self, objects):
        object_list = []
        for object_k, object_v in objects.items():
            obj_list = object_k.split()
            obj_name = obj_list[1]
            obj_class = obj_list[-1]
            coords = [0,0]
            loop = 0
            properties = None
            bases = []
            for obj_k, obj_v in object_v.items():
                if 'properties' in obj_k:
                    properties = obj_v
                    coords = [obj_v['x'], obj_v['y']]
                    if 'loop' in obj_v.keys():
                        loop = obj_v['loop']
                if 'base' in obj_k:
                    bases.append({obj_k:obj_v})
            obj = WorldObject(obj_name, obj_class, coords, loop, properties, bases)
            object_list.append(obj)
        return object_list

    def __repr__(self):
        return 'Room {}'.format(self.number)

class World:
    """
    representation of The Realm Online's .WLD file, for representing world structure.
    """
    def __init__(self, filename=None, rooms=None):
        self.name = filename[filename.rfind(os.sep)+1:]
        if rooms is not None:
            self.rooms = rooms
        if filename is not None:
            parsed_world = process_wld_file(filename)
            self.rooms = [Room(get_room(r)) for r in parsed_world]

    def __repr__(self):
        return self.name

class ATP:
    """
    contains id and coordinate of an ATP item for The Realm Online
    """

    def __init__(self, atp_num: int, x: int, y: int, z: int = 0):
        """
        :param id: integer corresponding to an atp id
        :param coords: tuple of two integers, corresponding to the location of this atp object within a room.
        """
        self.atp_num = int(atp_num)
        self.reference_atp_num = int((self.atp_num - 32768 if self.atp_num > 32768 else self.atp_num))
        self.mirror = (True if int(atp_num) > 32768 else False)
        self.node = None
        self.x = x
        self.y = y
        self.z = z

    def __repr__(self):
        return 'ATP: {}{}'.format((self.atp_num - 32768 if self.atp_num > 32768 else self.atp_num), ('M' if self.atp_num > 32768 else ''))

class WorldObject:
    """
    instance of a The Realm Online object in the WLD files.
    """

    def __init__(self, name, object_class, coords, loop=0, properites=None, bases=None):
        self.name = name
        self.object_class = object_class
        self.x = int(coords[0])
        self.y = int(coords[1])
        self.z = 0
        self.loop = int(loop)
        self.properties = properites
        self.bases = bases

    def __repr__(self):
        return "object {} of {}".format(self.name, self.object_class)




if __name__ == '__main__':
    import os
    f = 'C:\\Users\\caleb\\PycharmProjects\\World_Editor\\Resources\\World_Files\\Leineast.wld'
    world = World(f)
    pass

