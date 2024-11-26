from PyQt6.QtCore import pyqtSignal

from .Element_view import *
from .algorithms_for_graph.Provider_for_algorithms import Provider


class AlgoWindow(View_AlgoWindow, Provider):
    helped_mark = pyqtSignal()
    light_path_change = pyqtSignal()
    change_status = pyqtSignal()

    def __init__(self, Memeory):
        super(AlgoWindow, self).__init__(Memory=Memeory)
        self.Memory = Memeory
        self.connect_events()

    def connect_events(self):
        self.algo.Change_Status.connect(self.change_algo)
        self.other_widget.helped_restate.connect(self.emit_restate)
        self.button_start.clicked.connect(self.calculate)

    def calculate(self):
        self.calculate_algorithm(self.get_info())
        self.answer_widget.clear()
        if self.get_answer() is not None:
            self.answer_widget.set_answer(self.get_answer())
            self.Memory.set_lighted_path(self.get_lighted_path())
            self.light_path_change.emit()

    def emit_restate(self):
        self.Memory.set_mark_name(self.other_widget.get_state())
        if self.name_algo is not None and self.get_info_algo(self.name_algo) is not None:
            self.Memory.set_color_mark(self.get_color_mark(self.name_algo))
        self.helped_mark.emit()

    def set_helped_mark(self, key):
        self.other_widget.set_element_helped(key)

    def change_algo(self):
        self.change_status.emit()
        self.answer_widget.clear()
        self.name_algo = self.algo.status
        if self.name_algo is not None:
            self.other_widget.set_button(self.get_bt_info(self.name_algo))
            self.grid_layout.addWidget(self.other_widget, 3, 0)
            self.Memory.set_dict_marked_element(self.get_info_algo(self.name_algo))
        else:
            self.other_widget.clear_all()

    def get_lighted_path(self):
        return self.get_path()

    def get_info(self):
        return {"name": self.algo.status, "parameter": self.algo_state.get_state(),
                "dop_info": self.Memory.get_helped(), "graph": self.Memory.get_graph()}

    def closeEvent(self, event):
        self.answer_widget.clear()
        self.change_status.emit()
