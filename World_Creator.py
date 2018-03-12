import os
import tkinter as tk
from tkinter import filedialog, messagebox

from PIL import Image, ImageTk, ImageOps

from PyFotoSCIop.source.p56files import p56file32
from PyFotoSCIop.source.v56files import V56file
from Resources.stock_objects.stkobj7 import stkObjDict
from atp_info import ATP_CATEGORIES, ATP_BY_PIC
from p56_info import PIC_INFO
from PyFotoSCIop.PySCIs.WLDInterpreter import ATP, WorldObject, Room
import PyFotoSCIop.PySCIs.WLDInterpreter as WldInterp


def scale_image(pil_image: Image, y_depth: int, p56_info, race='default'):
    """
    Scales pil_im to the appropriate size, using the scaling parameters from pic_info, and given the y_depth

    :param pil_image: PIL Image to be scaled
    :param y_depth: new y-depth to scale pil_image to
    :param p56_info: information regarding the scaling with respect to the current background pic

    returns a scaled ImageTk, a scaling factor, and a scaled PIL Image
    """
    # Handle 3 cases of scaling; there is a back and front limit for scaling, based on the p56 background
    if p56_info.back_y < y_depth < p56_info.front_y:
        slope = p56_info.slope()
        const = p56_info.scale_constant()
        new_scale = slope * y_depth + const
        race_adjustment = {'default': 100, 'human': 100, 'giant': 110, 'elf': 90}
        scale_factor = (new_scale * race_adjustment[race]) / 100
    elif y_depth >= p56_info.front_y:
        scale_factor = p56_info.frontPercent()
    else:
        scale_factor = p56_info.backPercent()
    # Scale the image based on the calculated scale_factor
    new_shape = (int(pil_image.width * scale_factor), int(pil_image.height * scale_factor))
    scaled_pil_im = pil_image.resize(new_shape)
    tk_im = ImageTk.PhotoImage(scaled_pil_im)
    return tk_im, scale_factor, scaled_pil_im


class MapButton(tk.Button):
    def __init__(self, root, room_id, *args, **kwargs):
        """
        tkinter Button subclass that stores the id of the Realm room that it corresponds too

        :param root: parent, tkinter widget
        :param room_id: int, number of room for this map button
        :param args:
        :param kwargs:
        """
        tk.Button.__init__(self, root, *args, **kwargs)
        self.room_id = room_id


class NestedOptionMenu(tk.Frame):
    def __init__(self, app, parent, top_info, callback=None):
        tk.Frame.__init__(self, parent)
        self.callback = callback
        self.app = app
        self.top_info = {}
        if isinstance(top_info, list):
            self.convert_to_dict(top_info)
        else:
            self.top_info = top_info
        self.the_value = tk.StringVar()
        self.menubutton = tk.Menubutton(self, textvariable=self.the_value, indicatoron=True)
        self.top_menu = tk.Menu(self.menubutton, tearoff=False)
        self.menubutton.configure(menu=self.top_menu)
        self.the_value.set(self.set_the_value(self.top_info))
        self.option_count = 0
        self.create_menu(self.top_info, self.top_menu, self.the_value)
        self.top_menu.entryconfigure(self.option_count // 3, columnbreak=1)
        self.top_menu.entryconfigure(self.option_count * 2 // 3, columnbreak=2)
        self.menubutton.pack()

    def create_menu(self, top_info, top_menu, value_var, parent=''):
        if isinstance(top_info, dict):
            alphabetical_info = [[k, v] for k,v in top_info.items()]
            alphabetical_info.sort(key=lambda x: x[0])
            for key, value in alphabetical_info:
                menu = tk.Menu(top_menu)
                if value:
                    top_menu.add_cascade(label=key, menu=menu)
                    self.create_menu(value, menu, value_var, parent=key)
                else:
                    top_menu.add_radiobutton(label=key, variable=value_var, value=key, command=self.callback)
                    self.option_count += 1
            return
        else:
            top_info.sort()
            for item in top_info:
                if parent != '':
                    label_value = parent + ':' + item
                else:
                    label_value = item
                top_menu.add_radiobutton(label=item, variable=value_var, value=label_value,
                                         command=self.app.set_category_atps)
                self.option_count += 1
            return

    def set_the_value(self, top_info):
        if isinstance(top_info, dict):
            first_key = list(top_info.keys())[0]
            first_value = top_info[first_key]
            if first_value is None:
                return first_key
            return first_key + ':' + self.set_the_value(first_value)
        elif isinstance(top_info, str):
            return top_info
        elif isinstance(top_info, list):
            return top_info[0]

    def get(self):
        return self.the_value.get()

    def convert_to_dict(self, top_info):
        for item in top_info:
            if ':' in item:
                item_list = item.split(':')
                key = item_list[0]
                value = item_list[1:]
                if len(value) > 1:
                    new_dict = {key: {}}
                    self.top_info = {**self.top_info, **new_dict}
                    self.convert_to_dict(':'.join(value))
                else:
                    if key in self.top_info.keys():
                        self.top_info[key].append(value[0])
                    else:
                        self.top_info[key] = [value[0]]
            else:
                self.top_info[item] = None


class WorldCreator(tk.Tk):
    def __init__(self, title='World Creator', atp_categories=None, pic_info=None, object_info=None, atps_by_pic=ATP_BY_PIC):
        tk.Tk.__init__(self)
        # Store the ATPs, by category, and by pic:
        self.atps = {'category': {}, 'atp': {}, 'view': {}}
        self.set_atps(atp_categories)
        self.atps_by_pic = atps_by_pic
        # Store the p56 information
        self.pic_atps = {}
        self.pics = pic_info
        # Store the object Info
        self.stk_objs = object_info
        self.obj_bases = self.get_obj_bases()
        # dictionary to hold all non-top level widgets; keys are the parent widgets
        self.widgets = {}
        # Storage for access to media files
        self.media = {'v56': {}, 'p56': {}, 'wld': {}, 'zon': {}, 'PATH': []}
        self.background = None
        # Build default media paths
        default_56_path = os.path.join('Resources', '56_Files')
        default_wld_path = os.path.join('Resources', 'World_Files')
        self.add_media(default_56_path)
        self.add_media(default_wld_path)
        self.room_directory = self.build_room_directory()
        # Store WLD, by Zone
        self.zones = self.set_worlds_by_zone()
        # Keep track of the object being dragged
        self.moving_view = None
        # Store dict of rooms, active Room, and world
        self.rooms = {}
        self.active_room = None
        self.world = None
        self.save_file = None
        # Build Category Canvas and children
        # Set the window title
        self.wm_title(title)
        # Create the top level menu bar
        self.menu = tk.Menu()
        self.config(menu=self.menu)
        self.build_menu_bar()
        # Create the left-most canvas, for category and atp information
        self.category_canvas = tk.Canvas(self)
        self.category_canvas.grid(row=0, column=0, rowspan=20, sticky=(tk.W, tk.W, tk.S, tk.N))
        # builds header, option menu, and listbox for category ATPs
        self.build_category_canvas(list(atp_categories.keys()))
        # Create the center canvas, which holds the v56 and p56 images.
        self.room_canvas = tk.Canvas(self, width=640, height=320)
        self.room_canvas.grid(row=0, column=1, columnspan=2, sticky=(tk.N, tk.S, tk.W, tk.E))
        # Allow for draggable children of this canvas
        self.set_canvas_bindings()
        # Create the map canvas:
        self.map_canvas = tk.Canvas()
        self.map_canvas.grid(row=2, column=1, columnspan=2, sticky=(tk.E, tk.W, tk.S, tk.N))
        # Create WLD column Canvas
        self.wld_canvas = tk.Canvas()
        self.wld_canvas.grid(row=0, column=3, rowspan=20, sticky=(tk.N, tk.S, tk.E, tk.W))
        # Setup the wld listbox
        self.build_wld_canvas(list(self.zones.keys()))
        # Create Toplevel widget for handling popup widgets
        self.top = None
        # Initialize listboxes
        self.set_category_atps()
        self.set_wld_listbox()
        # Set False to disable popup errors - convenient for debugging
        self._popup_error = True
        # Store initial polygon state
        self.polygon_state = 'normal'

        self.mainloop()

    def errorbox(self, error_message=''):
        if self._popup_error:
            messagebox.showerror('Error', error_message)

    def get_obj_bases(self):
        objs_by_base = {'Misc': []}
        for obj_class, obj in self.stk_objs.items():
            if len(obj.bases) == 0:
                objs_by_base['Misc'].append(obj)
            for base in obj.bases:
                if 'escribed' in base and len(obj.bases) > 1:
                    continue
                elif base not in objs_by_base.keys():
                    objs_by_base[base] = [obj]
                else:
                    objs_by_base[base].append(obj)
        return objs_by_base

    def set_atps(self, atps_by_category):
        self.atps['category'] = atps_by_category
        self.atps['atp'] = {}
        self.atps['view'] = {}
        for k, category in atps_by_category.items():
            for atp_num, atp in category.items():
                self.atps['atp'][atp.number] = atp
                self.atps['view'][atp.view] = atp

    def set_worlds_by_zone(self):
        worlds_by_zone = {'Misc': []}
        for zon, path in self.media['zon'].items():
            with open(path, 'r', encoding='ISO-8859-1') as f:
                lines = f.readlines()
            lines = [x for x in lines if 'worldFile' in x or 'title' in x]
            temp = {'title': '', 'worlds': []}
            for line in lines:
                if 'title' in line:
                    line = line[line.find('"') + 1:line.rfind('"')].replace(':', '')
                    temp['title'] = line
                elif '.wld' in line.lower():
                    wld_file = line[line.find('"') + 1:line.rfind('"')].split('/')[-1].strip()
                    temp['worlds'].append(wld_file)
            if len(temp['worlds']) > 0:
                if temp['title'] == '':
                    if 'Misc' not in worlds_by_zone.keys():
                        worlds_by_zone['Misc'] += [x for x in temp['worlds'] if x not in worlds_by_zone['Misc']]
                elif temp['title'] not in worlds_by_zone.keys():
                    worlds_by_zone[temp['title']] = temp['worlds']
                else:
                    worlds_by_zone[temp['title']] += [x for x in temp['worlds'] if
                                                      x not in worlds_by_zone[temp['title']]]
        worlds_with_zone = []
        for wld_list in worlds_by_zone.values():
            for wld in wld_list:
                worlds_with_zone.append(wld.lower())
        for wld in self.media['wld'].keys():
            if wld.lower() not in worlds_with_zone:
                if 'Misc' not in worlds_by_zone.keys():
                    worlds_by_zone['Misc'] = []
                worlds_by_zone['Misc'].append(wld)
        return worlds_by_zone

    def build_room_directory(self):
        room_directory = {}
        for wld, path in self.media['wld'].items():
            with open(path, 'r') as f:
                try:
                    data = f.readlines()
                except UnicodeDecodeError as e:
                    print(path)
            for line in data:
                lower_line = line.lower()
                if 'room\t' in lower_line or 'room ' in lower_line:
                    num = line.split()[-1]
                    if num.strip().isnumeric():
                        room_directory[num] = wld
        return room_directory


    def image_under_cursor(self, event):
        canv_x = self.room_canvas.canvasx(event.x)
        canv_y = self.room_canvas.canvasy(event.y)
        ids_to_check = list(self.room_canvas.find_overlapping(canv_x, canv_y, canv_x + 1, canv_y + 1))
        ids_to_check.sort(reverse=True)
        im_id = ids_to_check[0]
        if im_id == self.background['im_id']:
            ids_to_check.pop(0)
            try:
                im_id = ids_to_check[0]
            except IndexError:
                return
        while im_id is not None and im_id != self.background['im_id']:
            pil_im = self.active_room.view_from_image[im_id].images['scaled_image']
            if pil_im is None:
                pil_im = self.active_room.view_from_image[im_id].images['original_image']
            # bounding box in relation to canvas NE
            bbox = self.room_canvas.bbox(im_id)
            # pixel_xy in image, of picel under cursor
            pixel_x = int(event.x - bbox[0])
            pixel_y = int(event.y - bbox[1])
            pixel_outside_image = pixel_x < 0 or pixel_x > pil_im.width - 1 or pixel_y < 0 or pixel_y > pil_im.height - 1
            if not pixel_outside_image:
                pixel = pil_im.getpixel((pixel_x, pixel_y))[-1]
                transparent_pixel = pixel == 0
                if not transparent_pixel:
                    return im_id
            self.moving_view = None
            ids_to_check.pop(ids_to_check.index(im_id))
            if len(ids_to_check) > 0:
                im_id = ids_to_check[0]
            else:
                return
            if im_id == self.background['im_id']:
                return

    def drag_start(self, event):
        im_id = self.image_under_cursor(event)
        if im_id is None:
            self.moving_view = None
            print('no view under cursor')
            return
        self.moving_view = im_id
        self.active_room.view_from_image[im_id].canvas_coords['x'] = event.x
        self.active_room.view_from_image[im_id].canvas_coords['y'] = event.y
        pass

    def move_to(self, im_id, x, y=0, z=None, scale=True):
        atp_obj = self.active_room.view_from_image[im_id]
        cur_x = atp_obj.canvas_coords['x']
        x_move = x - cur_x
        cur_y = atp_obj.canvas_coords['y']
        y_move = y - cur_y
        if z is None:
            if scale:
                # Handle scalling when moving views into the background/foreground
                y_depth = atp_obj.y + y_move
                original_pil_im = atp_obj.images['original_image']
                tk_im, scale_factor, scaled_pil_im = scale_image(original_pil_im, y_depth, self.background['info'])
                self.room_canvas.itemconfig(im_id, image=tk_im)
                atp_obj.images['tk_image'] = tk_im
                atp_obj.images['scaled_image'] = scaled_pil_im
            # Move Item and Update value to represent new location:
            self.room_canvas.move(im_id, x_move, y_move)
            atp_obj.canvas_coords['x'] = x
            atp_obj.canvas_coords['y'] = y
            atp_obj.y += y_move
            atp_obj.x += x_move
            # Handle moving image on top of other images dynamically, when changing y_depth
            depth_sorted_ims = [[view.y, view] for view in self.active_room.active_views]
            depth_sorted_ims.sort(key=lambda x: x[0])
            for im in depth_sorted_ims:
                self.room_canvas.lift(im[1].im_id)
        elif z:
            cur_y = atp_obj.canvas_coords['y']
            y_move = z - cur_y
            # update to reflect new location
            atp_obj.canvas_coords['x'] = x
            atp_obj.canvas_coords['y'] = z
            atp_obj.z -= y_move
            atp_obj.x += x_move
            self.room_canvas.move(im_id, x_move, y_move)

    def drag_motion_button1(self, event, scale=True):
        if self.moving_view is None:
            return
        im_id = self.moving_view
        if 'scalable' not in self.room_canvas.gettags(im_id):
            scale = False
        else:
            scale = True
        self.move_to(im_id, event.x, event.y, scale=scale)

    def drag_motion_button3(self, event, scale=True):
        if self.moving_view is None:
            return
        im_id = self.moving_view
        if 'object' in self.room_canvas.gettags(im_id):
            return
        scale = False
        self.move_to(im_id, event.x, y=0, z=event.y, scale=scale)

    def view_popup_menu(self, event):
        im_id = self.image_under_cursor(event)
        image_tags = self.room_canvas.gettags(im_id)
        view_popup = tk.Menu(self, tearoff=0)
        view_popup.add_command(label='Cell Properties', command=lambda: self.draw_properties_box(im_id))
        view_popup.add_command(label='Move To', command=lambda: self.xyz_entry_popup(im_id))
        if 'atp' in image_tags:
            view_popup.add_command(label='Mirror', command=lambda: self.mirror_image(im_id))
        elif 'object' in image_tags:
            view_popup.add_command(label='Next Loop', command=lambda: self.next_loop(im_id))
        view_popup.add_command(label='Delete', command=lambda: self.delete_from_room(im_id))
        # try:
        view_popup.tk_popup(event.x_root, event.y_root, 0)
        # finally:
        #     view_popup.grab_release()

    def next_loop(self, im_id):
        v56 = self.active_room.view_from_image[im_id].v56
        obj = self.active_room.view_from_image[im_id]
        x = obj.x
        y = obj.y
        z = obj.z
        max_loop = len(v56._loops) - 1
        cur_loop = obj.loop
        if cur_loop == max_loop:
            cur_loop = 0
        else:
            cur_loop += 1
        obj.loop = cur_loop
        obj.x = x
        obj.y = y
        obj.z = z
        self.draw_object(obj)
        self.delete_from_room(im_id)

    def mirror_image(self, image_id):
        atp = self.active_room.view_from_image[image_id]
        original_pil = atp.images['original_image']
        mirror_pil = ImageOps.mirror(original_pil)
        atp.images['original_image'] = mirror_pil
        if atp.images['scaled_image']:
            scaled_pil = atp.images['scaled_image']
            mirror_scale = ImageOps.mirror(scaled_pil)
            tk_im = ImageTk.PhotoImage(mirror_scale)
            self.room_canvas.itemconfig(image_id, image=tk_im)
            atp.images['scaled_image'] = mirror_scale
            atp.images['tk_image'] = tk_im
        else:
            tk_im = ImageTk.PhotoImage(mirror_pil)
            self.room_canvas.itemconfig(image_id, image=tk_im)
            atp.images['tk_image'] = tk_im
        # update the mirror state of the active view and object
        atp.mirror = not atp.mirror

    def delete_from_room(self, image_id):
        self.room_canvas.delete(image_id)
        # This is a custom remove method that handles deleting the
        self.active_room.remove(image_id)

    def xyz_entry_popup(self, im_id):
        image = self.active_room.view_from_image[im_id]
        cur_x = image.x
        cur_y = image.y
        cur_z = image.y
        self.top = tk.Toplevel()
        tk.Label(self.top, text='X : ').grid(row=0, column=0)
        x_entry = tk.Entry(self.top, justify=tk.RIGHT)
        x_entry.grid(row=0, column=1, columnspan=2)
        x_entry.insert(0, str(cur_x))
        tk.Label(self.top, text='Y : ').grid(row=1, column=0)
        y_entry = tk.Entry(self.top, justify=tk.RIGHT)
        y_entry.grid(row=1, column=1, columnspan=2)
        y_entry.insert(0, str(cur_y))
        tk.Label(self.top, text='Z : ').grid(row=2, column=0)
        z_entry = tk.Entry(self.top, justify=tk.RIGHT)
        z_entry.grid(row=2, column=1, columnspan=2)
        z_entry.insert(0, str(cur_z))

        def callback(app):
            new_x = round(float(x_entry.get()))
            new_y = round(float(y_entry.get()))
            new_z = round(float(z_entry.get()))
            x_pos = image['x'] + new_x - cur_x
            y_pos = image['y'] + new_y - cur_y
            if new_z == cur_z:
                new_z = None
            app.move_to(im_id, x_pos, y_pos, new_z, scale=True)
            app.top.destroy()

        tk.Button(self.top, text='OK', command=lambda: callback(self)).grid(row=3, column=1)

    def draw_properties_box(self, image_id):
        cell_attrs = ["_width", "_height", "_left", "_top", "_skpColor", "_compression", "_flags", "_imageSize",
                      "_packSize", "_cachedHeader", "_cached", "_changed", "_zDepth", "_xPos", "_yPos", "new_cell",
                      "old_cell"]
        world_attrs = ['view_id', 'x', 'y', 'z']
        box_height = len(cell_attrs) + len(world_attrs)
        self.top = tk.Toplevel()
        view_properties_box = tk.Text(self.top, height=box_height, width=80)
        view_properties_box.pack()
        obj = self.active_room.view_from_image[image_id]
        cell = obj.v56._loops[obj.loop]._cells[0]
        for attrs_list, attrs_storage in zip([world_attrs, cell_attrs], [obj, cell]):
            for attribute in attrs_list:
                if attribute == 'view_id':
                    view_properties_box.insert(tk.END, '{}:\t{}\n'.format(attribute, obj.v56.id))

                elif isinstance(attrs_storage, dict):
                    view_properties_box.insert(tk.END, '{}:\t{}\n'.format(attribute, attrs_storage[attribute]))
                else:
                    view_properties_box.insert(tk.END,
                                               '{}:\t{}\n'.format(attribute, str(getattr(attrs_storage, attribute))))
        self.update()
        self.wait_window(self.top)

    def set_canvas_bindings(self):
        self.room_canvas.tag_bind('atp', '<Button-1>', self.drag_start)
        self.room_canvas.tag_bind('atp', '<B1-Motion>', lambda x: self.drag_motion_button1(x, scale=True))
        self.room_canvas.tag_bind('atp', '<Button-3>', self.drag_start)
        self.room_canvas.tag_bind('atp', '<B3-Motion>', lambda x: self.drag_motion_button3(x, scale=False))
        self.room_canvas.tag_bind('object', '<Button-1>', self.drag_start)
        self.room_canvas.tag_bind('object', '<B1-Motion>', lambda x: self.drag_motion_button1(x, scale=True))
        self.room_canvas.tag_bind('view', '<Double-Button-1>', self.view_popup_menu)

    def build_menu_bar(self):
        # Create the File Cascading Menu
        file_menu = self.build_file_menu()
        self.menu.add_cascade(label='File', underline=0, menu=file_menu)
        self.menu.add_command(label='Toggle Polygons', command=self.toggle_polygons)
        # update widgets dict
        self.widgets = {**self.widgets, **{self.menu: file_menu}}

    def toggle_polygons(self):
        # items = self.room_canvas.find_withtag('polygon')
        if self.polygon_state == 'normal':
            self.room_canvas.itemconfig('polygon', state='hidden')
            self.polygon_state = 'hidden'
        elif self.polygon_state == 'hidden':
            self.room_canvas.itemconfig('polygon', state='normal')
            self.polygon_state = 'normal'

    def build_file_menu(self):
        file_menu = tk.Menu(self.menu, tearoff=False)
        file_menu.add_command(label='Open', underline=1, command=self.open_sci_file)
        file_menu.add_command(label='Add Media', underline=1, command=self.add_media)
        file_menu.add_command(label='Save', underline=1, command=self.save_world)
        file_menu.add_command(label='Save As', underline=1, command=lambda: self.save_world(saveas=True))
        file_menu.add_command(label='Exit', underline=1, command=self.quit)
        return file_menu

    def add_media(self, foldername=None):
        if not foldername:
            foldername = tk.filedialog.askdirectory()
        if foldername not in self.media['PATH']:
            self.media['PATH'].append(foldername)
        self.load_media()

    def save_world(self, saveas=False):
        wld_representation = self.world.realm_representation
        if saveas:
            wld = tk.filedialog.asksaveasfile(mode='w', defaultextension=".wld")
            if wld is None:  # asksaveasfile return `None` if dialog closed with "cancel".
                return
            if os.path.split(wld.name)[0] not in self.media['PATH']:
                self.add_media(os.path.split(wld.name)[0])
                self.zones = self.set_worlds_by_zone()
            self.save_file = wld.name
        else:
            wld = open(self.save_file, 'w')
        wld.writelines(wld_representation)
        wld.close()

    def load_media(self):
        for dir in self.media['PATH']:
            for f in os.listdir(dir):
                name, extension = os.path.splitext(f)
                if extension.lower()[1:] in ['p56', 'v56', 'wld', 'zon']:
                    full_path = os.path.join(dir, f)
                    if extension.lower() == '.wld':
                        self.media[extension.lower()[1:]][name + extension] = full_path
                    else:
                        self.media[extension.lower()[1:]][name] = full_path

    def build_wld_canvas(self, categories):
        # Create header label
        zone_header = tk.Label(self.wld_canvas, text='World_Files:')
        zone_header.pack(fill=tk.X)
        # Create custom nested option Menu
        zone_option_menu = NestedOptionMenu(self, self.wld_canvas, categories, callback=self.set_wld_listbox)
        zone_option_menu.pack(fill=tk.X)
        # Create Listbox for selectable WLDs
        listbox = tk.Listbox(self.wld_canvas)
        listbox.bind('<Double-Button-1>', lambda x: self.get_wld_from_listbox())
        listbox.pack(fill=tk.BOTH, expand=1)
        self.widgets[self.wld_canvas] = {'zone_header': zone_header, 'zone_option_menu': zone_option_menu,
                                         'wld_listbox': listbox}

        self.set_wld_listbox()

    def build_category_canvas(self, categories):
        # TODO: Remove categories that can't be added to this world:
        # Create the expected nested list format, and add object categories
        for obj_catg in self.obj_bases.keys():
            categories.append('Objects: {}'.format(obj_catg))
        # Create header label
        category_header = tk.Label(self.category_canvas, text='ATP Category: ')
        category_header.pack(fill=tk.X)
        # Create custom nested option Menu
        category_option_menu = NestedOptionMenu(self, self.category_canvas, categories, callback=self.set_category_atps)
        category_option_menu.pack(fill=tk.X)
        # Create listbox for selectable ATPs
        listbox = tk.Listbox(self.category_canvas)
        # bind listbox to double click, allowing for selection of atps
        listbox.bind('<Double-Button-1>', lambda x: self.add_view_from_listbox())
        listbox.pack(fill=tk.BOTH, expand=1)
        # update widgets list
        new_widgets = {
            self.category_canvas: {'category_header': category_header, 'category_option_menu': category_option_menu,
                                   'atp_listbox': listbox}}
        self.widgets = {**self.widgets, **new_widgets}
        # Initialize the category listbox entries the first time, without user input
        self.set_category_atps()

    def set_wld_listbox(self, category=None):
        listbox = self.widgets[self.wld_canvas]['wld_listbox']
        # Clear previous ATPs
        listbox.delete(0, tk.END)
        if not category:
            zone = self.widgets[self.wld_canvas]['zone_option_menu'].get()
        for name in self.zones[zone]:
            if name in self.media['wld'].keys():
                listbox.insert(tk.END, name)
            else:
                listbox.insert(tk.END, 'MISING-{}'.format(name))

    def set_category_atps(self, category=None):
        listbox = self.widgets[self.category_canvas]['atp_listbox']
        # Clear previous ATPs
        listbox.delete(0, tk.END)
        if not category:
            category = self.widgets[self.category_canvas]['category_option_menu'].get()
        if 'Objects' in category:
            obj_catg = category.split(':')[-1].strip()
            for obj in self.obj_bases[obj_catg]:
                if str(obj.view) in self.media['v56'].keys():
                    listbox.insert(tk.END, '{}_{}'.format(obj.name, obj.view))
        else:
            for atp_num, atp in self.atps['category'][category].items():
                view_id = self.view_num_from_atp_num(atp_num)[0]
                if str(view_id) in self.media['v56'].keys():
                    if atp.pDescriber:
                        text = '{} {}'.format(atp.pDescriber, atp_num)
                    elif atp.noun:
                        text = '{} {}'.format(atp.noun, atp_num)
                    else:
                        text = '{}'.format(atp_num)
                    listbox.insert(tk.END, text.replace(' ', '_'))

    def add_view_from_listbox(self):
        cur_category = self.widgets[self.category_canvas]['category_option_menu'].get()
        listbox = self.widgets[self.category_canvas]['atp_listbox']
        if 'Objects' not in cur_category:
            atp_description = listbox.get(listbox.curselection()[0])
            atp_num = atp_description.split('_')[-1]
            atp = ATP(atp_num)
            self.draw_atp(atp)
        else:
            obj_description = listbox.get(listbox.curselection()[0])
            obj_class, view_num = obj_description.split('_')
            obj = WorldObject(obj_class)
            self.draw_object(obj)

    def get_wld_from_listbox(self):
        listbox = self.widgets[self.wld_canvas]['wld_listbox']
        wld_name = listbox.get(listbox.curselection()[0])
        wld_path = self.media['wld'][wld_name]
        self.open_wld(wld_path)

    def draw_cell(self, cell, x=None, y=None, z=0, anchor=tk.S, scaled=True, transparent=True, mirror=False):
        pil_im = cell.get_pil_image(transparent=transparent)
        if not x:
            x_pos = (int(self.room_canvas.cget('width')) - pil_im.width) / 2
        if not y:
            y_pos = (int(self.room_canvas.cget('height')) - pil_im.height) / 2
        if mirror:
            pil_im = ImageOps.mirror(pil_im)
        if scaled:
            if y is None or x is None:
                try:
                    background_id = self.background['im_id']
                except Exception as e:
                    self.errorbox("No Background Picture Set.")
                    raise (e)
                background_im = self.background['images']['tk_image']
                if y is None: y = int(background_im.height() * 3 / 4)
                if x is None: x = int(background_im.width() / 2)
            tk_im, scaling_factor, scaled_pil_im = scale_image(pil_im, y, self.background['info'])
            picture_coords = self.room_canvas.coords(self.background['im_id'])
            x_pos = picture_coords[0] + x + int(scaling_factor * (cell._left if not mirror else -1*cell._left))
            y_pos = picture_coords[1] + y - z + int(scaling_factor * cell._top)
        else:
            if self.background:
                if y is None or x is None:
                    background_id = self.background['im_id']
                    background_im = self.background['images']['tk_image']
                    if y is None: y = int(background_im.height() * 3 / 4)
                    if x is None: x = int(background_im.width() / 2)
                picture_coords = self.room_canvas.coords(self.background['im_id'])
                x_pos = picture_coords[0] + x + (cell._left if not mirror else -1*cell._left)
                y_pos = picture_coords[1] + y - z + cell._top
            else:
                x_pos, y_pos = x, y
            tk_im, scaled_pil_im = ImageTk.PhotoImage(pil_im), None
        im_id = self.room_canvas.create_image(x_pos, y_pos, image=tk_im, anchor=anchor)
        return im_id, {'original_image': pil_im, 'scaled_image': scaled_pil_im, 'tk_image': tk_im},{'x': x_pos, 'y': y_pos}

    def set_background(self, p56_or_file, cell=0, mirror=False):
        if not isinstance(p56_or_file, p56file32):
            p56 = p56file32(p56_or_file)
        else:
            p56 = p56_or_file
        cell = p56._cells[cell]
        im_id, images, coords = self.draw_cell(cell, x=0, y=0, z=0, anchor=tk.NW, scaled=False, transparent=False, mirror=mirror)
        self.room_canvas.itemconfig(im_id, tags=('p56',))
        pic_info = self.pics[int(p56.id)]
        self.background = {'p56': p56, 'im_id': im_id, 'info': pic_info, 'images':images}
        self.pic_atps = self.atps_by_pic[pic_info.roomtype]
        self.update()

    def draw_v56(self, v56_or_file, loop=0, cell=0, x=None, y=None, z=0, scaled=True, transparent=True, mirror=False,
                 polygon=False):
        try:
            if not isinstance(v56_or_file, V56file):
                v56 = V56file(v56_or_file)
            else:
                v56 = v56_or_file
        except Exception as e:
            self.errorbox('Unable to load v56 from file:'.format(v56_or_file))
            raise (e)
        sci_loop = v56._loops[loop]
        if sci_loop._basedOnLoop != -1:
            mirror = (sci_loop._mirror if sci_loop._mirror is not None else False)
            sci_loop = v56._loops[sci_loop._basedOnLoop]
        sci_cell = sci_loop._cells[cell]
        if scaled:
            try:
                atp = self.pic_atps['view'][int(v56.id)]
                if self.background:
                    scaled = atp.pDoScaler
            except KeyError:
                atp = None
                scaled = True
        else:
            atp = None
        # Create the tk_im object
        x = (int(x) if x else 320 + sci_cell._width//2)
        y = (int(y) if y else 250)
        if z is not None: z = int(z)
        world_coords = (x,y,z)
        im_id, images, coords = self.draw_cell(sci_cell, x=x, y=y, z=z, anchor=tk.S, scaled=scaled, transparent=transparent, mirror=mirror)
        if scaled:
            tags = ['view', 'scalable', ]
        else:
            tags = ['view', ]
        if polygon:
            tags.append('polygon')
        tags = tuple(tags)
        self.room_canvas.itemconfig(im_id, tags=tags)
        return im_id, images, coords, loop, mirror, v56, world_coords

    def draw_atp(self, atp, transparent=True, polygon=False):
        add_tag = 'atp'
        mirror = atp.mirror
        try:
            atp.node = self.pic_atps['atp'][atp.reference_atp_num]
        except KeyError as e:
            print("ATP Node {} not in current pic, must be added in ATPLIST.SC to work in game".format(atp.reference_atp_num))
            atp.node = self.atps['atp'][atp.reference_atp_num]
        view_file = self.media['v56'][str(atp.node.view)]
        im_id, images, coords, loop, mirror, v56, world_cords = self.draw_v56(view_file, x=atp.x, y=atp.y, z=atp.z,
                                                                 mirror=mirror, transparent=transparent,
                                                                 polygon=polygon)
        atp.im_id = im_id
        atp.images = images
        atp.canvas_coords = coords
        atp.mirror = mirror
        atp.v56 = v56
        atp.x, atp.y, atp.z = world_cords
        self.room_canvas.addtag_withtag(add_tag, im_id)
        self.active_room.active_views.append(atp)
        self.active_room.view_from_image[im_id] = atp

    def draw_object(self, obj):
        add_tag = 'object'
        loop = (int(obj.loop) if obj.loop else 0)
        view_num = self.stk_objs[obj.object_class].view
        view_file = self.media['v56'][str(view_num)]
        im_id, images, coords, loop, mirror, v56, world_cords = self.draw_v56(view_file, loop=loop, x=obj.x, y=obj.y)
        obj.im_id = im_id
        obj.images = images
        obj.canvas_coords = coords
        obj.loop = loop
        obj.v56 = v56
        obj.x, obj.y, obj.z = world_cords
        self.room_canvas.addtag_withtag(add_tag, im_id)
        self.active_room.active_views.append(obj)
        self.active_room.view_from_image[im_id] = obj

    def open_wld(self, filename):
        if filename is None:
            return
        world = WldInterp.World(filename)
        self.world = world
        self.save_file = filename
        self.set_rooms()

    def map_button_callback(self, room):
        map_frame = self.widgets[self.map_canvas]['map_frame']
        buttons = self.widgets[self.map_canvas][map_frame]
        for k, v in buttons.items():
            if k == 'potential_rooms':
                continue
            v.configure(background='LightCyan3')
        new_button = buttons[room.number]
        new_button.configure(background='PaleTurquoise2')
        for exit in [x for x in room.properties['exits'].values() if x is not None]:
            if exit in buttons.keys():
                adj_button = buttons[exit]
                adj_button.configure(background='yellow')
        self.draw_room(room)
        self.active_room = room

    def clear_current_rooms(self):
        if self.map_canvas in self.widgets.keys():
            if 'map_frame' in self.widgets[self.map_canvas].keys():
                map_frame = self.widgets[self.map_canvas]['map_frame']
                if map_frame in self.widgets[self.map_canvas].keys():
                    for room_num, map_button in self.widgets[self.map_canvas][map_frame].items():
                        if room_num == 'potential_rooms':
                            for potential_room in map_button:
                                potential_room.grid_forget()
                        else:
                            map_button.grid_forget()

    def create_new_room(self, button_index, row, col):
        # Get the map frame
        map_frame = self.widgets[self.map_canvas]['map_frame']
        # Find all Adjacent rooms
        adjacent_rooms = {'West':(row, col-1), 'East':(row, col+1), 'North':(row-1, col), 'South':(row+1, col)}
        empty_grid = []
        for direction, grid_coords in adjacent_rooms.items():
            adjacent_rooms[direction] = None
            widgets_on_grid = map_frame.grid_slaves(grid_coords[0], grid_coords[1])
            if len(widgets_on_grid) > 0:
                if widgets_on_grid[0].room_id is not None:
                    adjacent_rooms[direction] = widgets_on_grid[0]
            else:
                empty_grid.append(grid_coords)
        # Calculate room number, set old room exits, get this rooms exits, get reference room info
        exits = {'north':None, 'east':None, 'south':None, 'west':None}
        reference_room = None
        room_num = None
        for direction in ['West', 'East', 'North', 'South']:
            room_button = adjacent_rooms[direction]
            if room_button:
                if direction == 'West':
                    room_num = (int(room_button.room_id) + 1 if room_num is None else room_num)
                    adj_room =self.rooms[room_button.room_id]
                    adj_room.properties['exits']['east'] = room_num
                    reference_room = (adj_room if reference_room is None else reference_room)
                    exits['west'] = room_button.room_id
                elif direction == 'East':
                    room_num = (int(room_button.room_id) - 1 if room_num is None else room_num)
                    adj_room =self.rooms[room_button.room_id]
                    adj_room.properties['exits']['west'] = room_num
                    reference_room = (adj_room if reference_room is None else reference_room)
                    exits['east'] = room_button.room_id
                elif direction == 'North':
                    room_num = (int(room_button.room_id) + 10 if room_num is None else room_num)
                    adj_room =self.rooms[room_button.room_id]
                    adj_room.properties['exits']['south'] = room_num
                    reference_room = (adj_room if reference_room is None else reference_room)
                    exits['north'] = room_button.room_id
                elif direction == 'South':
                    room_num = (int(room_button.room_id) - 10 if room_num is None else room_num)
                    adj_room =self.rooms[room_button.room_id]
                    adj_room.properties['exits']['north'] = room_num
                    reference_room = (adj_room if reference_room is None else reference_room)
                    exits['south'] = room_button.room_id
        buttons = self.widgets[self.map_canvas][map_frame]
        if room_num in buttons.keys():
            self.errorbox('Cannot add a room here, a room in this location already exists')
            raise(Exception('Room Number already exists!'))
        old_map_button = buttons['potential_rooms'][button_index]
        old_map_button.grid_forget()
        ## Create a new room object, add to self.rooms
        new_room = Room()
        new_room.number = room_num
        new_room.picture = (reference_room.picture if reference_room.active_background is None else reference_room.active_background)
        new_room.properties['exits'] = exits
        self.rooms[room_num] = new_room
        ## create a map button for the room
        map_button = MapButton(map_frame, room_num, width=5, height=1, background='LightCyan3',
                               text=str(room_num), highlightcolor='black',
                               command=lambda: self.map_button_callback(self.rooms[new_room.number]))
        map_button.bind('<Button-3>', lambda x: self.map_popup_menu(x, map_button))
        map_button.grid(row=row, column=col)
        buttons[room_num] = map_button
        self.map_button_callback(new_room)
        # Add the new_room buttons are any new rooms
        for grid_coord in empty_grid:
            # This probably won't always work. If it creates a possible new room in a place where a room exits from a
            #   different WLD file, this should break things. I'll need to set up a global room manager at some point...
            # TODO: global room manager for all WLD files.
            self.add_potential_room(grid_coord[0], grid_coord[1])
        # TODO: pic a p56 file
        # TODO: add a room number (How to know it's not taken?)

    def map_popup_menu(self, event, map_button):
        room_num = map_button.room_id
        room = self.rooms[room_num]
        map_popup = tk.Menu(self, tearoff=0)
        map_popup.add_command(label='Change Room Number', command=lambda: self.change_room_number(room, map_button))
        map_popup.add_command(label='Change Picture', command=lambda: self.change_room_picture(room))
        map_popup.add_command(label='Change Exits', command=lambda: self.change_room_exits(room))
        map_popup.add_command(label='Reset', command=lambda: self.reset_room(room))
        # map_popup.add_command(label='Delete', command=lambda: self.delete_room(room))
        map_popup.tk_popup(event.x_root, event.y_root, 0)

    def delete_room(self, room):
        # get the rooms that this leads to
        adjacent_rooms = [self.rooms[int(x)] for x in room.properties['exits'].values() if x is not None and int(x) in self.rooms.keys()]
        map_frame = self.widgets[self.map_canvas]['map_frame']
        button_dict = self.widgets[self.map_canvas][map_frame]
        room_button = button_dict[room.number]
        row = room_button.grid_info()['row']
        col = room_button.grid_info()['column']
        # Delete this room's button, add a potential room button
        room_button.grid_forget()
        self.add_potential_room(row, col)
        # Remove this room from the adjacent room's exits
        for room in adjacent_rooms:
            for dir, exit in room.properties['exits'].items():
                if exit == room.number:
                    room.properties['exits'][dir] = None
        # Delete the reference to this room
        del self.rooms[room.number]
        # Delete the reference to this room_button
        del button_dict[room.number]


    def change_room_exits(self, room):
        self.top = tk.Toplevel()
        tk.Label(self.top, text='Exits').grid(row=0, column=0, columnspan=3)
        exits = room.properties['exits']
        new_directions = {}
        for i, direction in enumerate(['north', 'south', 'east', 'west']):
            exit = (exits[direction] if exits[direction] else 'No Exit')
            tk.Label(self.top, text='{} :'.format(direction)).grid(row=i+1, column=0)
            dir_entry = tk.Entry(self.top, justify=tk.RIGHT)
            dir_entry.grid(row=i+1, column=1, columnspan=2)
            dir_entry.insert(0, str(exit))
            new_directions[direction] = dir_entry

        def callback(app):
            for k in room.properties['exits'].keys():
                entry = new_directions[k].get()
                if len(entry) > 0 and entry.lower() != 'No Exit'.lower():
                    try:
                        room_int = int(entry)
                    except Exception as e:
                        self.errorbox("Exit must be an integer, blank, or 'No Exit'!")
                        raise(e)
                else:
                    entry = None
                room.properties['exits'][k] = entry
            app.top.destroy()

        tk.Button(self.top, text='OK', command=lambda: callback(self)).grid(row=5, column=1)
        x = self.winfo_pointerx()
        y = self.winfo_pointery()
        w = 230
        h = 200  # self.top.winfo_height()
        self.top.geometry("%dx%d+%d+%d" % (w, h, x + 50, y - 50))

    def change_room_picture(self, room, picture=None, event=None):
        def callback(app, picture=None):
            if picture is None:
                pic = listbox.get(listbox.curselection()[0]).split('_')[-1]
                room.active_background = pic
                app.map_button_callback(room)
                app.top.destroy()
            else:
                room.active_background = picture
                app.map_button_callback(room)

        if picture is None:
            self.top = tk.Toplevel()
            header = tk.Label(self.top, text='Select a P56')
            header.pack(fill=tk.X)
            listbox = tk.Listbox(self.top)
            listbox.pack(fill=tk.BOTH, expand=1)
            listbox.bind('<Double-Button-1>', lambda x: callback(self))
            for pic in self.media['p56'].keys():
                try:
                    pic_int = int(pic)
                    if pic_int in self.pics.keys():
                        pic_info = self.pics[pic_int]
                        listbox.insert(tk.END, '{}_{}'.format(pic_info.roomtype, pic))
                except Exception as e:
                    print(e)
                    pass
            x = self.winfo_pointerx()
            y = self.winfo_pointery()
            w = 40
            h = 300
            self.top.geometry("%dx%d+%d+%d" % (w, h, x + 50, y - 200))
        else:
            callback(self, picture)

    def change_room_number(self, room, map_button, new_room_number=None):
        self.top = tk.Toplevel()
        tk.Label(self.top, text='Room Number : ').grid(row=0, column=0)
        room_num_entry = tk.Entry(self.top, justify=tk.RIGHT)
        room_num_entry.grid(row=0, column=1, columnspan=2)
        room_num_entry.insert(0, str(room.number))
        x = self.winfo_pointerx()
        y = self.winfo_pointery()
        w = 230
        h = 50  # self.top.winfo_height()
        self.top.geometry("%dx%d+%d+%d" % (w, h, x + 50, y - 50))

        def callback(app, new_room_number=None):
            if new_room_number is None:
                try:
                    new_room_number = int(room_num_entry.get())
                    if new_room_number in self.rooms.keys():
                        self.errorbox("room number: {} already exists".format(new_room_number))
                        return
                except Exception as e:
                    self.errorbox("New Room Number must be an integer.")
                    raise (e)
            # add updated room number entry
            self.rooms[new_room_number] = room
            # delete the old room number entry
            try:
                del self.rooms[room.number]
            except Exception as e:
                print(e)
            # update the button key
            map_frame = self.widgets[self.map_canvas]['map_frame']
            self.widgets[self.map_canvas][map_frame][new_room_number] = map_button
            try:
                del self.widgets[self.map_canvas][map_frame][room.number]
            except Exception as e:
                print(e)
            # update the room number in the room object
            room.number = new_room_number
            # Update the button text
            map_button.configure(text=new_room_number)
            map_button.room_id = new_room_number
            app.top.destroy()

        tk.Button(self.top, text='OK', command=lambda: callback(self, new_room_number)).grid(row=1, column=1)

    def add_potential_room(self, row, col):
        map_frame = self.widgets[self.map_canvas]['map_frame']
        buttons = self.widgets[self.map_canvas][map_frame]
        if 'potential_rooms' not in buttons.keys():
            buttons['potential_rooms'] = []
        button_index = len(buttons['potential_rooms'])
        new_map_button = MapButton(map_frame, None, width=5, height=1, background='ivory2', highlightcolor='black',
                                   text='New',
                                   command=lambda: self.create_new_room(button_index, row, col))
        new_map_button.grid(row=row, column=col)
        buttons['potential_rooms'].append(new_map_button)

    def draw_map(self, room_num=None, direction=None, row=1000, col=1000, terminate=False):
        map_frame = self.widgets[self.map_canvas]['map_frame']
        if not room_num and not terminate:
            self.widgets[self.map_canvas][map_frame] = {}
            buttons = self.widgets[self.map_canvas][map_frame]
            first_room_num = list(self.rooms.keys())[0]
            self.active_room = None
            room = self.rooms[first_room_num]
            map_button = MapButton(map_frame, first_room_num, width=5, height=1, background='LightCyan3',
                                   text=str(first_room_num), highlightcolor='black',
                                   command=lambda: self.map_button_callback(self.rooms[room.number]))
            map_button.bind('<Button-3>', lambda x: self.map_popup_menu(x, map_button))
            map_button.grid(row=row, column=col)
            buttons[first_room_num] = map_button
            for direction, exit in self.rooms[first_room_num].properties['exits'].items():
                if exit and exit in self.rooms.keys():
                    self.draw_map(exit, direction)
                elif not exit:
                    self.draw_map(exit, direction, row, col, terminate=True)
            first = True
            while len(self.rooms) != len(buttons) - 1:
                remaining_rooms = [x for x in self.rooms.keys() if x not in buttons.keys()]
                if len(remaining_rooms) == 0:
                    break
                next_room_num = remaining_rooms[0]
                if first:
                    row, col = 1000, 2000
                    first = not first
                else:
                    col += 1
                    if col % 4 == 0:
                        row += 1
                        col -= 4
                    self.draw_map(next_room_num, row=row, col=col)
        else:
            buttons = self.widgets[self.map_canvas][map_frame]
            if direction:
                side_dict = {'north': (-1, 0), 'south': (1, 0), 'east': (0, 1), 'west': (0, -1)}
                row, col = row + side_dict[direction][0], col + side_dict[direction][1]
            if len(map_frame.grid_slaves(row, col)) > 0:
                return
            if terminate:
                if 'potential_rooms' not in buttons.keys():
                    buttons['potential_rooms'] = []
                button_index = len(buttons['potential_rooms'])
                map_button = MapButton(map_frame, None, width=5, height=1, background='ivory2', highlightcolor='black',
                                       text='New', command=lambda: self.create_new_room(button_index, row, col))
                map_button.grid(row=row, column=col)
                buttons['potential_rooms'].append(map_button)
            elif room_num in self.rooms.keys() and room_num not in buttons.keys():
                room = self.rooms[room_num]
                map_button = MapButton(map_frame, room_num, width=5, height=1, background='LightCyan3',
                                       highlightcolor='black', text=str(room_num),
                                       command=lambda: self.map_button_callback(self.rooms[room.number]))
                map_button.bind('<Button-3>', lambda x: self.map_popup_menu(x, map_button))
                map_button.grid(row=row, column=col)
                buttons[room_num] = map_button
                if not direction:
                    return
                for direction, exit in self.rooms[room_num].properties['exits'].items():
                    if exit and exit in self.rooms.keys() and exit not in buttons.keys():
                        self.draw_map(exit, direction, row, col)
                    elif not exit:
                        self.draw_map(exit, direction, row, col, terminate=True)

    def set_rooms(self):
        self.clear_current_rooms()
        self.rooms = {r.number: r for r in self.world.rooms}
        if self.map_canvas in self.widgets.keys():
            if 'map_frame' in self.widgets[self.map_canvas].keys():
                map_frame = self.widgets[self.map_canvas]['map_frame']
            else:
                map_frame = tk.Frame(self.map_canvas)
                map_frame.pack(anchor=tk.CENTER)
        else:
            map_frame = tk.Frame(self.map_canvas)
            map_frame.pack(anchor=tk.CENTER)
        self.widgets[self.map_canvas] = {}
        self.widgets[self.map_canvas]['map_frame'] = map_frame
        self.draw_map()
        first_room_number = self.world.rooms[0].number
        self.map_button_callback(self.rooms[first_room_number])
        self.widgets[self.map_canvas][map_frame][first_room_number].configure(background='PaleTurquoise2')
        self.update()

    def open_sci_file(self, filename=None):
        if not filename:
            filename = filedialog.askopenfilename()
        name, extension = os.path.splitext(filename)
        if extension.lower() not in ['.v56', '.p56', '.wld']:
            self.errorbox('Extension {} is not a SCI filetype'.format(extension))
            raise (Exception('Not a SCI File: {}'.format(extension)))
        if extension.lower() == '.wld':
            self.open_wld(filename)
        if extension.lower() == '.v56':
            v56 = V56file(filename)
            self.draw_v56(v56)
        if extension.lower() == '.p56':
            p56 = p56file32(filename)
            self.set_background(p56)

    def reference_atp_num(self, atp_num):
        if int(atp_num) > 32768:
            atp_num -= 32768
        return atp_num

    def view_num_from_atp_num(self, atp_num):
        if int(atp_num) > 32768:
            atp_num = atp_num - 32768
            mirror = True
        else:
            mirror = False
        view_id = None
        if atp_num in self.atps['atp'].keys():
            view_id = self.atps['atp'][atp_num].view
        elif atp_num + 1000 in self.atps['atp'].keys():
            view_id = self.atps['atp'][atp_num + 1000].view
        return view_id, mirror

    def view_from_atp_number(self, atp_num):
        view_id, mirror = self.view_num_from_atp_num(atp_num)
        if str(view_id) not in self.media['v56']:
            return None, mirror
        view_file = self.media['v56'][str(view_id)]
        return view_file, mirror

    def reset_room(self, room):
        room.reset()
        self.draw_room(room)

    def draw_room(self, room):
        # reset Previous room
        self.background = None
        self.room_canvas.delete("all")
        self.active_room = room
        # check if we need to use a template
        if 'template' in room.properties.keys():
            template_room_num = room.properties['template']
            template_room_wld_file = self.media['wld'][self.room_directory[template_room_num]]
            template_room_wld = WldInterp.World(template_room_wld_file)
            try:
                template_room_num_int = int(template_room_num)
                template_room = [x for x in template_room_wld.rooms if x.number == template_room_num_int][0]
            except:
                print("Template Room {} not found in current WLD files".format(template_room_num))
            room.picture = template_room.picture
            room.properties['picture'] = room.picture
            del room.properties['template']
            room.atpinfo += template_room.atpinfo
            room.objects += template_room.objects
        pic = room.picture
        if room.active_background:
            pic = room.active_background
        file_path = self.media['p56'][pic]
        self.open_sci_file(file_path)
        if len(self.active_room.active_views) > 0:
            depth_sorted_atps_objs = [[int(atp_or_obj.y), atp_or_obj] for atp_or_obj in room.active_views]
            room.active_views = []
        else:
            depth_sorted_atps_objs = [[int(atp_or_obj.y), atp_or_obj] for atp_or_obj in room.atpinfo + room.objects]
        depth_sorted_atps_objs.sort(key=lambda x: x[0])
        for atp_or_obj_info in depth_sorted_atps_objs:
            atp_or_obj = atp_or_obj_info[1]
            try:
                if isinstance(atp_or_obj, ATP):
                    atp = atp_or_obj
                    if atp.reference_atp_num in self.atps['category']['Polygons'].keys():
                        self.draw_atp(atp, transparent=False, polygon=True)
                    else:
                        self.draw_atp(atp)
                elif isinstance(atp_or_obj, WorldObject):
                    obj = atp_or_obj
                    self.draw_object(obj)
            except KeyError as e:
                print(e)
                continue
        # Hide the polygons, by default
        self.polygon_state = 'normal'
        self.toggle_polygons()
        self.update()


if __name__ == '__main__':
    try:
        w = WorldCreator(atp_categories=ATP_CATEGORIES, pic_info=PIC_INFO, object_info=stkObjDict)
    except Exception as e:
        raise(e)
