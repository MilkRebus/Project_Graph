from Config import *


class Arrow:
    def __init__(self):
        self.dict_arrow = {}
        self.last_cord_arrow = None
        self.cord_element = None

    def search_top(self, arr):
        for item in arr:
            if item.name == "Top":
                return item.get_cord()
        return None

    def save_text(self, key, text):
        if text != "":
            if (text[0] == "-" and len(text) == 1) or text in ("-.", "."):
                self.dict_arrow[key]["algo"]["weight"] = 0
            else:
                self.dict_arrow[key]["algo"]["weight"] = float(text)
        else:
            self.dict_arrow[key]["algo"]["weight"] = None

    def organize_element(self, colliding_arr, cord=None):
        self.cord_element = None
        new_top = self.search_top(colliding_arr)
        if new_top is not None:
            if self.last_cord_arrow is not None and self.last_cord_arrow != new_top:
                key = tuple([self.last_cord_arrow, new_top])
                if (key[1], key[0]) in self.dict_arrow and not (key in self.dict_arrow):
                    self.remake_arrow((key[1], key[0]))
                if key not in self.dict_arrow:
                    self.cord_element = key
                    self.last_cord_arrow = None
            else:
                self.last_cord_arrow = new_top
        else:
            self.last_cord_arrow = None

    def remake_arrow(self, key):
        self.dict_arrow[key]["render"]["item"].remake()

    def add_node(self, key, item, value=None):
        #print(key)
        if value is not None:
            self.dict_arrow[key] = value
            if key[::-1] in self.dict_arrow and value["render"]["item"].state == "only":
                self.remake_arrow(key)
            elif key[::-1] in self.dict_arrow:
                self.remake_arrow(key[::-1])
        elif key not in self.dict_arrow:

            self.dict_arrow[key] = {"render": {"color": color_top, "item": item, "type": "Arrow"},
                                    "algo": {"weight": None}
                                    }
            if key[::-1] in self.dict_arrow:
                #print("remake two")
                self.remake_arrow(key)

    def get_value(self, key):
        return self.dict_arrow[key]

    def get_item(self, key):
        return self.dict_arrow[key]["render"]["item"]

    def clear(self):
        self.dict_arrow.clear()
        self.last_cord_arrow = None

    def clear_last_point(self):
        self.last_cord_arrow = None

    def pop(self, key):
        if key[::-1] in self.dict_arrow:
            self.remake_arrow(key[::-1])
        self.dict_arrow.pop(key)

    def get_cord_element(self):
        return self.cord_element

    def get_dict(self):
        return {name: self.dict_arrow[name] for name in self.dict_arrow.keys()}
