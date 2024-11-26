class Mark_element_algo():
    def __init__(self):
        self.color_mark = {}
        self.mark_name = None
        self.marked_element = {}
        self.light_path = None
        self.mark_type = None
        self.color_path = "green"
        self.cleared_path = None

    def set_mark_name(self, node):
        self.mark_name, self.mark_type = node

    def set_dict_marked_element(self, dict_element):
        self.marked_element = dict_element

    def add_mark(self, key):
        self.marked_element[self.mark_type[0]][self.mark_type[1]][self.mark_name] = key

    def check_ident_mark(self):
        if self.mark_type[1] in self.marked_element[self.mark_type[0]]:
            return self.mark_name in self.marked_element[self.mark_type[0]][self.mark_type[1]] and \
                   self.marked_element[self.mark_type[0]][self.mark_type[1]][self.mark_name] is not None
        else:
            return False

    def delete_mark(self, name_mark):
        self.marked_element[name_mark[1][0]][name_mark[1][1]][name_mark[0]] = None

    def get_helped(self):
        return self.marked_element

    def get_marked_item(self):
        key = self.marked_element[self.mark_type[0]][self.mark_type[1]][self.mark_name]
        return key

    def set_color_mark(self, dict):
        self.color_mark = dict

    def replay_mark(self, key):
        if self.marked_element[self.mark_type[0]][self.mark_type[1]][self.mark_name] != key:
            return True
        else:
            self.marked_element[self.mark_type[0]][self.mark_type[1]][self.mark_name] = None
            return False

    def get_color_mark(self):
        return self.color_mark[self.mark_name]

    def set_lighted_path(self, path, section):
        self.cleared_path = self.light_path
        if path is not None:
            self.light_path = set()
            self.color_path = "green" if len(path) == 2 else path[2]
            type_edge = path[1]
            path = path[0]
            last_node = path[0]
            for node in range(1, len(path)):
                node = path[node]
                self.light_path.add(section[type_edge].get_item((node, last_node)))
                self.light_path.add(section["Top"].get_item(node))
                last_node = node
            self.light_path.remove(section["Top"].get_item(last_node))
            if self.cleared_path is None:
                self.cleared_path = self.light_path
        else:
            self.light_path = None

    def get_lighted_item(self):
        return self.light_path

    def get_cleared_path(self):
        return self.cleared_path

    def clear_mark(self):
        self.marked_element = {}
        self.color_mark = {}
        self.mark_name = None
