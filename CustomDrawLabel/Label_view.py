from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPainter, QBrush, QColor
from PyQt6.QtWidgets import QGraphicsView

from Config import background_color
from CustomDrawLabel.Drawing_Scene.Scene import View_scene


class Canvas_lb(QGraphicsView):
    def __init__(self, Memory):
        super(Canvas_lb, self).__init__(View_scene(Memory))
        self.setStyleSheet("border: 0px")

        self.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.setRenderHint(QPainter.RenderHint.Antialiasing)
        self.setAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignTop)
        brush = QBrush(QColor(f"{background_color}"))
        self.setBackgroundBrush(brush)

    def set_condition(self, state=None):
        self.scene().clear_flags()
        self.scene().clear_light_path()
        if state is not None:
            if state["type"] == "sticking":
                self.scene().set_state(state["name"])
            elif state["type"] == "helped_mark":
                self.scene().set_state(state["type"])
                self.scene().set_mark_name(state["name"])
            else:
                if state["name"] == "Refund":
                    self.scene().refund_state()
                elif state["name"] == "Recover":
                    self.scene().recover_state()
                elif state["name"] == "Clear":
                    self.scene().clear_all()
                elif state["name"] == "light_path":
                    self.scene().set_light_path()
                elif state["name"] == "clear_mark":
                    self.scene().clear_mark()
        else:
            self.scene().set_state(state)
