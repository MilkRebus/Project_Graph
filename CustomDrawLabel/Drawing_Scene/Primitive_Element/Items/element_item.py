from collections import deque

from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPen, QBrush, QColor
from PyQt6.QtWidgets import QGraphicsPathItem, QGraphicsItem

from Config import color_dict, width_pen, background_color


class ElementItem(QGraphicsPathItem):
    def __init__(self, parent, name, cord):
        super(ElementItem, self).__init__(parent)
        self.setFlags(QGraphicsItem.GraphicsItemFlag.ItemIsFocusable)
        self._name = name
        self._cord = cord
        self._color = color_dict[self._name]
        self.color_element = self._color
        self._focus_flag = False
        self._text = None
        self._mark_flag = False
        self._mark_stack = deque()
        self._pen = QPen(QColor(f"{self._color}"))
        self._brush = QBrush(QColor(f"{background_color}"))
        self.setBrush(self._brush)
        self._pen.setWidth(width_pen)
        self.setPen(self._pen)

    def _restyle(self):
        self._pen.setStyle(Qt.PenStyle.DotLine)
        self.setPen(self._pen)

    def recolor(self, color=None):
        self.color_element = (self._color if color is None else color)
        self._pen.setColor(QColor(f"{self.color_element}"))
        self.setPen(self._pen)

    def add_mark(self, mark_name, color):
        if not self._mark_flag or mark_name is not None:
            self._mark_flag = True
            self._mark_stack.append((mark_name, color))
            self.recolor(color)

    def clear_mark(self, mark_name, color):
        if self._mark_stack:
            self._mark_stack.remove((mark_name, color))
            if self._mark_stack:
                self.recolor(self._mark_stack[-1][1])
            else:
                self._mark_flag = False
                self.recolor()

    @property
    def name_mark(self):
        if self._mark_stack:
            return self._mark_stack[-1][0]
        else:
            return None

    def clear_all_mark(self):
        self._mark_flag = False
        self._mark_stack = deque()
        self.recolor()

    def focusInEvent(self, event):
        self._restyle()
        if self._focus_flag:
            self.clearFocus()
            self._focus_flag = True

    def focusOutEvent(self, event):
        self._pen.setStyle(Qt.PenStyle.SolidLine)
        self._pen.setColor(QColor(f"{self.color_element}"))
        self._pen.setWidth(width_pen)
        self.setPen(self._pen)

    def get_cord(self):
        return self._cord

    @property
    def name(self):
        return self._name

    @property
    def text(self):
        return self._text

    @text.setter
    def text(self, string):
        self._text = string

    def get_text(self):
        return self._text

    @property
    def mark(self):
        return self._mark_flag
