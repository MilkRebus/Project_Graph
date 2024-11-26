from PyQt6.QtCore import pyqtSignal, QSize, Qt, QVariantAnimation, QAbstractAnimation, QEasingCurve
from PyQt6.QtGui import QIcon, QPainter
from PyQt6.QtWidgets import QLabel

from Config import *


class ImageButton(QLabel):
    clicked = pyqtSignal()
    entered = pyqtSignal()
    leaved = pyqtSignal()

    def __init__(self, geometry, name, setting, parent=None):
        super(ImageButton, self).__init__(parent)
        self.name = name
        self.image = setting["image"]
        self.type = setting["type"]
        self.state = False
        self.size_icon = 0.6
        self.geometry_icon = QSize(int(geometry * self.size_icon), int(geometry * self.size_icon))
        self.border = int((geometry + geometry) / 7)
        self.setFixedSize(geometry, geometry)
        self.PaintDeviceMetric(QPainter.RenderHint.Antialiasing)
        self.active_style = f"""border-style: intset;padding: -3px; border: 3px solid {button_disabled_color};
             border-radius: {self.border}px; background-color: {button_active_color};"""

        self.setStyleSheet(self.active_style)
        self.setAlignment(Qt.AlignmentFlag.AlignCenter)
        if self.image is not None:
            self.setPixmap(QIcon(self.image[0]).pixmap(QSize(self.geometry_icon)))

        self._animation = QVariantAnimation(
            self,
            valueChanged=self._animate,
            startValue=0,
            endValue=80,
            duration=250
        )
        self._animation.setEasingCurve(QEasingCurve.Type.InCurve)

    def _animate(self, value):
        if value > 80: value = 160 - value
        qss = f"""
            border-style: inset;
            border-radius: {self.border}px;
            padding: -3px;
            border: 2px solid rgb({80 - value},{80 - value},{80 - value});
            background-color: rgb({160 - value},{160 - value},{160 - value});
        """
        self.setStyleSheet(qss)

    def mousePressEvent(self, ev):
        super().mousePressEvent(ev)
        self.clicked.emit()
        self.change_style()
        self.parent().restate({"name": self.name, "type": self.type})

    def change_style(self):
        if not self.state:
            if self.image[1] is not None:
                self.setPixmap(QIcon(self.image[1]).pixmap(QSize(self.geometry_icon)))
            elif self.type == "sticking":
                self._animation.setDirection(QAbstractAnimation.Direction.Forward)
                self._animation.start()
        else:
            if self.image[1] is not None:
                self.setPixmap(QIcon(self.image[0]).pixmap(QSize(self.geometry_icon)))
            elif self.type != "clicked":
                self._animation.setDirection(QAbstractAnimation.Direction.Backward)
                self._animation.start()
        if self.type == "clicked":
            self._animation.setEndValue(160)
            self._animation.start()
        self.state = not self.state

    def get_state(self):
        return self.state

    def enterEvent(self, ev):
        super().enterEvent(ev)
        self.entered.emit()

    def leaveEvent(self, ev):
        super().leaveEvent(ev)
        self.leaved.emit()
