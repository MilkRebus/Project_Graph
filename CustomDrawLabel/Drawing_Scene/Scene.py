from PyQt6.QtGui import QBrush, QPen, QColor

from Config import *
from CustomDrawLabel.Drawing_Scene.DrawSceneFunctional import DrawScene


class View_scene(DrawScene):
    def __init__(self, Memory):
        super(View_scene, self).__init__(Memory)
        self.Memory = Memory
        self.name_element = {"Arrow", "Top", "Stick", "Loop"}
        self.setSceneRect(0, 0, 300, 200)
        self.last_state = 0
        self.state = "Top"

        self.brush = QBrush(QColor(f"{background_color}"))

    def mouseDoubleClickEvent(self, event):
        pass

    def set_state(self, state):
        self.state = state

    def set_mark_name(self, name):
        self.mark_name = name

    def keyPressEvent(self, event):
        self.drawText(event.key(), event.text())

    def clear_flags(self):
        self.Memory.clear_flag()
        self.clearFocus()
        self.last_state = self.state

    def clear_all(self):
        self.clear()
        self.Memory.clear_memory()

    def mousePressEvent(self, event):
        cord = (event.scenePos().x(), event.scenePos().y())
        self.clear_light_path()
        if self.state == "Delete":
            self.deleteElement(cord)

        if self.state == "helped_mark":
            self.marking(cord)

        if self.state == "Edit":
            self.setFocusText(cord)

        if self.state in self.name_element:
            self.drawElement(self.state, cord)
