import tkinter as tk


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