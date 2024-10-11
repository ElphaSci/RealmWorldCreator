import tkinter as tk
from tkinter import ttk

import atp_info
import stock_objects


def convert_to_dict(top_info):
    categories = {}
    for item in top_info:
        if ':' in item:
            item_list = item.split(':')
            key = item_list[0]
            value = item_list[1:]
            if len(value) > 1:
                new_dict = {key: {}}
                categories = {**categories, **new_dict}
                convert_to_dict(':'.join(value))
            else:
                if key in categories.keys():
                    categories[key].append(value[0].strip())
                else:
                    categories[key.strip()] = [value[0].strip()]
        else:
            categories[item] = None
    return categories


class ViewCategoriesTreeView(ttk.Treeview):

    def __init__(self, parent, categories, **kw):

        super().__init__(parent, selectmode='browse', **kw)
        self.category_items = {}
        if isinstance(categories, list):
            self.categories = convert_to_dict(categories)
        else:
            self.categories = categories

    def reset_view_categories(self):
        self.set_children("")
        self.category_items = {}
        self.add_categories(self.categories)
        self.category_items = self.category_items[""] if "" in self.category_items else self.category_items

    def add_categories(self, categories: dict, parent=""):
        for (k, v) in categories.items():
            if v is not None:

                if isinstance(v, atp_info.ATPNode):
                    self.insert(parent, 'end', None, text=self.format_atp_name(v), values=[v.number, 'atp'])
                    continue
                elif isinstance(v, stock_objects.StockObject):
                    self.insert(parent, 'end', None, text=f"{v.name} ({v.pName})", values=[v.name, 'obj'])
                    continue

                item = self.insert(parent, 'end', text=k)
                if type(v) is list:

                    for x in v:
                        if isinstance(x, dict):
                            self.add_categories(x, item)
                        elif isinstance(x, atp_info.ATPNode):
                            self.insert(item, 'end', None, text=self.format_atp_name(x), values=[x.number, 'atp'])
                        elif isinstance(x, stock_objects.StockObject):
                            self.insert(item, 'end', None, text=f"{x.name} ({x.pName})", values=[x.name, 'obj'])
                elif type(v) is dict:
                    self.add_categories(v, item)

    def format_atp_name(self, atp: atp_info.ATPNode) -> str:
        if atp.pDescriber and atp.noun:
            return f"{atp.pDescriber} {f'({atp.noun})' if atp.noun != '0' else ''}"
        if atp.pDescriber:
            return atp.pDescriber
        elif atp.noun:
            return atp.noun
        else:
            return f'{atp.number}'


class NestedOptionMenu(tk.Frame):

    def __init__(self, app, parent, top_info, callback=None):
        tk.Frame.__init__(self, parent)
        self.callback = callback
        self.app = app
        if isinstance(top_info, list):
            self.top_info = convert_to_dict(top_info)
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
            alphabetical_info = [[k, v] for k, v in top_info.items()]
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
            first_key = sorted(list(top_info.keys()))[0]
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


class ResourcePathList(tk.Listbox):

    def __init__(self):
        pass
class ScrollableFrame(ttk.Frame):
    def __init__(self, container, *args, **kwargs):
        super().__init__(container, *args, **kwargs)
        canvas = tk.Canvas(self)
        scrollbar = ttk.Scrollbar(self, orient="vertical", command=canvas.yview)
        h_scrollbar = ttk.Scrollbar(self, orient="horizontal", command=canvas.xview)
        self.scrollable_frame = ttk.Frame(canvas)

        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(
                scrollregion=canvas.bbox("all")
            )
        )

        canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        canvas.configure(xscrollcommand=h_scrollbar.set, yscrollcommand=scrollbar.set)

        h_scrollbar.pack(side="bottom", fill="x")
        scrollbar.pack(side="right", fill="y")
        canvas.pack(side="left", fill="both", expand=True)