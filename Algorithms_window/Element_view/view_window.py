from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QWidget, QGridLayout

from Algorithms_window.Element_view.like_button import LoginButton
from .algo_changed_widget import Algo_changed_widget
from .answer_widge import Answer_widget
from .helped_button import Helped_Button
from .widget_setting import Widget_setting


class View_AlgoWindow(QWidget):
    def __init__(self, **kwargs):
        super(View_AlgoWindow, self).__init__(**kwargs)
        self.grid_layout = QGridLayout()
        self.setLayout(self.grid_layout)
        self.setFixedSize(650, 400)
        self.setWindowTitle("Algorithms")
        self.setWindowFlag(Qt.WindowType.WindowStaysOnTopHint)
        self.setStyleSheet("background-color: black;")
        self.algo_state = Widget_setting(self.parameter_for_algo)
        self.answer_widget = Answer_widget()
        self.algo = Algo_changed_widget(self.dict_algorithms)
        self.other_widget = Helped_Button()
        self.name_algo = None
        self.button_start = LoginButton()
        self.widget_pos()
        self.widget_view()

    def widget_view(self):
        self.algo.setFixedSize(self.algo.get_size())
        self.button_start.setFixedSize(260, 60)

    def widget_pos(self):
        self.grid_layout.addWidget(self.algo_state, 1, 0)
        self.grid_layout.addWidget(self.algo, 0, 0)
        self.grid_layout.addWidget(self.answer_widget, 0, 1, 2, 1)
        self.grid_layout.addWidget(self.button_start, 3, 1, 1, 2)
