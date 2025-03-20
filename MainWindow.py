import sys

from PyQt6.QtCore import QEvent
from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QApplication, QMainWindow, QGraphicsView

from Algo_Memory.Memory_algo import Memory
from Algorithms_window import *
from CustomDrawLabel import *
from Setting_window import *
from CustomToolBar.CustomToolBar import ReadyToolBar

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.Memory = Memory()
        self.window_algo = AlgoWindow(self.Memory)
        self.window_setting = Window_setting(self)
        self.ToolBar = ReadyToolBar(self)
        self.Canvas = Canvas_lb(self.Memory)
        self.setCentralWidget(self.Canvas)
        self.ToolBar.move(0, 0)
        self.Canvas.stackUnder(self.ToolBar)
        self.view_window()
        self.ToolBar.installEventFilter(self)
        self.ToolBar.clicked.connect(self.algo_window_restate)
        self.window_algo.helped_mark.connect(self.canvas_mark_state)
        self.window_algo.light_path_change.connect(self.set_light_path)
        self.window_algo.change_status.connect(self.clear_mark)
        self.window_setting.path_changed.connect(self.open_file)
        self.window_setting.path_save_to.connect(self.save_file)

    def view_window(self):
        self.setGeometry(200, 200, 700, 500)
        self.setMinimumSize(700, 500)
        self.setWindowTitle("Graphs")
        self.setWindowIcon(QIcon('GraphIcon.png'))

    def canvas_mark_state(self):
        self.Canvas.set_condition({"type": "sticking", "name": "helped_mark"})
        self.ToolBar.clear()

    def set_light_path(self):
        self.Canvas.set_condition({"type": "system", "name": "light_path"})

    def clear_mark(self):
        self.Canvas.set_condition({"type": "system", "name": "clear_mark"})

    def eventFilter(self, obj, event):
        if event.type() == QEvent.Type.MouseButtonPress or event.type() == QEvent.Type.MouseButtonDblClick:
            state = self.ToolBar.get_state()
            tap = self.ToolBar.get_tap()
            if tap != None:
                self.Canvas.set_condition(tap)
                if tap["name"] == "Done":
                    # self.ToolBar.clear()
                    # self.Canvas.set_condition()
                    self.algo_window_restate()
                if tap["name"] == "Setting":
                    # self.ToolBar.clear()
                    # self.Canvas.set_condition()
                    self.setting_window_restate()
            else:
                self.Canvas.set_condition(state)
            return True
        return False

    def algo_window_restate(self):
        if not self.window_algo.isVisible():
            self.window_algo.show()
        else:
            self.window_algo.close()
    def setting_window_restate(self):
        if not self.window_setting.isVisible():
            self.window_setting.show()
        else:
            self.window_setting.close()
    def open_file(self):
        self.Canvas.scene().clear_all()
        self.Canvas.scene().from_file(self.window_setting.get_path())
    def save_file(self):
        self.Memory.save_to_file(self.window_setting.get_save_path())

    def closeEvent(self, event):
        self.window_setting.hide()
        self.window_algo.hide()



app = QApplication(sys.argv)
f = open("Config.py", "w")
with open("Config_change.txt", "r") as r:
    for i in r:
        f.write(i)
with open("Config_no_change.txt", "r") as r:
    for i in r:
        f.write(i)
f.close()

if __name__ == "__main__":
    window = MainWindow()
    window.show()
    app.exec()

f = open("Config.py", "w")
with open("Config_change.txt", "r") as r:
    for i in r:
        f.write(i)
with open("Config_no_change.txt", "r") as r:
    for i in r:
        f.write(i)
f.close()