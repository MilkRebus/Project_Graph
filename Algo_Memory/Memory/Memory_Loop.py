from Config import *


class Loop:
    def __init__(self):
        self.dict_loop = {}
        self.last_cord_loop = None
        self.cord_element = None

    def search_top(self, arr):
        for item in arr:
            if item.name == "Top":
                return item.get_cord()
        return None

    def save_text(self, key, text):
        if len(key) > 1: key = key[0]
        if text != "":
            if (text[0] == "-" and len(text) == 1) or text in ("-.", "."):
                self.dict_loop[key]["algo"]["weight"] = 0
            else:
                self.dict_loop[key]["algo"]["weight"] = float(text)
        else:
            self.dict_loop[key]["algo"]["weight"] = None

    def organize_element(self, colliding_arr, cord_click):
        self.cord_element = None
        new_loop = self.search_top(colliding_arr)
        if new_loop is not None:
            if self.last_cord_loop is None and not (new_loop in self.dict_loop) and self.last_cord_loop != new_loop:
                self.last_cord_loop = new_loop
            else:
                self.last_cord_loop = None
        else:
            if self.last_cord_loop is not None:
                self.cord_element = (self.last_cord_loop, cord_click)
            self.last_cord_loop = None

    def add_node(self, key, item, value=None):
        if len(key) > 1: key = key[0]
        if value is not None:
            self.dict_loop[key] = value
        else:
            self.dict_loop[key] = {"render": {"color": color_top, "item": item, "type": "Loop"},
                                   "algo": {"weight": None}
                                   }

    def get_value(self, key):
        if len(key) > 1: key = key[0]
        return self.dict_loop[key]

    def clear_last_point(self):
        self.last_cord_loop = None

    def pop(self, key):
        if len(key) > 1: key = key[0]
        self.dict_loop.pop(key)

    def clear(self):
        self.dict_loop.clear()
        self.last_cord_loop = None
    def get_item(self, key):
        return self.dict_loop[key]["render"]["item"]

    def get_cord_element(self):
        return self.cord_element

    def get_dict(self):
        return {name: self.dict_loop[name] for name in self.dict_loop.keys()}
