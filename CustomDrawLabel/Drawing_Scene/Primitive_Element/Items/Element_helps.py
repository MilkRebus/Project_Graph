from PyQt6.QtWidgets import QGraphicsEllipseItem

from Config import diameter_top


class focus(QGraphicsEllipseItem):
    def __init__(self, cord, diameter, parent=None):
        super(focus, self).__init__(parent)
        self.setRect(cord[0] - diameter / 2, cord[1] - diameter / 2, diameter, diameter)


class collidingTop(QGraphicsEllipseItem):
    def __init__(self, cord, parent=None):
        super(collidingTop, self).__init__(parent)
        self.setRect(cord[0] - diameter_top, cord[1] - diameter_top, diameter_top * 2, diameter_top * 2)

