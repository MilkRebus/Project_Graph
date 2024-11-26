from PyQt6.QtCore import pyqtSignal
from PyQt6.QtWidgets import QLabel

from Config import setting_button
from CustomToolBar.ImButton import ImageButton


class Group(QLabel):
    entered = pyqtSignal()
    leaved = pyqtSignal()

    def __init__(self, size, names, parent=None):
        super(Group, self).__init__(parent)
        self.num = len(names)
        self.size_bt = size
        self.names = names
        self.resize(self.size_bt, self.size_bt)
        self.buttons = {}
        self.button_init()

    def button_init(self):
        count = -1
        for name in self.names:
            count += 1
            self.buttons[name] = ImageButton(self.size_bt, name, setting_button[name], self)
            self.buttons[name].move(0, self.size_bt * count)

    def get_button(self):
        return self.buttons

    def restate(self, state):
        self.parent().restate(state)

    def enterEvent(self, event):
        super().enterEvent(event)
        self.entered.emit()
        self.resize(self.size_bt, self.size_bt * self.num)

    def leaveEvent(self, event):
        super().leaveEvent(event)
        self.leaved.emit()
        self.resize(self.size_bt, self.size_bt)
