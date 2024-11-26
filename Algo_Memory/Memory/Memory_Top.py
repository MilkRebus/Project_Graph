from Config import color_top


class Top:
    def __init__(self):
        self.dict_top = {}
        self.opposites = {"in": "out", "out": "in"}
        self.cord_element = None

    def save_text(self, key, text):
        if text != "":
            if text.replace(".", "", 1).isdigit() or (
                    text[0] == "-" and text.translate({ord(i): None for i in '.-'}).isdigit()):
                self.dict_top[key]["algo"]["weight"] = float(text)
                self.dict_top[key]["algo"]["name"] = None
            else:
                self.dict_top[key]["algo"]["name"] = text
                self.dict_top[key]["algo"]["weight"] = None
        else:
            self.dict_top[key]["algo"]["name"] = None
            self.dict_top[key]["algo"]["weight"] = None

    def correct_edge(self, key, name):
        if name == "Loop": key = (key[0], key[0])
        if name != "Top":
            self.dict_top[key[0]]["render"]["All_Edge"].add((name, key))
            self.dict_top[key[1]]["render"]["All_Edge"].add((name, key))
        if name == "Loop": name = "Arrow"
        if name == "Arrow":
            self.dict_top[key[0]]["algo"][name]["out"][key[1]] = None
            self.dict_top[key[1]]["algo"][name]["in"][key[0]] = None
        if name == "Stick":
            self.dict_top[key[0]]["algo"][name][key[1]] = None
            self.dict_top[key[1]]["algo"][name][key[0]] = None

    def organize_element(self, colliding_arr, cord):
        self.cord_element = None
        if len(colliding_arr) == 0:
            self.cord_element = cord

    def delete_edge(self, key, name):
        if name != "Top":
            if name == "Loop": key = (key[0], key[0])
            self.dict_top[key[0]]["render"]["All_Edge"].remove((name, key))
            if name != "Loop":
                self.dict_top[key[1]]["render"]["All_Edge"].remove((name, key))
            if name == "Loop": name = "Arrow"
            if name == "Arrow":
                self.dict_top[key[0]]["algo"][name]["out"].pop(key[1])
                self.dict_top[key[1]]["algo"][name]["in"].pop(key[0])
            if name == "Stick":
                self.dict_top[key[0]]["algo"][name].pop(key[1])
                self.dict_top[key[1]]["algo"][name].pop(key[0])

    def add_node(self, key, item, value=None):
        if value is not None:
            self.dict_top[key] = value
        else:
            self.dict_top[key] = {"render": {"color": color_top,
                                             "item": item,
                                             "type": "Top",
                                             "All_Edge": set()},
                                  "algo": {"name": None, "weight": None,
                                           "Arrow": {"in": {}, "out": {}},
                                           "Stick": {}}
                                  }

    def get_edges(self, key):
        return [element for element in self.dict_top[key]["render"]["All_Edge"]]

    def get_item(self, key):
        return self.dict_top[key]["render"]["item"]

    def pop(self, key):
        self.dict_top.pop(key)

    def get_value(self, key):
        return self.dict_top[key]

    def clear(self):
        self.dict_top.clear()
        self.cord_element = None

    def get_cord_element(self):
        return self.cord_element

    def empety(self):
        if len(self.dict_top) > 0:
            return False
        else:
            return True

    def get_dict(self):
        return {name: self.dict_top[name] for name in self.dict_top.keys()}
