from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QGraphicsItem

from CustomDrawLabel.Drawing_Scene.Primitive_Element.Paths_element import *
from .element_item import ElementItem


class Arrow(ElementItem):
    def __init__(self, cord, parent=None):
        super(Arrow, self).__init__(parent, "Arrow", cord)
        self.setZValue(0)
        self.state = "only"
        self.setFlags(QGraphicsItem.GraphicsItemFlag.ItemIsFocusable)
        self._pen.setJoinStyle(Qt.PenJoinStyle.MiterJoin)
        self.setPath(ArrowPath(cord))

    def remake(self):
        if self.state == "only":
            self.setPath(ArcPath(self._cord))
            self.state = "due"
        else:
            self.setPath(ArrowPath(self._cord))
            self.state = "only"
        if self.text is not None:
            child = self.childItems()[0]
            child.remake(self.text)

    def set_text(self, text):
        if self.text is None:
            self.text = ""
        if text is None:
            self.text = self.text[:-1]
        elif len(self.text) < 3 and (text.isdigit() or text == "." or (text == "-" and self.text == "")):
            self.text += text
        child = self.childItems()[0]
        child.set_text(self.text)


class Loop(ElementItem):
    def __init__(self, cord, parent=None):
        super(Loop, self).__init__(parent, "Loop", cord)
        self.setZValue(0)
        self.setPath(LoopPath(cord))

    def set_text(self, text):
        if self.text is None:
            self.text = ""
        if text is None:
            self.text = self.text[:-1]
        elif len(self.text) < 3 and (text.isdigit() or text == "." or (text == "-" and self.text == "")):
            self.text += text
        child = self.childItems()[0]
        child.set_text(self.text)


class Stick(ElementItem):
    def __init__(self, cord, parent=None):
        super(Stick, self).__init__(parent, "Stick", cord)
        self.setZValue(0)
        self.setPath(StickPath(cord))

    def set_text(self, text):
        child = self.childItems()[0]
        if self.text is None:
            self.text = ""
        if text is None:
            self.text = self.text[:-1]
        elif len(self.text) < 3 and (text.isdigit() or text == "." or (text == "-" and self.text == "")):
            self.text += text
        child.set_text(self.text)


class Top(ElementItem):
    def __init__(self, cord, parent=None):
        super(Top, self).__init__(parent, "Top", cord)
        self.setZValue(10)
        self.setFlags(QGraphicsItem.GraphicsItemFlag.ItemIsFocusable)
        self.setPath(TopPath(cord))

    def set_text(self, text):
        if self.text is None:
            self.text = ""
        if text is None:
            self.text = self.text[:-1]
        elif len(self.text) < 3:
            self.text += text
        child = self.childItems()[0]
        child.set_text(self.text)
