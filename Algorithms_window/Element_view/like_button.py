from PyQt6.QtCore import pyqtSignal, QEasingCurve, QVariantAnimation, QAbstractAnimation
from PyQt6.QtGui import QColor
from PyQt6.QtWidgets import QPushButton


class LoginButton(QPushButton):
    clicked = pyqtSignal()

    def __init__(self, parent=None):
        super().__init__(parent)

        self.setMinimumSize(60, 60)
        self.setText("РАСЧИТАТЬ")
        self.color1 = QColor(116, 116, 116)
        self.color2 = QColor(0, 0, 0, 0)
        self.qss = """font: 75 14pt "Microsoft YaHei UI";
            color: rgb(255,255,255);
            font-weight: bold;
            border-style: solid;
            border-radius:21px;
            border: 2px solid rgb(67,67,67);"""

        self._animation_hover = QVariantAnimation(
            self,
            valueChanged=self._animate_hover,
            startValue=0.0001,
            endValue=0.5,
            duration=150
        )
        self._animation_click = QVariantAnimation(
            self,
            valueChanged=self._animate_click,
            startValue=0.0001,
            endValue=0.9999,
            duration=200
        )
        self._animation_click.setEasingCurve(QEasingCurve.Type.OutCubic)
        self._animation_hover.setEasingCurve(QEasingCurve.Type.InCubic)
        self.setStyleSheet(self.qss)

    def _animate_hover(self, value):
        gp = f"""
                    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0,
                    stop: 0 {QColor(67, 67, 67).name()},stop:{1 - value} {self.color2.name()},stop:{value} {self.color2.name()}, stop: 1 {QColor(67, 67, 67).name()});
                    """
        if value == 0.5:
            gp = f"background: {QColor(67, 67, 67).name()};"
        self.setStyleSheet(self.qss + gp)

    def _animate_click(self, value):
        if value > 0.5: value = 1 - value
        gp = f"""
                    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0,
                    stop: 0 {self.color1.name()},stop:{1 - value} {QColor(67, 67, 67).name()},stop:{value} {QColor(67, 67, 67).name()}, stop: 1 {self.color1.name()});"""

        self.setStyleSheet(self.qss + gp)

    def mousePressEvent(self, event):
        self.clicked.emit()
        self._animation_click.start()
        super(LoginButton, self).mousePressEvent(event)

    def enterEvent(self, event):
        self._animation_hover.setDirection(QAbstractAnimation.Direction.Forward)
        self._animation_hover.start()
        super().enterEvent(event)

    def leaveEvent(self, event):
        self._animation_hover.setDirection(QAbstractAnimation.Direction.Backward)
        self._animation_hover.start()
        super().leaveEvent(event)
