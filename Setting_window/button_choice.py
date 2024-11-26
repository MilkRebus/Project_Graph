from PyQt6.QtWidgets import QApplication, QWidget, QSlider, QLabel, QGridLayout
from PyQt6.QtCore import Qt
import Config
class Slider(QWidget):
    def __init__(self, Name, val, default, parent=None):
        super().__init__(parent)
        self.grid_layout = QGridLayout()
        self.setLayout(self.grid_layout)
        self.default = default

        self.val_label = QLabel(self)
        self.name_label = QLabel(Name)

        self.slider = QSlider(Qt.Orientation.Horizontal, self)

        self.val_label.setStyleSheet("""background-color: black; color: white; """)
        self.name_label.setStyleSheet("""background-color: black; color: white; """)
        self.slider.setOrientation(Qt.Orientation.Horizontal)

        self.slider.setMinimum(default//2)
        self.slider.setMaximum(default*2)
        self.slider.setTickInterval(1)
        self.slider.setValue(val)

        self.slider.setSingleStep(1)
        self.slider.setPageStep(1)

        self.slider.valueChanged.connect(self.display)

        self.grid_layout.addWidget(self.name_label, 0, 0)
        self.grid_layout.addWidget(self.slider, 0, 1)
        self.grid_layout.addWidget(self.val_label, 0, 2)
        self.display()
    def display(self):
        self.name_label.setFixedSize(100, 40)
        self.val_label.setFixedSize(100, 40)
        self.slider.setFixedSize(200, 40)
        self.val_label.setText("Value:  "+str(int((self.slider.value() / self.default) * 100)) + "%")
        self.val_label.adjustSize()

    def get_value(self):
        return self.slider.value()