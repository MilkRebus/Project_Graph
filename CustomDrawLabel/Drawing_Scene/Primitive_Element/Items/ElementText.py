from PyQt6.QtCore import Qt
from PyQt6.QtGui import QColor, QPen, QBrush
from PyQt6.QtWidgets import QGraphicsPathItem

from Config import *
from CustomDrawLabel.Drawing_Scene.Primitive_Element.Paths_element.Geometry import *
from CustomDrawLabel.Drawing_Scene.Primitive_Element.Paths_element import *


class Text(QGraphicsPathItem):
    def __init__(self, cord, parent):
        super(Text, self).__init__(parent)
        self.name = "Text"
        self.cord = cord
        self.center = cord
        self.pen = QPen()
        self.pen.setStyle(Qt.PenStyle.SolidLine)
        self.pen.setColor(QColor(f"{color_top}"))
        self.pen.setWidth(1)
        self.brush = QBrush(QColor(f"{color_top}"))
        self.setPen(self.pen)
        self.setBrush(self.brush)
        self.setZValue(100)
        if self.parentItem().name != "Top":
            self.center = self.search_center()
        if self.parentItem().name in ("Stick", "Arrow"):
            self.set_angle()

    def set_angle(self):
        self.setTransformOriginPoint(self.center[0], self.center[1])
        angle = angle_text(self.cord)
        self.setRotation(angle)

    def remake(self, text):
        if self.parentItem().name != "Top":
            self.center = self.search_center()
            self.set_angle()
        self.set_text(text)

    def search_center(self):
        padding = 16
        if self.parentItem().name == "Stick" or (
                self.parentItem().name == "Arrow" and self.parentItem().state == "only"):
            return perpendicular_point_only((center_segment(self.cord), self.cord[0]), padding)
        elif self.parentItem().name == "Loop":
            return indent(self.cord[0], self.cord[1], joint)
        else:
            between = points_between_top(self.cord, depth_due_arrow, sqrt(radius_top ** 2 - depth_due_arrow ** 2))
            center = center_arrow(self.cord)
            return perpendicular_point_only((center_segment(between), between[0]),
                                            height_arc_segment(between, center) + padding)

    def set_text(self, text):
        self.setPath(TextPath(self.center, text))
