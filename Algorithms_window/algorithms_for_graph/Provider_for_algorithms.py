from .algorithms import *


class Provider:
    def __init__(self, Memory):
        self.Memory = Memory
        self.answer = None
        self.path = None
        self.parameter_for_algo = {"Graph": ["Weight graph", "Oriented graph", "Light path"]}
        self.dict_algorithms = {"Bellman_Ford": Bellman_Ford_Algorithm(), "Deikstr": Deikstr_Algorithm(),
                                "Negative_cycle": Negative_cycle(), "Number of paths": NumberPaths_Algorithm()}

    def calculate_algorithm(self, info):
        if info["name"] is not None:
            self.dict_algorithms[info["name"]].calculate(info)
            self.answer = self.dict_algorithms[info["name"]].answer
            self.answer = self.answer if len(self.answer) > 0 else None
            self.path = self.dict_algorithms[info["name"]].path

    def get_info_algo(self, name):
        dict_info = dict()
        for type_mark, dict_mark in self.dict_algorithms[name].info.items():
            if type_mark not in dict_info:
                dict_info[type_mark] = dict()
            for type_element, dict_name in dict_mark.items():
                if type_element not in dict_info:
                    dict_info[type_mark][type_element] = dict()
                for name in dict_name.keys():
                    dict_info[type_mark][type_element][name] = None
        return dict_info

    def get_bt_info(self, name):
        name_button = {}
        if self.dict_algorithms[name].info is not None:
            for mark_type, section in self.dict_algorithms[name].info.items():
                for section_bt, marks in section.items():
                    for name_bt, color_bt in marks.items():
                        name_button[name_bt] = (mark_type, section_bt), color_bt
        return name_button

    def get_color_mark(self, name):
        name_button = {}
        for mark_type in self.dict_algorithms[name].info.values():
            for section_bt in mark_type.values():
                for name_bt in section_bt.keys():
                    name_button[name_bt] = section_bt[name_bt]
        return name_button

    def get_path(self):
        return self.path

    def get_answer(self):
        return self.answer
