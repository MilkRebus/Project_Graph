from PyQt6.QtCore import Qt, pyqtSignal, QAbstractAnimation, QVariantAnimation, QEasingCurve
from PyQt6.QtGui import QColor
from PyQt6.QtWidgets import QHBoxLayout, QPushButton, QLabel


class Button(QPushButton):
    def __init__(self, name, info, parent=None):
        super(Button, self).__init__(name, parent)
        self.name = name
        self.type = info[0]
        self.color = QColor(info[1])
        self.setFixedSize(60, 50)
        self.qss = """font: 75 10pt "Microsoft YaHei UI";
            color: rgb(255,255,255);
            font-weight: bold;
            border-style: solid;
            border-radius:5px;
            border: 2px solid rgb(67,67,67);"""
        self._animation_hover = QVariantAnimation(
            self,
            valueChanged=self._animate_hover,
            startValue=0.0001,
            endValue=0.9999,
            duration=150
        )
        self._animation_click = QVariantAnimation(
            self,
            valueChanged=self._animate_click,
            startValue=0.0001,
            endValue=0.9999,
            duration=200
        )
        # self._animation_click.setEasingCurve(QEasingCurve.Type.OutCubic)
        self._animation_hover.setEasingCurve(QEasingCurve.Type.InCubic)
        self.setStyleSheet(self.qss)

    def _animate_click(self, value):
        if value > 0.5: value = 1 - value
        gp = f"""
                    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1,
                    stop: 0 {QColor(67, 67, 67).name()},stop:{1 - value} {self.color.name()},stop:{value} {self.color.name()}, stop: 1 {QColor(67, 67, 67).name()});"""

        self.setStyleSheet(self.qss + gp)

    def mousePressEvent(self, event):
        self._animation_click.start()
        self.parent().set_state((self.name, self.type))

    def _animate_hover(self, value):
        gp = f"""
                    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0,
                    stop:{value} {QColor(0, 0, 0).name()}, stop: 0 {self.color.name()}); 
                    """
        if value == 0.9999:
            gp = f"background: {self.color.name()};"
        self.setStyleSheet(self.qss + gp)

    def enterEvent(self, event):
        self._animation_hover.setDirection(QAbstractAnimation.Direction.Forward)
        self._animation_hover.start()
        super().enterEvent(event)

    def leaveEvent(self, event):
        self._animation_hover.setDirection(QAbstractAnimation.Direction.Backward)
        self._animation_hover.start()
        super().leaveEvent(event)


class Helped_Button(QLabel):
    helped_restate = pyqtSignal()

    def __init__(self, parent=None):
        super(Helped_Button, self).__init__(parent)
        self.hlayout = QHBoxLayout()
        self.hlayout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.hlayout.setSpacing(20)
        self.state = None
        self.buttons = {}

    def set_button(self, dict_button):
        self.clear_all()
        if dict_button is not None:
            for name in dict_button.keys():
                button = Button(name, dict_button[name], self)
                self.hlayout.addWidget(button)
                self.buttons[name] = button
        self.setLayout(self.hlayout)

    def get_state(self):
        return self.state

    def set_state(self, name):
        self.state = name
        self.helped_restate.emit()

    def clear_all(self):
        if len(self.buttons) != 0:
            for button in self.buttons.values():
                self.hlayout.removeWidget(button)
        self.buttons.clear()
        self.state = None
