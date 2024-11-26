from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QWidget, QGridLayout, QPushButton, QDialog
from .button_choice import Slider
from .change_group import Group

class Window_setting(QDialog):
    def __init__(self, parent=None):
        super(Window_setting, self).__init__(parent)
        self.grid_layout = QGridLayout()
        self.setLayout(self.grid_layout)
        self.setFixedSize(500, 400)
        self.setWindowTitle("Setting")
        self.setWindowFlag(Qt.WindowType.WindowStaysOnTopHint)
        #self.setWindowFlag(Qt.WindowType.)
        self.setStyleSheet("""background-color: black;""")
        self.read_setting()
        self.widgets()
        self.widget_pos()
        self.read_setting()

    def closeEvent(self, a0):
        self.write_setting()
        self.hide()

    def read_setting(self):
        self.setting = []
        self.default_setting = []
        f = open("Config_change.txt")
        fd = open("Config_default.txt")
        for i in f:
            x = i.split()
            self.setting.append([x[0], int(x[-1])])
        for i in fd:
            x = i.split()
            self.default_setting.append([x[0], int(x[-1])])
        f.close()
        fd.close()

    def write_setting(self):
        f = open("Config_change.txt", "w")
        state = self.group.get_state()
        for i in range(len(self.setting)):
            f.write(f"{self.setting[i][0]} = {int(state[i])}\n")
        f.close()


    def widgets(self):
        self.group = Group(self.setting, self.default_setting)
        self.exit_button = QPushButton("Save and Exit")
        self.exit_button.setStyleSheet("""background-color: white;border-radius: 10px;font: bold 14px;""")
        self.exit_button.clicked.connect(self.closeEvent)

    def widget_pos(self):
        self.grid_layout.addWidget(self.group, 0, 0)
        self.grid_layout.addWidget(self.exit_button, 1, 0)