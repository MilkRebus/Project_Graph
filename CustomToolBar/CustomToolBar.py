from PyQt6.QtCore import pyqtSignal
from PyQt6.QtWidgets import QLabel

from Config import *
from CustomToolBar.ImButton import ImageButton
from CustomToolBar.LabelGroup import Group


class ReadyToolBar(QLabel):
    clicked = pyqtSignal()
    tap = pyqtSignal()

    def __init__(self, parent=None):
        super(ReadyToolBar, self).__init__(parent)
        self.num = len(arr_name_button)
        self.depth_button = 1
        self.state = None
        self.tap = None
        self.sticking_button = None
        self.resize(size_button * 2, size_button)
        self.dict_button = {}
        self.dict_groups = {}
        self.flag = False
        self.init_button()
        self.connect_func()

    def init_button(self):
        for index in range(self.num):
            name = arr_name_button[index]
            if type(name) is tuple:
                if len(name) > self.depth_button:
                    self.depth_button = len(name[1])
                element = Group(size_button, name[1], self)
                self.dict_button = self.dict_button | element.get_button()
                self.dict_groups[name[0]] = element
                self.connect_resize(element)
            else:
                element = ImageButton(size_button, name, setting_button[name], self)
                self.dict_button[name] = element
            element.move(index * size_button, 0)

    def condition(self):
        if self.flag:
            self.flag = False
            self.resize(size_button * 2, size_button)
        else:
            self.flag = True
            self.resize(size_button * self.num, size_button)

    def connect_resize(self, element):
        element.entered.connect(self.wider)
        element.leaved.connect(self.narrower)

    def wider(self):
        self.resize(size_button * self.num, size_button * self.depth_button)

    def narrower(self):
        self.resize(size_button * self.num, size_button)

    def connect_func(self):
        self.dict_button["Tools"].clicked.connect(self.condition)

    def mouseDoubleClickEvent(self, a0):
        pass

    def clear(self):
        if self.sticking_button is not None:
            self.sticking_button.change_style()
            self.sticking_button = None
        self.state = None

    def restate(self, state):
        if state["type"] == "sticking":
            if self.state == state:
                state = None
                self.sticking_button = None
            else:
                if not (self.sticking_button is None or self.sticking_button is self.dict_button[
                    state["name"]]) and self.sticking_button.get_state():
                    self.sticking_button.change_style()
                self.sticking_button = self.dict_button[state["name"]]
            self.state = state
        else:
            self.tap = state

    def get_state(self):
        return self.state
    def get_tap(self):
        tap = self.tap
        self.tap = None
        return tap
