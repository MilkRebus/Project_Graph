from PyQt6.QtCore import Qt, QStandardPaths, pyqtSignal
from PyQt6.QtWidgets import QWidget, QGridLayout, QPushButton, QDialog, QFileDialog
from .button_choice import Slider
from .change_group import Group

class Window_setting(QDialog):
    path_changed = pyqtSignal()
    path_save_to = pyqtSignal()
    def __init__(self, parent=None):
        super(Window_setting, self).__init__(parent)
        self.style = """background-color: #b7b7b7; border: solid #434343; border-width: 2px; 
                        border-radius: 10px;height: 30px; font-size: 20px;"""
        self.grid_layout = QGridLayout()
        self.setLayout(self.grid_layout)
        self.setFixedSize(500, 500)
        self._path = None
        self._save_path = None
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
        self.exit_button = QPushButton("Save setting")
        self.open_button = QPushButton("Open")
        self.save_button = QPushButton("Save")

        self.save_button.setStyleSheet(self.style)
        self.open_button.setStyleSheet(self.style)
        self.exit_button.setStyleSheet(self.style)

        self.save_button.clicked.connect(self.saveFile)
        self.open_button.clicked.connect(self.handleOpen)
        self.exit_button.clicked.connect(self.closeEvent)

    def handleOpen(self):
        start = QStandardPaths.standardLocations(
            QStandardPaths.StandardLocation.DocumentsLocation)[0]
        path = QFileDialog.getOpenFileName(self, "Open", start)[0]
        if path.endswith(".txt"):
            self._path = path
            self.path_changed.emit()
    def saveFile(self):
        start = QStandardPaths.standardLocations(
            QStandardPaths.StandardLocation.DocumentsLocation)[0]
        path = QFileDialog.getSaveFileName(self, "Save", start)[0]
        if path != None and path != "":
            self._save_path = path
            if not(path.endswith(".txt")):
                self._save_path += ".txt"
            self.path_save_to.emit()

    def get_path(self):
        return self._path
    def get_save_path(self):
        return self._save_path
    def widget_pos(self):
        self.grid_layout.addWidget(self.open_button, 0, 0)
        self.grid_layout.addWidget(self.save_button, 0, 1)
        self.grid_layout.addWidget(self.group, 1, 0, 1, 2)
        self.grid_layout.addWidget(self.exit_button, 2, 0, 1, 2)