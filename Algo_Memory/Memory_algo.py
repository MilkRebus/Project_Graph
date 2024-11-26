from collections import deque

from Algo_Memory.Memory import *
from Algo_Memory.element_mark_algo import Mark_element_algo


class Memory(Mark_element_algo):
    def __init__(self):
        super(Memory, self).__init__()
        self.section = {"Arrow": Arrow(), "Top": Top(), "Loop": Loop(), "Stick": Stick()}
        self.opposites = {"Arrow": "Stick", "Stick": "Arrow"}
        self.cancellation = deque()
        self.recovery = deque()

    def replay(self, name):
        if name not in ("Arrow", "Stick") or (
                not (self.section[name].get_cord_element() in self.section[self.opposites[name]].get_dict() or
                     self.section[name].get_cord_element()[::-1] in self.section[self.opposites[name]].get_dict())):
            return True
        else:
            return False

    def save_text(self, text, key, name):
        self.section[name].save_text(key, text)

    def clear_memory(self):
        self.pop_marked_items()
        for element in self.section.values():
            element.clear()
        self.light_path = set()
        self.recovery.clear()
        self.cancellation.clear()

    def clear_flag(self):
        self.section["Stick"].clear_last_point()
        self.section["Arrow"].clear_last_point()
        self.section["Loop"].clear_last_point()

    def add_element(self, key, item, name):
        self.recovery.clear()
        self.section[name].add_node(key, item)
        self.section["Top"].correct_edge(key, name)
        self.cancellation.append(("add", [(name, key, self.section[name].get_value(key))]))

    def get_cord_element(self, name):
        return self.section[name].get_cord_element()

    def organize_element(self, name, colliding_arr, cord=None):
        self.section[name].organize_element(colliding_arr, cord)

    def delete_element(self, key, name):
        self.recovery.clear()
        elements = self.related_element(key, name)
        self.cancellation.append(("delete", elements))
        return [item[2]["render"]["item"] for item in elements]

    def related_element(self, key, name):
        arr_element = [(name, key, self.section[name].get_value(key))]
        if name == "Top":
            elements = self.section[name].get_edges(key)
            for name_element, key_element in elements:
                arr_element.append((name_element, key_element, self.section[name_element].get_value(key_element)))
                self.section[name_element].pop(key_element)
                self.section[name].delete_edge(key_element, name_element)
        else:
            self.section["Top"].delete_edge(key, name)
        self.section[name].pop(key)
        return arr_element

    def refunding(self):
        elements = self.cancellation.pop()
        self.recovery.append(elements)
        for name, key, value in elements[1]:
            if elements[0] == "delete":
                self.section[name].add_node(key, None, value)
                self.section["Top"].correct_edge(key, name)
            else:
                self.section[name].pop(key)
                self.section["Top"].delete_edge(key, name)
        return elements[0], [item[2]["render"]["item"] for item in elements[1]]

    def recovering(self):
        elements = self.recovery.pop()
        self.cancellation.append(elements)
        if elements[0] == "add":
            for name, key, value in elements[1]:
                self.section[name].add_node(key, None, value)
                self.section["Top"].correct_edge(key, name)
        else:
            for name, key, value in elements[1][::-1]:
                self.section[name].pop(key)
                self.section["Top"].delete_edge(key, name)
        return elements[0], [item[2]["render"]["item"] for item in elements[1]]

    def get_mark_item(self):
        return self.section["Top"].dict_top[super(Memory, self).get_marked_item()]["render"]["item"]

    def get_graph(self):
        return {name: self.section[name].get_dict() for name in self.section.keys()}

    def set_lighted_path(self, path):
        super(Memory, self).set_lighted_path(path, self.section)

    def pop_marked_items(self):
        if len(self.marked_element) != 0:
            items = []
            for type_name, dict_section in self.marked_element.items():
                for section_name, item in dict_section.items():
                    for name, key in item.items():
                        if key is not None:
                            items.append(self.section[section_name].get_item(key))
                            self.marked_element[type_name][section_name][name] = None
            return items