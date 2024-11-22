import os


class Exits(dict):
    """
    dictionary with keys "nortth", "south", "east", and "west", with integers values.
    The key represents the direction of the exit, while the integer corresponds to the room number the exit leads to.
    A value of None for a key represents a room where exit in that direction is not possible
    """

    def __init__(self, N=None, E=None, S=None, W=None):
        super(Exits, self).__init__({'north': N, 'east': E, 'south': S, 'west': W})


class ATP:
    """
    contains id and coordinate of an ATP item for The Realm Online
    """

    def __init__(self, id: int, coords: tuple, z: int = 0):
        """
        :param id: integer corresponding to an atp id
        :param coords: tuple of two integers, corresponding to the location of this atp object within a room.
        """
        self.id = id
        self.x = coords[0]
        self.y = coords[1]
        self.z = z


class WorldObject:
    """
    instance of a The Realm Online object in the WLD files.
    """

    def __init__(self, name, object_class, coords, z=0, loop=0, color=0, other=None):
        self.name = name
        self.object_class = object_class
        self.x = coords[0]
        self.y = coords[1]
        self.z = 0
        self.loop = loop
        self.color = color
        self.other = other


class Room:
    """
    representation of a single room inbstance for The Realm Online
    """

    def __init__(self, number: int, picture: int, name: str = None, exits: Exits = None, atpinfo: list = None,
                 objects: list = None, flags=None, template=None):
        """
        :param picture: the p56 file name used as the background for this room
        :param name: the name of the room to be shown in game
        :param exits: Exits subclass of dict, contains corresponding exit rooms for cardinal direction exits.
        :param atpinfo: list of ATP objects
        """
        self.template = template
        self.number = number
        self.picture = picture
        self.name = name
        self.exits = exits
        self.atpinfo = (atpinfo if atpinfo is not None else [])
        self.objects = (objects if objects is not None else [])
        self.flags = flags


def parseWLDfile(filename):
    """
    parses a .WLD file to create a list of room objects. The list of room objects is returned

    :param filename:
    :return: list of room objects
    """
    with open(filename, 'r') as f:
        lines = f.readlines()
    rooms = []
    while len(lines) > 0:
        line = lines.pop(0).split()
        if len(line) == 0:
            continue
        if 'end' in line:
            break
        level_1 = line[0]
        if level_1 == 'room':
            room_dict = {'number': None, 'picture': None, 'roomName': None, 'north': None, 'south': None, 'east': None,
                         'west': None, 'atpinfo': [], 'objects': []}
            room_dict['number'] = line[1]
            while True:
                line = lines.pop(0).split()
                while len(line) == 0:
                    line = lines.pop(0).split()
                if 'end' in line:
                    break
                level_2 = line[0]
                if level_2 == 'properties':
                    while True:
                        line = lines.pop(0).split()
                        while len(line) == 0:
                            line = lines.pop(0).split()
                        if 'end' in line:
                            break
                        room_dict[line[0]] = line[1]
                elif level_2 == 'atpinfo':
                    while True:
                        line = lines.pop(0).split()
                        while len(line) == 0:
                            line = lines.pop(0).split()
                        if 'end' in line:
                            break
                        if len(line) == 3:
                            atp = ATP(line[0], (line[1], line[2]))
                        elif len(line) == 4:
                            atp = ATP(line[0], (line[1], line[2]), line[3])
                        else:
                            print('not three or four lines?')
                            continue
                        room_dict['atpinfo'].append(atp)
                elif level_2 == 'objects':
                    while True:
                        line = lines.pop(0).split()
                        while len(line) == 0:
                            line = lines.pop(0).split()
                        if 'end' in line:
                            break
                        level_3 = line[0]
                        if level_3 == 'object':
                            object_name = line[1]
                            object_class = line[-1]
                            object_dict = {'x': None, 'y': None, 'z': None, 'loop': None, 'color': None}
                            while True:
                                line = lines.pop(0).split()
                                while len(line) == 0:
                                    line = lines.pop(0).split()
                                if 'end' in line:
                                    break
                                level_4 = line[0]
                                if level_4 == 'properties':
                                    while True:
                                        line = lines.pop(0).split()
                                        while len(line) == 0:
                                            line = lines.pop(0).split()
                                        if 'end' in line:
                                            break
                                        object_dict[line[0]] = line[1]
                                elif level_4 == 'base':
                                    base = line[1]
                                    object_dict[base] = {}
                                    while True:
                                        line = lines.pop(0).split()
                                        while len(line) == 0:
                                            line = lines.pop(0).split()
                                        if 'end' in line:
                                            break
                                        elif 'inventory' in line:
                                            inv = object_dict[base]['inventory'] = {}
                                            while True:
                                                line = lines.pop(0).split()
                                                while len(line) == 0:
                                                    line = lines.pop(0).split()
                                                if 'end' in line:
                                                    break
                                                elif 'category' in line:
                                                    categ = inv[' '.join(line[1:])] = {'object': []}
                                                    while True:
                                                        line = lines.pop(0).split()
                                                        while len(line) == 0:
                                                            line = lines.pop(0).split()
                                                        if 'end' in line:
                                                            break
                                                        elif 'object' in line:
                                                            categ['object'].append(line[1])
                                        else:
                                            object_dict[base][line.pop(0)] = ' '.join(line)
                            obj = WorldObject(object_name, object_class, (object_dict['x'], object_dict['y']),
                                              loop=object_dict['loop'], other=object_dict)
                            room_dict['objects'].append(obj)
            exits = Exits(N=room_dict['north'], S=room_dict['south'], E=room_dict['east'], W=room_dict['west'], )
            temp_room = Room(room_dict['number'], room_dict['picture'], room_dict['roomName'], exits,
                             room_dict['atpinfo'], room_dict['objects'])
            rooms.append(temp_room)
    return rooms


# def parseWLDFile(filename: str) -> list:
#     with open(filename, 'r') as f:
#         lines = f.readlines()
#     rooms = []
#     i = 0
#     while i < len(lines):
#         # print(i, len(lines))
#         line = lines[i]
#         if line[:4] == 'room':
#             room_number = int(line.split()[-1])
#             picture = None
#             exits = Exits()
#             room_name = None
#             atpinfo = []
#             objects = []
#             while 'end' not in line:
#                 i += 1
#                 line = lines[i]
#                 if 'properties' in line:
#                     i += 1
#                     line = lines[i]
#                     while 'end' not in line:
#                         # print('props')
#                         prop = line.split()
#                         if prop[0] == 'picture':
#                             picture = int(prop[1])
#                         elif prop[0] in ['north', 'south', 'east', 'west']:
#                             exits[prop[0]] = int(prop[1])
#                         elif prop[0] == 'name':
#                             room_name = line[line.find('"'):]
#                         i += 1
#                         line = lines[i]
#                     i += 1
#                     line = lines[i]
#                 if 'atpinfo' in line:
#                     i += 1
#                     line = lines[i]
#                     while 'end' not in line:
#                         # print('atpinfo')
#                         atp = line.split()
#                         atp = ATP(atp[0], (atp[1], atp[2]))
#                         atpinfo.append(atp)
#                         i += 1
#                         line = lines[i]
#                     i += 1
#                     line = lines[i]
#                 if 'objects' in line:
#                     i += 1
#                     line = lines[i]
#                     while 'end' not in line:
#                         if 'object' in line:
#                             obj_info = line.split()
#                             obj_name = obj_info[1]
#                             obj_class = obj_info[-1]
#                             i += 1
#                             line = lines[i]
#                             while 'end' not in line:
#                                 if 'properties' in line:
#                                     i += 1
#                                     line = lines[i]
#                                     while 'end' not in line:
#                                         line_list = line.split()
#                                         if line_list[0] == 'x':
#                                             obj_x = line_list[1]
#                                         elif line_list[0] == 'y':
#                                             obj_y = line_list[1]
#                                         elif line_list[0] == 'loop':
#                                             obj_loop = line_list[1]
#                                         i += 1
#                                         line = lines[i]
#                                     i += 1
#                                     line = lines[i]
#                             room_obj = WorldObject(obj_name, obj_class, (obj_x, obj_y), obj_loop)
#                             objects.append(room_obj)
#                             i += 1
#                             line = lines[i]
#                     i += 1
#                     line = lines[i]
#
#             i += 1
#             room = Room(room_number, room_name, exits, atpinfo, objects)
#             rooms.append(room)
#     return rooms


class WLD:
    """
    representation of The Realm Online's .WLD file, for representing world structure.
    """

    def __init__(self, filename=None, rooms=None):
        self.name = filename[filename.rfind(os.sep):]
        if rooms is not None:
            self.rooms = rooms
        if filename is not None:
            self.rooms = parseWLDfile(filename)


if __name__ == '__main__':
    # print('test')
    world = WLD('./WLD_files/ACHREN01.WLD')
    # print(len(world.rooms))
    print([r.picture for r in world])
