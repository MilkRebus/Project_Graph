from Config import *


class Stick:
    def __init__(self):
        self.last_cord_stick = None
        self.cord_element = None
        self.dict_stick = {}

    def search_top(self, arr):
        for item in arr:
            if item.name == "Top":
                return item.get_cord()
        return None

    def clear_flag(self):
        self.last_cord_stick = None

    def save_text(self, key, text):
        key = frozenset({key[0], key[1]})
        if text != "":
            if (text[0] == "-" and len(text) == 1) or text in ("-.", "."):
                self.dict_stick[key]["algo"]["weight"] = 0
            else:
                self.dict_stick[key]["algo"]["weight"] = float(text)
        else:
            self.dict_stick[key]["algo"]["weight"] = None

    def organize_element(self, colliding_arr, cord=None):
        self.cord_element = None
        new_cord = self.search_top(colliding_arr)
        if new_cord is not None:
            if self.last_cord_stick is not None and self.last_cord_stick != new_cord:
                key = tuple([self.last_cord_stick, new_cord])
                if frozenset({key[0], key[1]}) not in self.dict_stick:
                    self.cord_element = key
            else:
                self.last_cord_stick = None
        else:
            self.last_cord_stick = None
        self.last_cord_stick = new_cord

    def add_node(self, key, item, value=None):
        key = frozenset({key[0], key[1]})
        if value is not None:
            self.dict_stick[key] = value
        else:
            self.dict_stick[key] = {"render": {"color": color_top, "item": item, "type": "Stick"},
                                    "algo": {"weight": None}
                                    }

    def get_value(self, key):
        return self.dict_stick[frozenset({key[0], key[1]})]

    def pop(self, key):
        self.dict_stick.pop(frozenset({key[0], key[1]}))

    def clear_last_point(self):
        self.last_cord_stick = None

    def clear(self):
        self.dict_stick.clear()
        self.last_cord_stick = None

    def get_cord_element(self):
        return self.cord_element

    def get_dict(self):
        return {name: self.dict_stick[name] for name in self.dict_stick.keys()}

    def get_item(self, key):
        return self.dict_stick[frozenset(key)]["render"]["item"]

    def get_item_element(self, key):
        return self.dict_stick[frozenset(key)]["render"]["item"]
