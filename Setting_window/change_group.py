from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QWidget, QGridLayout, QPushButton
from .button_choice import Slider

class Group(QWidget):
    def __init__(self, setting, default_setting, parent=None):
        super().__init__(parent)
        self.name = [i[0] for i in setting]
        self.val = [i[1] for i in setting]
        self.default = [i[1] for i in default_setting]
        self.sliders = []
        self.grid_layout = QGridLayout()
        self.setLayout(self.grid_layout)
        self.init_sliders()


    def init_sliders(self):
        for i in range(len(self.name)):
            self.sliders.append(Slider(self.name[i], self.val[i], self.default[i]))
            self.grid_layout.addWidget(self.sliders[i], i, 0)

    def get_state(self):
        state = [0] * len(self.name)
        for i in range(len(self.name)):
            state[i] = self.sliders[i].get_value()
        return state