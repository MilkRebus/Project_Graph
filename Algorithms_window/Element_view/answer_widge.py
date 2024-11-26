from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPainter, QColor, QBrush
from PyQt6.QtWidgets import QGraphicsView, QGraphicsScene, QGraphicsTextItem


class Answer_widget(QGraphicsView):
    def __init__(self, parent=None):
        super(Answer_widget, self).__init__(parent)
        self.setScene(Answer_scene())
        self.setRenderHint(QPainter.RenderHint.Antialiasing)
        self.setAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignTop)
        self.setStyleSheet(f""" background:rgb(116,116,116);
                                border: 3px rgb(67,67,67);
                                border-style: solid ;
                                border-radius:10px;""")

    def clear(self):
        self.scene().clear()

    def set_answer(self, answer):
        self.scene().clear()
        self.scene().set_answer(answer)


class AnswerTextItem(QGraphicsTextItem):
    def __init__(self, text):
        super(AnswerTextItem, self).__init__()


class Answer_scene(QGraphicsScene):
    def __init__(self):
        super(Answer_scene, self).__init__()

    def set_answer(self, answer):
        for text_index in range(len(answer)):
            item = QGraphicsTextItem(answer[text_index])
            item.moveBy(0, text_index * 15)
            self.addItem(item)
