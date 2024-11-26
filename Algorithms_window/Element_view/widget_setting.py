from PyQt6.QtWidgets import QLabel, QGridLayout, QWidget

from Algorithms_window.Element_view.toggle import ToggleCheckBox


class Widget_setting(QWidget):
    def __init__(self, dict_parameter, parent=None):
        super(Widget_setting, self).__init__(parent)
        self.main_layout = QGridLayout()
        self.main_layout.setVerticalSpacing(8)
        self.main_layout.setHorizontalSpacing(20)
        self.parameter = dict_parameter
        self._dict_value = {}
        self.setLayout(self.main_layout)
        self.main_layout.setHorizontalSpacing(150)
        self.init_parameter()
        self.setFixedSize(self.layout().sizeHint())

    def value(self, key):
        return self._dict_value[key].isChecked()

    def get_state(self):
        return {key: self.value(key) for key in self._dict_value.keys()}

    def init_parameter(self):
        column = 0
        for section in self.parameter.keys():
            label = QLabel(section + ":")
            label.setStyleSheet("""color: white; font-size: 18pt;""")
            self.main_layout.addWidget(label, column, 1)
            column += 1
            for parameter in self.parameter[section]:
                label = QLabel(parameter)
                label.setStyleSheet("""color: white; font-size: 14pt;""")
                toggle = ToggleCheckBox()
                self.main_layout.addWidget(label, column, 1)
                self.main_layout.addWidget(toggle, column, 2)
                self._dict_value[parameter] = toggle
                column += 1

    def clearMark(self):
        for toggle in self._dict_value.values():
            toggle.setChecked(False)
