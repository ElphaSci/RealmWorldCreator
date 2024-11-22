import os

procedure_keys = ['room', 'properties', 'atpinfo', 'objects', 'object', 'base', 'inventory', 'category',
                  'actions']  # , 'special']


def parse_wld_data(input_data=None, parent=None):
    # Now process all the lines
    data_list = []
    line, wld = get_next_line(input_data)
    try:
        while 'end' not in line:
            if len(wld) == 0:
                break
            if len(line) > 0:
                if line[0] in procedure_keys and not (line[0] == 'object' and len(line) == 2) and parent != ['base',
                                                                                                             'entry']:
                    wld, data = parse_wld_data(input_data=wld, parent=line)
                    data = [(''.join(line) if len(line) == 1 else ' '.join(line)), data]
                    # data.insert(0, (''.join(line) if len(line) == 1 else ' '.join(line)))
                    data_list.append(data)
                else:
                    if line in [['drop'], ['mana'], ['special']]:
                        line += ['True']
                    data_list.append(line)
                if len(wld) == 0:
                    break
            line, wld = get_next_line(wld)
    except Exception as e:
        print(e)
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
        '''
        This is hack to account for a malformed file that seemingly Realm is fine with, so I have
        to handle it to :(
        
        It was in ARIMATHI.WLD and it had the following text:
                title	"the sorcery shopkeeper
                    
        It's missing the second " So below we will just append if we ever see this happen 
        '''
        try:
            second = line.index('"', first + 1)
        except ValueError:
            line.append('"')
            second = line.index('"', first + 1)
        line[first:second + 1] = [' '.join(line[first:second + 1]).replace('" ', '"').replace(' "', '"')]
    return line, wld

def process_wld_file(filename):
    with open(filename, 'r', encoding='utf8') as f:
        wld = f.readlines()
    if len(wld) == 0:
        print("WLD File is empty!")
    wld, parsed_wld_data = parse_wld_data(wld)
    return parsed_wld_data


def create_room(room_list, parent=None):
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
    def __init__(self, room_info: dict = None):
        self.number = None
        self.picture = None
        self.properties = {}
        self.atpinfo = []
        self.objects = []
        self.active_views = []
        self.view_from_image = {}
        self.active_background = None
        if room_info:
            self.number = int(room_info['room'])
            if 'properties' in room_info.keys():
                self.properties = self.set_properties(room_info['properties'])
            if 'atpinfo' in room_info.keys():
                self.atpinfo = [ATP(*x) for x in room_info['atpinfo']]
            if 'objects' in room_info.keys():
                self.objects = self.set_objects(room_info['objects'])

    @property
    def realm_representation(self):
        data = []
        data.append('room {}'.format(self.number))
        data.append('\tproperties')
        for k, v in self.properties.items():
            if k == 'exits':
                for direction, exit_num in v.items():
                    if exit_num is None:
                        continue
                    if isinstance(exit_num, list):
                        exit_num = ' '.join(exit_num)
                    data.append('\t\t{} {}'.format(direction, exit_num))
            else:
                data.append('\t\t{} {}'.format(k, v))
        data.append('\tend')
        atp_info = ['\tatpinfo']
        objects = ['\tobjects']
        object_class_count = {}
        if len(self.active_views) == 0:
            atps_objs = self.atpinfo + self.objects
        else:
            atps_objs = self.active_views
        for atp_obj in atps_objs:
            if isinstance(atp_obj, ATP):
                atp_realm_representation = '\t\t' + atp_obj.realm_representation
                atp_info.append(atp_realm_representation)
            if isinstance(atp_obj, WorldObject):
                if atp_obj.object_class not in object_class_count.keys():
                    object_class_count[atp_obj.object_class] = -1
                object_class_count[atp_obj.object_class] += 1
                number = object_class_count[atp_obj.object_class]
                name = atp_obj.object_class[0].lower() + atp_obj.object_class[1:]
                object_header = 'object {}{}-{} of {}'.format(name, self.number, number, atp_obj.object_class)
                obj_realm_representation = atp_obj.realm_representation
                obj_realm_representation = ['\t\t\t{}'.format(x) for x in obj_realm_representation]
                objects.append('\t\t{}'.format(object_header))
                objects += obj_realm_representation
                objects.append('\t\tend')
        if len(atp_info) == 1:
            atp_info = []
        else:
            atp_info.append('\tend')
        if len(objects) == 1:
            objects = []
        else:
            objects.append('\tend')
        data += atp_info
        data += objects
        data.append('end')
        data = ['{}\n'.format(x) for x in data]
        return data

    def reset(self):
        for im_id in self.active_views[:]:
            self.remove(im_id)
        for atp_obj in self.atpinfo + self.objects:
            atp_obj.reset()
        self.active_background = None

    def remove(self, instance_or_id):
        if isinstance(instance_or_id, int):
            id = instance_or_id
            inst = self.view_from_image[id]
        else:
            inst = instance_or_id
            id = inst.im_id
        self.active_views.remove(inst)
        del self.view_from_image[id]

    def set_properties(self, properties):
        props = {}
        exits = {'north': None, 'east': None, 'south': None, 'west': None}
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
            coords = [0, 0]
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
                    bases.append({obj_k: obj_v})
            obj = WorldObject(obj_class, coords, obj_name, loop, properties, bases)
            object_list.append(obj)
        return object_list

    def __repr__(self):
        return 'Room {}'.format(self.number)


class World:
    """
    representation of The Realm Online's .WLD file, for representing world structure.
    """

    def __init__(self, filename=None, rooms=None):
        self.name = filename[filename.rfind(os.sep) + 1:]
        if rooms is not None:
            self.rooms = rooms
        if filename is not None:
            parsed_world = process_wld_file(filename)
            self.rooms = [Room(get_room(r)) for r in parsed_world]

    @property
    def realm_representation(self):
        data = []
        for room in self.rooms:
            data += room.realm_representation
        return data

    def __repr__(self):
        return self.name


class ATP:
    """
    contains id and coordinate of an ATP item for The Realm Online
    """

    def __init__(self, atp_num: int, x: int = None, y: int = None, z: int = 0):
        """
        :param id: integer corresponding to an atp id
        :param coords: tuple of two integers, corresponding to the location of this atp object within a room.
        """
        self.__x, self.__y, self.__z, self.__mirror = None, None, None, None
        self.initial_coords = [None, None, None]
        self.im_id = None
        self.v56 = None
        self.images = {'original_image': None, 'scaled_image': None, 'tk_image': None}
        self.canvas_coords = {'x': None, 'y': None}
        self.atp_num = int(atp_num)
        self.reference_atp_num = int((self.atp_num - 32768 if self.atp_num > 32768 else self.atp_num))
        self.mirror = (True if int(atp_num) > 32768 else False)
        self.node = None
        self.x = (int(x) if x else None)
        self.y = (int(y) if y else None)
        self.z = (int(z) if z else 0)

    @property
    def mirror(self):
        return self.__mirror

    @mirror.setter
    def mirror(self, val):
        if val == self.__mirror or val not in [True, False]:
            return
        self.__mirror = val
        if val:
            # If it's mirrored, the atp_num should be > 32768
            if self.atp_num < 32768:
                self.atp_num += 32768
        else:
            # If it's not mirrored, the atp_num should be < 32768
            if self.atp_num > 32768:
                self.atp_num -= 32768

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    @property
    def z(self):
        return self.__z

    @x.setter
    def x(self, val):
        if self.initial_coords[0] is None:
            self.initial_coords[0] = (self.x if self.x is not None else val)
        self.__x = val

    @y.setter
    def y(self, val):
        if self.initial_coords[1] is None:
            self.initial_coords[1] = (self.y if self.y is not None else val)
        self.__y = val

    @z.setter
    def z(self, val):
        if self.initial_coords[2] is None:
            self.initial_coords[2] = (self.z if self.z is not None else val)
        self.__z = val

    @property
    def realm_representation(self):
        z = (self.z if self.z not in ['', None, 0] else '')
        repr = '{} {} {} {}'.format(self.atp_num, self.x, self.y, z)
        return repr

    def reset(self):
        self.x = self.initial_coords[0]
        self.y = self.initial_coords[1]
        self.z = self.initial_coords[2]

    def __repr__(self):
        return 'ATP: {}{}'.format((self.atp_num - 32768 if self.atp_num > 32768 else self.atp_num),
                                  ('M' if self.atp_num > 32768 else ''))


class WorldObject:
    """
    instance of a The Realm Online object in the WLD files.
    """

    def __init__(self, object_class, coords=None, name=None, loop=0, properites=None, bases=[]):
        self.name = name
        self.object_class = object_class
        self.__x = (None if not coords else int(coords[0]))
        self.__y = (None if not coords else int(coords[1]))
        self.__z = 0
        self.__loop = 0
        self.properties = properites
        self.bases = bases
        self.im_id = None
        self.v56 = None
        self.images = {'original_image': None, 'scaled_image': None, 'tk_image': None}
        self.canvas_coords = {'x': None, 'y': None}
        self.initial_coords = [None, None, None]
        # Set loop
        self.loop = loop

    @property
    def loop(self):
        return self.__loop

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    @property
    def z(self):
        return self.__z

    @loop.setter
    def loop(self, val):
        if self.properties is None:
            self.properties = {}
        if 'loop' not in self.properties.keys():
            self.properties['loop'] = None
        self.properties['loop'] = val
        self.__loop = val

    @x.setter
    def x(self, val):
        if self.initial_coords[0] is None:
            self.initial_coords[0] = (self.x if self.x is not None else val)
        if self.properties is None:
            self.properties = {}
        if 'x' not in self.properties.keys():
            self.properties['x'] = None
        self.properties['x'] = val
        self.__x = val

    @y.setter
    def y(self, val):
        if self.initial_coords[1] is None:
            self.initial_coords[1] = (self.y if self.y is not None else val)
        if self.properties is None:
            self.properties = {}
        if 'y' not in self.properties.keys():
            self.properties['y'] = None
        self.properties['y'] = val
        self.__y = val

    @z.setter
    def z(self, val):
        if self.initial_coords[2] is None:
            self.initial_coords[2] = (self.z if self.z is not None else val)
        if self.properties is None:
            self.properties = {}
        if 'z' not in self.properties.keys():
            self.properties['z'] = None
        self.properties['z'] = val
        self.__z = val

    @property
    def realm_representation(self):
        data = []
        data.append('properties')
        for k, v in self.properties.items():
            if k in ['x', 'y', 'loop']:
                new_v = getattr(self, k)
            elif k in ['mana', 'drop', 'special']:
                new_v = ''
            elif k in ['z', 'linkTo']:
                continue
            else:
                new_v = v
            datum = '\t{} {}'.format(k, new_v)
            data.append(datum)
        data.append('end')
        for base in self.bases:
            data.append(list(base.keys())[0])
            for k, v in list(base.values())[0].items():
                if isinstance(v, list):
                    if k == 'head':
                        v = ' '.join(v)
                        data.append('\t{} {}'.format(k, v))
                    else:
                        for vv in v:
                            datum = '\t{} {}'.format(k, vv)
                            data.append(datum)
                elif isinstance(v, dict):
                    data.append('\t{}'.format(k))
                    for kk, vv in v.items():
                        if isinstance(vv, dict):
                            data.append('\t\t{}'.format(kk))
                            for kkk, vvv in vv.items():
                                if isinstance(vvv, list):
                                    for vvvv in vvv:
                                        data.append('\t\t\t{} {}'.format(kkk, vvvv))
                                else:
                                    print('hmm2')
                            data.append('\t\tend')
                        else:
                            print('hmm')
                    data.append('\tend')
                else:
                    # TODO: handle linking to owner
                    if k == 'owner':
                        continue
                    datum = '\t{} {}'.format(k, v)

                    data.append(datum)
            data.append('end')
        return data

    def reset(self):
        self.x = self.initial_coords[0]
        self.y = self.initial_coords[1]
        self.z = self.initial_coords[2]

    def __repr__(self):
        return "object {} of {}".format(self.name, self.object_class)
