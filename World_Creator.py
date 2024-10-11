import os
import pathlib
import random
import tkinter
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog, messagebox
import PySimpleGUI as sg

from PIL import ImageTk, ImageOps

from rapidfuzz import fuzz, process
import appdirs

import atp_info
import stock_objects
import ui
from kaitaisci.picture import Picture
from kaitaisci.sci_resource import Ressci, ResType
from kaitaisci.view import View
from atp_info import ATP_CATEGORIES, ATP_BY_PIC
from pic_info import parse_pic_info_file
from realm.WLDInterpreter import ATP, WorldObject, Room
import realm.WLDInterpreter as WldInterp
from scires.legacy.p56files import p56file32
from scires.legacy.v56files import V56file
from stock_objects import StockObjList, generate_python_stock_objects
from ui.components import NestedOptionMenu, MapButton, ViewCategoriesTreeView
from utils import scale_image
import importlib.util
from pathlib import Path

PIC_INFO = {}
for pic in parse_pic_info_file("Resources/PICINFO.SC"):
    PIC_INFO[pic.picture] = pic

# Good? Bad? Who knows. We dynamically load these modules
# maybe better or worse, but we dynamically create them beforehand
generate_python_stock_objects()

for f in Path('Resources/objects/python/test').parent.glob("*.py"):
    module_name = f.stem
    if (not module_name.startswith("_")) and (module_name not in globals()):
        # import_module(f"Resources.objects.python.{module_name}")

        spec = importlib.util.spec_from_file_location(module_name, f"{f}")
        stkobj_module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(stkobj_module)

    del f, module_name
del importlib.util, Path

stkObjDict = {obj.name: obj for obj in StockObjList}


class WorldCreator(tk.Tk):
    def __init__(self, title='World Creator', atp_categories=None, pic_info=None, object_info=None,
                 atps_by_pic=ATP_BY_PIC):
        tk.Tk.__init__(self)
        self.geometry("1600x900")
        self.tk_setPalette(
            background='#f0f0f0')  # , foreground='#f0f0f0', activeBackground='#f0f0f0', activeForeground="#f0f0f0")

        # cache for images
        self.cached = {}
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
        # Storage for access to resource files
        self.resources = {'resources': {}, 'v56': {}, 'p56': {}, 'wld': {}, 'zon': {}, 'PATH': []}
        self.background = None
        # Build default resource paths
        default_56_path = os.path.join('Resources', '56_Files')
        default_ressci_path = os.path.join('Resources', 'ressci')
        default_wld_path = os.path.join('Resources', 'world')
        default_zon_path = os.path.join('Resources', 'zones')

        self.add_resource_dir(default_ressci_path)
        self.add_resource_dir(default_56_path)
        self.add_resource_dir(default_wld_path)
        self.add_resource_dir(default_zon_path)
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
        self.category_canvas.grid(row=0, column=0, rowspan=20, sticky="news")
        # builds header, option menu, and listbox for category ATPs
        self.build_category_tree()

        # Create the center canvas, which holds the v56 and p56 images.
        self.room_canvas = tk.Canvas(self, width=640, height=320)
        self.room_canvas.grid(row=0, column=2, sticky="news")
        # Allow for draggable children of this canvas
        self.set_canvas_bindings()
        # Create the map canvas:
        self.map_frame = tk.Frame()
        self.map_frame.grid(row=1, column=1, columnspan=3, rowspan=19, sticky="news")
        # Create WLD column Canvas
        self.wld_canvas = tk.Canvas()
        self.wld_canvas.grid(row=0, column=4, rowspan=20, sticky="news")

        self.grid_rowconfigure((1, 2), weight=1)
        self.grid_columnconfigure((0, 1, 3, 4), weight=1)
        # Setup the wld listbox
        self.build_wld_canvas()
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
        for zon, path in self.resources['zon'].items():
            with open(path, 'r', encoding='ISO-8859-1') as f:
                lines = f.readlines()
            lines = [x for x in lines if 'worldFile' in x or 'title' in x]
            temp = {'title': '', 'worlds': []}
            for line in lines:
                if 'title' in line:
                    line = line[line.find('"') + 1:line.rfind('"')].replace(':', '')
                    temp['title'] = line
                elif '.wld' in line.lower():
                    wld_file = line[line.find('=') + 1:line.lower().rfind('.wld') + 4].split('/')[-1].strip()
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
        for wld in self.resources['wld'].keys():
            if wld.lower() not in worlds_with_zone:
                if 'Misc' not in worlds_by_zone.keys():
                    worlds_by_zone['Misc'] = []
                worlds_by_zone['Misc'].append(wld)
        return worlds_by_zone

    def build_room_directory(self):
        room_directory = {}
        for wld, path in self.resources['wld'].items():
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
            # pixel_xy in image, of pixel under cursor
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
        view_popup.add_command(label='Properties', command=lambda: self.draw_properties_box(im_id))
        view_popup.add_command(label='Move To', command=lambda: self.xyz_entry_popup(im_id))
        if 'atp' in image_tags:
            view_popup.add_command(label='Mirror', command=lambda: self.mirror_image(im_id))
        elif 'object' in image_tags:
            view_popup.add_command(label='Next Loop', command=lambda: self.next_loop(im_id))
        view_popup.add_command(label='Delete', command=lambda: self.delete_from_room(im_id))
        # try:
        view_popup.tk_popup(event.x_root, event.y_root, 0)  # finally:  view_popup.grab_release()

    def next_loop(self, im_id):
        v56 = self.active_room.view_from_image[im_id].v56
        obj = self.active_room.view_from_image[im_id]
        x = obj.x
        y = obj.y
        z = obj.z

        obj.loop = (obj.loop + 1) % len(v56.loops)
        # but why not mod?
        # max_loop = len(v56.loops) - 1
        # cur_loop = obj.loop
        # if cur_loop == max_loop:
        #     cur_loop = 0
        # else:
        #     cur_loop += 1
        # obj.loop = cur_loop

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
            if new_z == cur_z:
                new_z = None
            app.move_to(im_id, new_x, new_y, new_z)

        tk.Button(self.top, text='OK', command=lambda: callback(self)).grid(row=3, column=1)

    def draw_properties_box(self, image_id):
        cell_attrs = ["width", "height", "x_shift", "y_shift", "transparent_color"]
        loop_attrs = ["based_on_loop", "mirror"]
        world_attrs = ['view_id', 'x', 'y', 'z', 'loop']
        self.top = tk.Toplevel()
        obj = self.active_room.view_from_image[image_id]
        loop = obj.v56.loops[obj.loop]
        cell = loop.cells[0]
        grid_row = 0

        def add_row(idx, start_column, k, v):
            label = tk.Label(self.top, text=k)
            label.grid(row=idx, column=start_column, sticky='e')
            spacer_label = tk.Label(self.top, text=" ")
            spacer_label.grid(row=idx, column=start_column + 1)
            entry = tk.Entry(self.top)
            entry.insert(0, str(v) if v is not None else "")
            entry.grid(row=idx, column=start_column + 2)

        for attrs_list, attrs_storage in zip([world_attrs, loop_attrs, cell_attrs], [obj, loop.header, cell]):
            for attribute in attrs_list:
                if attribute == 'view_id':
                    add_row(grid_row, 0, attribute, obj.v56.id)
                elif attribute == 'loop':
                    add_row(grid_row, 0, attribute, obj.loop)
                elif isinstance(attrs_storage, dict):
                    if attribute in attrs_storage.keys():
                        add_row(grid_row, 0, attribute, attrs_storage[attribute])
                else:
                    if hasattr(attrs_storage, attribute):
                        add_row(grid_row, 0, attribute, str(getattr(attrs_storage, attribute)))
                grid_row += 1

        grid_row = 0
        if isinstance(obj, ATP):
            atp_node = self.atps['atp'][obj.reference_atp_num]
            for attr in ['noun', 'pCategory', 'pDescriber']:
                if hasattr(atp_node, attr):
                    add_row(grid_row, 3, attr, getattr(atp_node, attr))
                    grid_row += 1
        elif isinstance(obj, WorldObject):
            add_row(grid_row, 3, "name", obj.name)
            add_row(grid_row + 1, 3, "class", obj.object_class)

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
        # Create the menu bar
        file_menu = self.build_file_menu()
        view_menu = self.build_view_menu()
        resource_menu = self.build_resources_menu()
        self.menu.add_cascade(label='File', underline=0, menu=file_menu)
        self.menu.add_cascade(label='View', underline=0, menu=view_menu)
        self.menu.add_cascade(label='Resources', underline=0, menu=resource_menu)
        # update widgets dict
        self.widgets = {**self.widgets,
                        **{self.menu: {"file": file_menu, "view": view_menu, "resources": resource_menu}}}

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
        file_menu.add_command(label='Open', underline=0, command=self.open_sci_file)
        file_menu.add_command(label='Save', underline=0, command=self.save_world)
        file_menu.add_command(label='Save As', underline=5, command=lambda: self.save_world(saveas=True))
        file_menu.add_command(label='Exit', underline=0, command=self.quit)
        return file_menu

    def build_resources_menu(self):
        resources_menu = tk.Menu(self.menu, tearoff=False)
        resources_menu.add_command(label='Resource Paths', underline=9, command=self.resource_list_window)
        return resources_menu

    def build_view_menu(self):
        view_menu = tk.Menu(self.menu, tearoff=False)
        view_menu.add_command(label='Toggle Polygon', underline=7, command=self.toggle_polygons)
        return view_menu

    def resource_list_window(self):

        default_paths = "-DEFAULT_PATHS_LIST-"
        add_res_path = "-ADD_RESOURCE_PATH-"
        default_list = sg.Listbox(self.resources["PATH"], size=(50, 10), expand_x=True, expand_y=True,
                                  enable_events=True, key=default_paths)
        remove_resource_dir = "-REMOVE_RESOURCE_DIR-"
        msg = "-MSG-"
        layout = [
            [sg.Input(expand_x=True, key=add_res_path), sg.Button('Add'),
             sg.FolderBrowse("Browse", target=add_res_path)],
            [default_list],
            [sg.Button("Remove", key=remove_resource_dir)],
            [sg.Text("", key=msg)]
        ]

        window = sg.Window('Resource Paths', layout, resizable=True)
        while True:
            event, values = window.read()
            if event in (sg.WIN_CLOSED, 'Exit'):
                break
            if event == 'Add':
                resource_dir = values[add_res_path]
                if (len(pathlib.Path(resource_dir).name.strip()) > 0):
                    if self.add_resource_dir(resource_dir):
                        self.build_category_tree()
                        self.zones = self.set_worlds_by_zone()
                        self.build_wld_canvas()
                        if self.active_room is not None:
                            self.load_room(self.active_room, reset=True)
                        window[default_paths].update(self.resources["PATH"])
                        window[msg].update("Added")

            if event == remove_resource_dir:
                for to_remove in default_list.get():
                    paths = self.resources["PATH"]
                    if to_remove in paths:
                        paths.remove(to_remove)
                        window[msg].update(f"Removed: {to_remove}")
                window[default_paths].update(self.resources["PATH"])
        window.close()

    def add_resource_dir(self, resource_dir: str | os.PathLike[str]) -> bool:
        resource_path = pathlib.Path(resource_dir)
        if not resource_path.exists():
            return False

        if resource_dir not in self.resources['PATH']:
            self.resources['PATH'].append(resource_dir)
        self.load_resources(resource_dir)
        return True

    def save_world(self, saveas=False):
        wld_representation = self.world.realm_representation
        if saveas:
            wld = tk.filedialog.asksaveasfile(mode='w', defaultextension=".wld")
            if wld is None:  # asksaveasfile return `None` if dialog closed with "cancel".
                return
            if os.path.split(wld.name)[0] not in self.resources['PATH']:
                self.add_resource_dir(os.path.split(wld.name)[0])
                self.zones = self.set_worlds_by_zone()
                self.build_wld_canvas()

            self.save_file = wld.name
        else:
            wld = open(self.save_file, 'w')
        wld.writelines(wld_representation)
        wld.close()

    def load_all_resources(self):
        for dir in self.resources['PATH']:
            if not os.path.exists(dir):
                continue
            self.load_resources(dir)

    def load_resources(self, resource_dir: str | os.PathLike[str]):
        for folder in os.listdir(resource_dir):
            full_path = os.path.join(resource_dir, folder)
            name, extension = os.path.splitext(folder)
            if extension.lower() in ['.p56', '.v56', '.wld', '.zon']:
                if extension.lower() == '.wld':
                    self.resources[extension.lower()[1:]][name + extension] = full_path
                else:
                    self.resources[extension.lower()[1:]][name] = full_path
            else:
                self.load_packed_resource(full_path)

    def load_packed_resource(self, ressci_path: str):
        if ressci_path in self.resources["resources"].keys():
            return
        try:
            resources = Ressci.from_file(ressci_path)
            self.resources["resources"][ressci_path] = resources
        except:
            self.log_to_display(f"Unable to load resource at {ressci_path}")

    def build_wld_canvas(self):
        for child in self.wld_canvas.winfo_children():
            child.destroy()

        categories = list(self.zones.keys())
        # Create header label
        zone_header = tk.Label(self.wld_canvas, text="World:")
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

    def save_to_favorites(self, lines: atp_info.ATPNode | stock_objects.StockObject | list[
        atp_info.ATPNode | stock_objects.StockObject]):
        def get_atp_line(atp: atp_info.ATPNode) -> str:
            return f'atp\t{atp.number}\n'

        def get_obj_line(obj: stock_objects.StockObject) -> str:
            return f'obj\t{obj.name}\n'

        with open(self.favorites_path(), 'a') as favorites:
            if type(lines) != list:
                lines = [lines]
            for line in lines:
                if isinstance(line, atp_info.ATPNode):
                    favorites.write(get_atp_line(line))
                elif isinstance(line, stock_objects.StockObject):
                    favorites.write(get_obj_line(line))

    def favorites_path(self) -> pathlib.Path:
        config_dir = pathlib.Path(appdirs.user_config_dir("RealmWorldCreator", False))
        config_dir.mkdir(parents=True, exist_ok=True)
        return config_dir / "favorites.txt"

    def load_favorites(self) -> list[atp_info.ATPNode | stock_objects.StockObject]:
        atp_objs = []
        with open(self.favorites_path(), 'r') as favorites:
            for fav in favorites.readlines():
                (type, id) = fav.strip().split(sep='\t')
                if type == 'atp':
                    atp_objs.append(self.atps['atp'][int(id)])
                elif type == 'obj':
                    atp_objs.append(self.stk_objs[id])
        atp_objs = list(set(atp_objs))

        def sort_key_atp_obj(atp_obj: atp_info.ATPNode | stock_objects.StockObject):
            if isinstance(atp_obj, atp_info.ATPNode):
                return atp_obj.pDescriber if atp_obj.pDescriber else atp_obj.number
            if isinstance(atp_obj, stock_objects.StockObject):
                return f"{atp_obj.name} ({atp_obj.pName})"

        atp_objs.sort(key=sort_key_atp_obj)

        return atp_objs

    def clear_favorites(self):
        self.favorites_path().unlink(missing_ok=True)

    def build_category_tree(self):
        single_context_menu = tk.Menu(self, tearoff=0)

        # TODO: Remove categories that can't be added to this world:
        # Create the expected nested list format, and add object categories
        categories = list(self.atps['category'].keys())
        for obj_catg in self.obj_bases.keys():
            categories.append('Objects: {}'.format(obj_catg))

        # Create ScrollableTreeView for selectable ATPs and Objects
        for child in self.category_canvas.winfo_children():
            child.destroy()
        atp_obj_tabs = ttk.Notebook(self.category_canvas)
        atps_objs_tab = ttk.Frame(atp_obj_tabs)
        favorites_tab = ttk.Frame(atp_obj_tabs)
        search_tab = ttk.Frame(atp_obj_tabs)

        atps_objs_tree_scroll_frame = tk.Frame(atps_objs_tab)
        atps_objs_tree_scroll_frame.pack(fill=tk.BOTH, expand=True)
        atp_treeview = ViewCategoriesTreeView(atps_objs_tree_scroll_frame, ["ATP/Objects"])
        atp_tree_scroll_y = tk.Scrollbar(atps_objs_tree_scroll_frame, command=atp_treeview.yview)
        atp_tree_scroll_y.pack(side=tk.RIGHT, fill=tk.Y)

        # bind atp_treeview to double click, allowing for selection of atps
        atp_treeview.bind('<Double-Button-1>', lambda x: self.add_view_from_treeview())
        atp_treeview.configure(yscrollcommand=atp_tree_scroll_y.set)
        atp_treeview.pack(fill=tk.BOTH, expand=True)

        atp_obj_tabs.add(atps_objs_tab, text="ATPs / Objects")
        atp_obj_tabs.add(favorites_tab, text="Favorites")
        atp_obj_tabs.add(search_tab, text="Search")

        atp_obj_tabs.pack(expand=True, fill=tk.BOTH)

        # update widgets list
        new_widgets = {
            self.category_canvas: {'-CATEGORY_ENTRIES-': atp_treeview}
        }
        self.widgets = {**self.widgets, **new_widgets}
        # Initialize the category listbox entries the first time, without user input
        self.set_category_atps()

        # Create input field for search
        search_string_var = tk.StringVar()
        search_entry = tk.Entry(search_tab, textvariable=search_string_var)
        search_entry.pack()

        # Create list box for search results
        search_results_listbox = tk.Listbox(search_tab)
        search_results_listbox.pack(fill=tk.BOTH, expand=True)

        def favorites_menu(event, atp_obj: atp_info.ATPNode | stock_objects.StockObject | None):
            if not atp_obj:
                return

            single_context_menu.delete(0)
            single_context_menu.add_command(label="Add to Favorites", command=lambda: self.save_to_favorites(atp_obj))
            single_context_menu.tk_popup(event.x_root, event.y_root, 0)

        def get_string_names(atp_obj):
            if isinstance(atp_obj, atp_info.ATPNode):
                return atp_treeview.format_atp_name(atp_obj)
            if isinstance(atp_obj, stock_objects.StockObject):
                return f"{atp_obj.name} ({atp_obj.pName})"
            else:
                return atp_obj

        def flatten_dict(d):
            if isinstance(d, dict):
                return [i for sublist in [flatten_dict(value) for value in d.values()] for i in sublist]
            elif isinstance(d, list):
                return [i for sublist in map(flatten_dict, d) for i in sublist]
            else:
                return [d]

        atp_objs = flatten_dict(atp_treeview.categories)
        sort_names = [get_string_names(x) for x in atp_objs]
        lower_names = [x.lower() for x in sort_names]

        def fuzzy_sort(names, query, limit):
            # Calculate fuzzy similarity and get top matches
            top_matches = process.extract(query, names, scorer=fuzz.ratio, limit=limit)

            return [(sort_names[idx], idx) for name, score, idx in top_matches]

        def on_search_string_change(*args):
            search_string = search_string_var.get()

            search_results = fuzzy_sort(lower_names, search_string.lower(), limit=40)

            search_results_listbox.delete(0, tk.END)

            # put search results into the list box
            for (name, idx) in search_results:
                search_results_listbox.insert(tk.END, name)

            def get_nearest_item(event=None):
                cur_idx = search_results_listbox.nearest(event.y)
                atp_obj_idx = search_results[cur_idx][1]
                return atp_objs[atp_obj_idx]

            def add_view_from_search_list(event):
                atp_or_obj = get_nearest_item(event)
                if isinstance(atp_or_obj, atp_info.ATPNode):
                    self.draw_atp(ATP(atp_or_obj.number))
                elif isinstance(atp_or_obj, stock_objects.StockObject):
                    self.draw_object(WorldObject(atp_or_obj.name))

            search_results_listbox.bind('<Double-Button-1>', add_view_from_search_list)
            search_results_listbox.bind('<Button-3>', lambda x: favorites_menu(x, get_nearest_item(x)))

        # Add trace to the search string var to call on_search_string_change every time it's changed
        search_string_var.trace('w', on_search_string_change)

        favorites_listbox = tk.Listbox(favorites_tab)
        favorites_listbox.pack(fill=tk.BOTH, expand=True)

        def nearest_atp_or_obj(event) -> atp_info.ATPNode | stock_objects.StockObject | None:
            item = atp_treeview.identify('item', event.x, event.y)
            values = atp_treeview.item(item, 'values')
            if len(values) == 2:
                if values[1] == 'atp':
                    return self.atps['atp'][int(values[0])]
                if values[1] == 'obj':
                    return self.stk_objs[values[0]]
            return None

        def update_favorites(event):
            favorites = self.load_favorites()
            favorites_listbox.delete(0, tk.END)
            for fav in favorites:
                if isinstance(fav, atp_info.ATPNode):
                    favorites_listbox.insert(tk.END, atp_treeview.format_atp_name(fav))
                elif isinstance(fav, stock_objects.StockObject):
                    favorites_listbox.insert(tk.END, fav.name)

            def add_view_from_favorites_list(event):
                cur_idx = favorites_listbox.curselection()[0]
                fav_item = favorites[cur_idx]
                if isinstance(fav_item, atp_info.ATPNode):
                    self.draw_atp(ATP(fav_item.number))
                elif isinstance(fav_item, stock_objects.StockObject):
                    self.draw_object(WorldObject(fav_item.name))

            def remove_from_favorites(event):
                idx = favorites_listbox.nearest(event.y)
                favorites.pop(idx)
                self.clear_favorites()
                self.save_to_favorites(favorites)
                update_favorites(event)

            def favorites_context_menu(event):
                single_context_menu.delete(0)
                single_context_menu.add_command(label="Remove from Favorites",
                                                command=lambda: remove_from_favorites(event))
                single_context_menu.tk_popup(event.x_root, event.y_root, 0)

            favorites_listbox.bind('<Double-Button-1>', add_view_from_favorites_list)
            favorites_listbox.bind('<Button-3>', lambda x: favorites_context_menu(x))

        favorites_listbox.bind('<Visibility>', update_favorites)
        atp_treeview.bind('<Button-3>', lambda x: favorites_menu(x, nearest_atp_or_obj(x)))

    def set_wld_listbox(self, category=None):
        listbox = self.widgets[self.wld_canvas]['wld_listbox']
        # Clear previous ATPs
        listbox.delete(0, tk.END)
        if not category:
            zone = self.widgets[self.wld_canvas]['zone_option_menu'].get()
        for name in self.zones[zone]:
            if name in self.resources['wld'].keys():
                listbox.insert(tk.END, name)
            else:
                listbox.insert(tk.END, 'MISSING-{}'.format(name))

    def set_category_atps(self, ):
        treeview: ViewCategoriesTreeView = self.widgets[self.category_canvas]['-CATEGORY_ENTRIES-']
        treeview.categories = {
            "Objects": {},
            "Region": {}
        }
        for (base, objects) in self.obj_bases.items():
            treeview.categories["Objects"][base] = objects

        regions = treeview.categories["Region"]
        for (region_set, set_atps) in self.atps["category"].items():
            if ":" in region_set:
                region, atp_set = [x.strip() for x in region_set.split(":")]
                if region not in regions:
                    regions[region] = {}
                regions[region][atp_set] = set_atps
            else:
                regions[region_set] = set_atps

        treeview.categories["ATP"] = [x for x in self.atps["atp"].values()]
        treeview.categories["ATP"].sort(key=treeview.format_atp_name)
        treeview.reset_view_categories()

    def view_found_in_resources(self, num: int):
        if str(num) in self.resources['v56'].keys():
            return True
        for res in self.resources["resources"].values():
            if res.has_resource(ResType.view, num):
                return True
        return False

    def get_resource(self, restype: ResType, num: int):
        res: Ressci
        for res in self.resources["resources"].values():
            if res.has_resource(restype, num):
                if restype == ResType.view:
                    return res.get_view(num)
                elif restype == ResType.pic:
                    return res.get_pic(num)

    def add_view_from_treeview(self):
        if self.background == None:
            return
        treeview: ViewCategoriesTreeView = self.widgets[self.category_canvas]['-CATEGORY_ENTRIES-']
        item_values = treeview.item(treeview.selection()[0], "values")
        if len(item_values) < 2:
            return

        (selection, atp_or_obj) = item_values[:2]
        if atp_or_obj == "atp":
            self.draw_atp(ATP(selection))
        elif atp_or_obj == "obj":
            self.draw_object(WorldObject(selection))

    def get_wld_from_listbox(self):
        listbox = self.widgets[self.wld_canvas]['wld_listbox']
        wld_name = listbox.get(listbox.curselection()[0])
        wld_path = self.resources['wld'][wld_name]
        self.open_wld(wld_path)

    def draw_cell(self, cell, x=None, y=None, z=0, anchor=tk.S, scaled=True, transparent=True, mirror=False,
                  cached=False):
        # if cached is not None, is it a tuple of (v56_num, loop, cell)
        if cached:
            # Todo, this will always use the transparency and mirror of the first time this cell was drawn; fix to depend on transparent arg
            pil_im = self.cached[cached]
        else:
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
            x_pos = picture_coords[0] + x + int(scaling_factor * (cell.x_shift if not mirror else -1 * cell.x_shift))
            y_pos = picture_coords[1] + y - z + int(scaling_factor * cell.y_shift)
        else:
            if self.background:
                if y is None or x is None:
                    background_id = self.background['im_id']
                    background_im = self.background['images']['tk_image']
                    if y is None: y = int(background_im.height() * 3 / 4)
                    if x is None: x = int(background_im.width() / 2)
                picture_coords = self.room_canvas.coords(self.background['im_id'])
                x_pos = picture_coords[0] + x + (cell.x_shift if not mirror else -1 * cell.x_shift)
                y_pos = picture_coords[1] + y - z + cell.y_shift
            else:
                x_pos, y_pos = x, y
            tk_im, scaled_pil_im = ImageTk.PhotoImage(pil_im), None
        im_id = self.room_canvas.create_image(x_pos, y_pos, image=tk_im, anchor=anchor)
        return im_id, {'original_image': pil_im, 'scaled_image': scaled_pil_im, 'tk_image': tk_im}, {'x': x_pos,
                                                                                                     'y': y_pos}

    def set_background(self, p56_or_file, cell=0, mirror=False):
        if not isinstance(p56_or_file, (p56file32, Picture)):
            p56 = Picture.from_file(p56_or_file)
        else:
            p56 = p56_or_file
        cell = p56.cells[cell]
        im_id, images, coords = self.draw_cell(cell, x=0, y=0, z=0, anchor=tk.NW, scaled=False, transparent=False,
                                               mirror=mirror)
        self.room_canvas.itemconfig(im_id, tags=('p56',))
        pic_info = self.pics[int(p56.id)]
        self.background = {'p56': p56, 'im_id': im_id, 'info': pic_info, 'images': images}
        self.pic_atps = self.atps_by_pic[pic_info.room_type]
        self.update()

    def draw_v56(self, v56_or_file, loop=0, cell=0, x=None, y=None, z=0, scaled=True, transparent=True, mirror=False,
                 polygon=False):
        try:
            if not isinstance(v56_or_file, (V56file, View)):
                v56 = View.from_file(v56_or_file)
            else:
                v56 = v56_or_file
        except Exception as e:
            self.errorbox(f'Unable to load v56 from file:{v56_or_file}')
            raise (e)
        sci_loop = v56.loops[loop]
        if sci_loop.based_on_loop != -1:
            mirror = (sci_loop.mirror if sci_loop.mirror is not None else False)
            sci_loop = v56.loops[sci_loop.based_on_loop]
        sci_cell = sci_loop.cells[cell]
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
        x = (int(x) if x else 320 + sci_cell.width // 2)
        y = (int(y) if y else 250)
        if z is not None: z = int(z)
        world_coords = (x, y, z)
        # check if the v56 pil image is cached
        cached = None
        # will only cache non-transparent, non-mirrored cells
        if (v56.id, loop, cell) in self.cached.keys() and transparent and not mirror:
            cached = (v56.id, loop, cell)
        im_id, images, coords = self.draw_cell(sci_cell, x=x, y=y, z=z, anchor=tk.S, scaled=scaled,
                                               transparent=transparent, mirror=mirror, cached=cached)
        # if it isn't cached, cache it
        if (v56.id, loop, cell) not in self.cached.keys() and transparent and not mirror:
            if len(self.cached) > 500:
                self.cached.pop(random.choice(self.cached.keys()))
            self.cached[(v56.id, loop, cell)] = images['original_image'].copy()
        if scaled:
            tags = ['view', 'scalable', ]
        else:
            tags = ['view', ]
        if polygon:
            tags.append('polygon')
        tags = tuple(tags)
        self.room_canvas.itemconfig(im_id, tags=tags)
        return im_id, images, coords, loop, mirror, v56, world_coords

    def draw_atp(self, atp: ATP):

        if atp.reference_atp_num in self.atps['category']['Polygons'].keys():
            transparent = False
            polygon = True
        else:
            transparent = True
            polygon = False

        add_tag = 'atp'
        mirror = atp.mirror
        try:
            atp.node = self.pic_atps['atp'][atp.reference_atp_num]
        except KeyError:
            atp_node = self.atps['atp'][atp.reference_atp_num]
            text = atp_node.pDescriber if atp_node.pDescriber else atp_node.noun if atp_node.noun else atp.reference_atp_num
            self.log_to_display(
                f"ATP \"{text}\" (ATP{atp.reference_atp_num}) not in current pic, must be added in ATPLIST.SC to work in game")
            atp.node = atp_node
        try:
            view = self.get_view_resource(atp.node.view)
        except KeyError:
            text = atp_node.pDescriber if atp_node.pDescriber else atp_node.noun if atp_node.noun else atp.reference_atp_num
            self.log_to_display(f"View ({atp.node.view}) missing for ATP \"{text}\"")
            return

        im_id, images, coords, loop, mirror, v56, world_cords = self.draw_v56(view, x=atp.x, y=atp.y, z=atp.z,
                                                                              mirror=mirror, transparent=transparent,
                                                                              polygon=polygon)
        atp.loop = 0
        atp.cell = 0
        atp.im_id = im_id
        atp.images = images
        atp.canvas_coords = coords
        atp.mirror = mirror
        atp.v56 = v56
        atp.x, atp.y, atp.z = world_cords
        self.room_canvas.addtag_withtag(add_tag, im_id)
        self.active_room.active_views.append(atp)
        self.active_room.view_from_image[im_id] = atp

    def log_to_display(self, text: str):
        print(text)

    def draw_object(self, obj):
        add_tag = 'object'
        loop = (int(obj.loop) if obj.loop else 0)
        view_num = self.stk_objs[obj.object_class].view

        try:
            view = self.get_view_resource(view_num)
        except KeyError:
            self.log_to_display(f"View ({view_num}) missing for OBJ \"{obj.name}\"")
            return

        im_id, images, coords, loop, mirror, v56, world_cords = self.draw_v56(view, loop=loop, x=obj.x, y=obj.y)
        obj.im_id = im_id
        obj.images = images
        obj.canvas_coords = coords
        obj.loop = loop
        obj.v56 = v56
        obj.x, obj.y, obj.z = world_cords
        self.room_canvas.addtag_withtag(add_tag, im_id)
        self.active_room.active_views.append(obj)
        self.active_room.view_from_image[im_id] = obj

    def get_view_resource(self, view_num):
        view = self.get_resource(ResType.view, view_num)
        if view is None:
            view = self.resources['v56'][str(view_num)]
        return view

    def get_pic_resource(self, pic_num):
        pic = self.get_resource(ResType.pic, pic_num)
        if pic is None:
            pic = self.resources['p56'][str(pic_num)]
        return pic

    def open_wld(self, filename):
        if filename is None:
            return
        world = WldInterp.World(filename)
        self.world = world
        self.save_file = filename
        self.set_rooms()

    def load_room(self, room: Room, reset: bool = False):
        if reset and self.active_room is not None:
            self.active_room.active_views = []
        map_canvas = self.widgets[self.map_frame]['map_canvas']
        buttons = self.widgets[self.map_frame][map_canvas]
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
        if self.map_frame in self.widgets.keys():
            if 'map_canvas' in self.widgets[self.map_frame].keys():
                # TOOD: what??
                map_canvas = self.widgets[self.map_frame]['map_canvas']
                if map_canvas in self.widgets[self.map_frame].keys():
                    for room_num, map_button in self.widgets[self.map_frame][map_canvas].items():
                        if room_num == 'potential_rooms':
                            for potential_room in map_button:
                                potential_room.grid_forget()
                        else:
                            map_button.grid_forget()

    def create_new_room(self, button_index, row, col):
        # Get the map frame
        map_canvas = self.widgets[self.map_frame]['map_canvas']
        # Find all Adjacent rooms
        adjacent_rooms = {'West': (row, col - 1), 'East': (row, col + 1), 'North': (row - 1, col),
                          'South': (row + 1, col)}
        empty_grid = []
        for direction, grid_coords in adjacent_rooms.items():
            adjacent_rooms[direction] = None
            widgets_on_grid = map_canvas.grid_slaves(grid_coords[0], grid_coords[1])
            if len(widgets_on_grid) > 0:
                if widgets_on_grid[0].room_id is not None:
                    adjacent_rooms[direction] = widgets_on_grid[0]
            else:
                empty_grid.append(grid_coords)
        # Calculate room number, set old room exits, get this rooms exits, get reference room info
        exits = {'north': None, 'east': None, 'south': None, 'west': None}
        reference_room = None
        room_num = None
        for direction in ['West', 'East', 'North', 'South']:
            room_button = adjacent_rooms[direction]
            if room_button:
                if direction == 'West':
                    room_num = (int(room_button.room_id) + 1 if room_num is None else room_num)
                    adj_room = self.rooms[room_button.room_id]
                    adj_room.properties['exits']['east'] = room_num
                    reference_room = (adj_room if reference_room is None else reference_room)
                    exits['west'] = room_button.room_id
                elif direction == 'East':
                    room_num = (int(room_button.room_id) - 1 if room_num is None else room_num)
                    adj_room = self.rooms[room_button.room_id]
                    adj_room.properties['exits']['west'] = room_num
                    reference_room = (adj_room if reference_room is None else reference_room)
                    exits['east'] = room_button.room_id
                elif direction == 'North':
                    room_num = (int(room_button.room_id) + 10 if room_num is None else room_num)
                    adj_room = self.rooms[room_button.room_id]
                    adj_room.properties['exits']['south'] = room_num
                    reference_room = (adj_room if reference_room is None else reference_room)
                    exits['north'] = room_button.room_id
                elif direction == 'South':
                    room_num = (int(room_button.room_id) - 10 if room_num is None else room_num)
                    adj_room = self.rooms[room_button.room_id]
                    adj_room.properties['exits']['north'] = room_num
                    reference_room = (adj_room if reference_room is None else reference_room)
                    exits['south'] = room_button.room_id
        buttons = self.widgets[self.map_frame][map_canvas]
        if room_num in buttons.keys():
            max_num = -1
            for x in self.widgets[self.map_frame][map_canvas].keys():
                try:
                    max_num = max(max_num, int(x))
                except:
                    continue
            room_num = max_num + 1
        old_map_button = buttons['potential_rooms'][button_index]
        old_map_button.grid_forget()
        ## Create a new room object, add to self.rooms
        new_room = Room()
        new_room.number = room_num
        new_room.picture = (
            reference_room.picture if reference_room.active_background is None else reference_room.active_background)
        new_room.properties["picture"] = new_room.picture
        new_room.properties['exits'] = exits
        self.rooms[room_num] = new_room
        self.world.rooms += [new_room]
        ## create a map button for the room
        map_button = MapButton(map_canvas, room_num, width=5, height=1, background='LightCyan3', text=str(room_num),
                               highlightcolor='black',
                               command=lambda: self.load_room(self.rooms[new_room.number]))
        map_button.bind('<Button-3>', lambda x: self.map_popup_menu(x, map_button))
        map_button.grid(row=row, column=col)
        buttons[room_num] = map_button
        self.load_room(new_room)
        # Add the new_room buttons are any new rooms
        for grid_coord in empty_grid:
            # This probably won't always work. If it creates a possible new room in a place where a room exits from a
            #   different WLD file, this should break things. I'll need to set up a global room manager at some point...
            # TODO: global room manager for all WLD files.
            # TODO: pic a p56 file
            # TODO: add a room number (How to know it's not taken?)
            self.add_potential_room(grid_coord[0], grid_coord[1])

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
        adjacent_rooms = [self.rooms[int(x)] for x in room.properties['exits'].values() if
                          x is not None and int(x) in self.rooms.keys()]
        map_canvas = self.widgets[self.map_frame]['map_canvas']
        button_dict = self.widgets[self.map_frame][map_canvas]
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
            tk.Label(self.top, text='{} :'.format(direction)).grid(row=i + 1, column=0)
            dir_entry = tk.Entry(self.top, justify=tk.RIGHT)
            dir_entry.grid(row=i + 1, column=1, columnspan=2)
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
                        raise (e)
                else:
                    entry = None
                room.properties['exits'][k] = entry

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
                room.picture = pic
                room.properties["picture"] = pic
                app.load_room(room)
            else:
                room.active_background = picture
                app.load_room(room)

        if picture is None:
            self.top = tk.Toplevel()
            header = tk.Label(self.top, text='Select a P56')
            header.pack(fill=tk.X)
            listbox = tk.Listbox(self.top)
            listbox.pack(fill=tk.BOTH, expand=1)
            listbox.bind('<Double-Button-1>', lambda x: callback(self))
            resources: list[Ressci] = self.resources["resources"].values()
            pic_nums_from_res = []
            for x in resources:
                pics: dict[Ressci.Resource] = x.resource_map[ResType.pic]
                pic_nums_from_res += [k for k, v in pics.items()]
            pic_nums_from_p56 = [int(p) for p in self.resources['p56'].keys()]
            for pic in pic_nums_from_p56 + pic_nums_from_res:
                try:
                    if pic in self.pics.keys():
                        pic_info = self.pics[pic]
                        listbox.insert(tk.END, '{}_{}'.format(pic_info.room_type, pic))
                except Exception as e:
                    print(f"Picture not found {e}")
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
                print(f"Error deleting room: {e}")
            # update the button key
            map_canvase = self.widgets[self.map_frame]['map_canvas']
            self.widgets[self.map_frame][map_canvase][new_room_number] = map_button
            try:
                del self.widgets[self.map_frame][map_canvase][room.number]
            except Exception as e:
                print(f"Error removing room button: {e}")
            # update the room number in the room object
            room.number = new_room_number
            # Update the button text
            map_button.configure(text=new_room_number)
            map_button.room_id = new_room_number

        tk.Button(self.top, text='OK', command=lambda: callback(self, new_room_number)).grid(row=1, column=1)

    def add_potential_room(self, row, col):
        map_canvas = self.widgets[self.map_frame]['map_canvas']
        buttons = self.widgets[self.map_frame][map_canvas]
        if 'potential_rooms' not in buttons.keys():
            buttons['potential_rooms'] = []
        button_index = len(buttons['potential_rooms'])
        new_map_button = MapButton(map_canvas, None, width=5, height=1, background='ivory2', highlightcolor='black',
                                   text='New', command=lambda: self.create_new_room(button_index, row, col))
        new_map_button.grid(row=row, column=col)
        buttons['potential_rooms'].append(new_map_button)

    def draw_map(self, room_num=None, direction=None, row=1000, col=1000, terminate=False):
        '''
        TODO: add map buttons to a 2D list [][] (maybe just 1000x1000) and always add the next
            free-floating (no exits) room to the closes available spot to [0,0].
            If something needs to be added to an existing cell, move all existing
            widgets at that row or column down or over
            (probably not that simple :( )
        '''

        map_canvas: tkinter.Canvas = self.widgets[self.map_frame]['map_canvas']
        map_canvas.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        if not (room_num or terminate):
            buttons = self.widgets[self.map_frame][map_canvas] = {}
            first_room_num = list(self.rooms.keys())[0]
            room = self.rooms[first_room_num]
            self.active_room = None
            map_button = MapButton(map_canvas, first_room_num, width=5, height=1, background='LightCyan3',
                                   text=str(first_room_num), highlightcolor='black',
                                   command=lambda: self.load_room(self.rooms[room.number]))
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
                    row += 20
                    if row % 40 == 0:
                        col += 20
                        row -= 40
                    self.draw_map(next_room_num, row=row, col=col)
        else:
            buttons = self.widgets[self.map_frame][map_canvas]
            if direction:
                side_dict = {'north': (-1, 0), 'south': (1, 0), 'east': (0, 1), 'west': (0, -1)}
                row, col = row + side_dict[direction][0], col + side_dict[direction][1]
            if len(map_canvas.grid_slaves(row, col)) > 0:
                return
            if terminate:
                if 'potential_rooms' not in buttons.keys():
                    buttons['potential_rooms'] = []
                button_index = len(buttons['potential_rooms'])
                map_button = MapButton(map_canvas, None, width=5, height=1, background='ivory2', highlightcolor='black',
                                       text='New', command=lambda: self.create_new_room(button_index, row, col))
                map_button.grid(row=row, column=col)
                buttons['potential_rooms'].append(map_button)
            elif room_num in self.rooms.keys() and room_num not in buttons.keys():
                room = self.rooms[room_num]
                map_button = MapButton(map_canvas, room_num, width=5, height=1, background='LightCyan3',
                                       highlightcolor='black', text=str(room_num),
                                       command=lambda: self.load_room(self.rooms[room.number]))
                map_button.bind('<Button-3>', lambda x: self.map_popup_menu(x, map_button))
                map_button.grid(row=row, column=col)
                buttons[room_num] = map_button
                for direction, exit in self.rooms[room_num].properties['exits'].items():
                    if exit and exit in self.rooms.keys() and exit not in buttons.keys():
                        self.draw_map(exit, direction, row, col)
                    elif not exit:
                        self.draw_map(exit, direction, row, col, terminate=True)

    def create_scrollable_canvas(self, frame):
        canvas = tk.Canvas(frame)
        # h_scrollbar = ttk.Scrollbar(frame, orient="horizontal", command=canvas.xview)
        # v_scrollbar = ttk.Scrollbar(frame, orient="vertical", command=canvas.yview)
        # scrollable_frame = ttk.Frame(canvas)
        #
        # scrollable_frame.bind("<Configure>",
        #                       lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
        #
        # canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        # canvas.configure(xscrollcommand=h_scrollbar.set, yscrollcommand=v_scrollbar.set)
        #
        # h_scrollbar.pack(side="bottom", fill="x")
        # v_scrollbar.pack(side="right", fill="y")
        canvas.pack(side="left", fill="both", expand=True)

        return canvas

    def set_rooms(self):
        self.clear_current_rooms()
        self.rooms = {r.number: r for r in self.world.rooms}
        if self.map_frame in self.widgets.keys():
            if 'map_canvas' in self.widgets[self.map_frame].keys():
                map_canvas = self.widgets[self.map_frame]['map_canvas']
            else:
                map_canvas = self.create_scrollable_canvas(self.map_frame)
        else:
            map_canvas = self.create_scrollable_canvas(self.map_frame)

        self.widgets[self.map_frame] = {}
        self.widgets[self.map_frame]['map_canvas'] = map_canvas
        self.draw_map()
        first_room_number = self.world.rooms[0].number
        self.load_room(self.rooms[first_room_number])
        self.widgets[self.map_frame][map_canvas][first_room_number].configure(background='PaleTurquoise2')
        self.update()

    def open_sci_file(self, filename=None):
        if not filename:
            filename = filedialog.askopenfilename()
        name, extension = os.path.splitext(filename)
        if extension.lower() not in ['.v56', '.p56', '.wld']:
            self.errorbox('Extension {} is not a SCI filetype'.format(extension))
            raise (Exception('Not a SCI File: {}'.format(extension)))
        elif extension.lower() == '.wld':
            self.open_wld(filename)
        elif extension.lower() == '.v56':
            # v56 = V56file(filename)
            v56 = View.from_file(filename)
            self.draw_v56(v56)
        elif extension.lower() == '.p56':
            p56 = Picture.from_file(filename)
            self.set_background(p56)
        else:
            self.load_packed_resource(filename)

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
        if not self.view_found_in_resources(view_id):
            return None, mirror
        view = self.get_view_resource(view_id)
        return view, mirror

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
            template_room_wld_file = self.resources['wld'][self.room_directory[template_room_num]]
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
        pic_res = self.get_pic_resource(int(pic))
        self.set_background(pic_res)
        if len(self.active_room.active_views) > 0:
            depth_sorted_atps_objs = [[int(atp_or_obj.y), atp_or_obj] for atp_or_obj in room.active_views]
            room.active_views = []
        else:
            depth_sorted_atps_objs = [[int(atp_or_obj.y), atp_or_obj] for atp_or_obj in room.atpinfo + room.objects]
        depth_sorted_atps_objs.sort(key=lambda x: x[0])
        for atp_or_obj_info in depth_sorted_atps_objs:
            atp_or_obj = atp_or_obj_info[1]
            if isinstance(atp_or_obj, ATP):
                atp = atp_or_obj
                try:
                    self.draw_atp(atp)
                except KeyError as e1:
                    print(f"Error drawing atp: {e1}")
                    continue
            elif isinstance(atp_or_obj, WorldObject):
                obj = atp_or_obj
                try:
                    self.draw_object(obj)
                except KeyError as e2:
                    self.errorbox(f"Error drawing object: [{obj}] with view [{e2}]")
                    continue

        # Hide the polygons, by default
        self.polygon_state = 'normal'
        self.toggle_polygons()
        self.update()


if __name__ == '__main__':
    try:
        w = WorldCreator(atp_categories=ATP_CATEGORIES, pic_info=PIC_INFO, object_info=stkObjDict)
    except Exception as e:
        raise (e)
