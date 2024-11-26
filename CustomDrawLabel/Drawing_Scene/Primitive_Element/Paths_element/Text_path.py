from PyQt6.QtCore import QPointF
from PyQt6.QtGui import QPainterPath, QFont, QFontMetrics
from Config import size_text


class CustomFont(QFont):
    def __init__(self):
        super(CustomFont, self).__init__()

    def width(self):
        QFontMetrics(self)


class TextPath(QPainterPath):
    def __init__(self, cord, text):
        super(TextPath, self).__init__()
        self.cord = cord
        self.font = QFont()
        self.text = text
        self.size_point = size_text
        self.font.setPixelSize(size_text)
        self.font.setPointSize(self.size_point)
        self.size = self.get_size()
        self.print_text()

    def get_size(self):
        point = QPointF(0, 0)
        self.addText(point, self.font, self.text)
        width = self.boundingRect().width()
        height = self.boundingRect().height()
        self.clear()
        return width, height

    def print_text(self):
        point = QPointF(self.cord[0] - self.size[0] / 2, self.cord[1] + self.size[1] / 2)
        self.addText(point, self.font, self.text)
