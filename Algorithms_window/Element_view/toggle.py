from PyQt6.QtCore import (
    Qt, QPoint, QEasingCurve, QPropertyAnimation, QRect, pyqtSlot, pyqtProperty)
from PyQt6.QtGui import *
from PyQt6.QtWidgets import QCheckBox


class ToggleCheckBox(QCheckBox):

    def __init__(self,
                 parent=None,
                 size=(40, 20),
                 padding=3,
                 active_bg_color=QColor("#00e1ff").name(),  # 1a9fff
                 active_fg_color=Qt.GlobalColor.white,
                 disabled_bg_color=QColor(150, 150, 150).name(),
                 disabled_fg_color=Qt.GlobalColor.white,
                 ):
        super(ToggleCheckBox, self).__init__(parent)
        self.setFixedSize(size[0], size[1])
        self.padding = padding
        self._circle_position = padding
        self._active_bg_color = active_bg_color
        self._active_fg_color = active_fg_color
        self._disabled_bg_color = disabled_bg_color
        self._disabled_fg_color = disabled_fg_color
        self.animation = QPropertyAnimation(self, b"circle_position", self)
        self.animation.setEasingCurve(QEasingCurve.Type.OutBack)
        self.animation.setDuration(250)

        self.stateChanged.connect(self.start_transition)

    @pyqtSlot(int)
    def start_transition(self, value):
        self.animation.stop()
        self.animation.setEndValue(self.width() - (self.height() - self.padding) if value else self.padding)
        self.animation.start()

    @pyqtProperty(int)
    def circle_position(self):
        return self._circle_position

    @circle_position.setter
    def circle_position(self, pos):
        self._circle_position = pos
        self.update()

    def hitButton(self, pos: QPoint):
        return self.contentsRect().contains(pos)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)
        painter.setPen(Qt.PenStyle.NoPen)
        rect = QRect(0, 0, self.width(), self.height())
        if not self.isChecked():
            painter.setBrush(QColor(self._disabled_bg_color))
            painter.drawRoundedRect(0, 0, rect.width(), self.height(), self.height() / 2, self.height() / 2)

            painter.setBrush(QColor(self._disabled_fg_color))

        else:
            painter.setBrush(QColor(self._active_bg_color))
            painter.drawRoundedRect(0, 0, rect.width(), self.height(), self.height() / 2, self.height() / 2)

            painter.setBrush(QColor(self._active_fg_color))

        painter.drawEllipse(self._circle_position, 3, self.height() - self.padding * 2,
                            self.height() - self.padding * 2)
        painter.end()
