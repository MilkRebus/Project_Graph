from PyQt6.QtCore import QSize, pyqtSignal
from PyQt6.QtWidgets import QLabel, QListWidget, QAbstractItemView, QListView


class CustomListWidget(QListWidget):
    Change_Status = pyqtSignal()

    def __init__(self, parent=None):
        super(CustomListWidget, self).__init__(parent)
        self.setStyleSheet("border: -1px;")
        self.horizontalScrollBar().hide()
        self.verticalScrollBar().setStyleSheet("""width: 5; border: -4;""")
        self.qss = """color: white; font-size: 12pt;border-radius: 7px;"""
        self.verticalScrollBar().hide()
        self.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectItems)
        self.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)
        self.setSpacing(3)
        self.status = None
        self.addItem("")
        self.sizeRow = self.sizeHintForRow(0)
        self.sizeColumn = self.sizeHint().width()

        self.resize(self.sizeColumn, self.sizeRow + 10)
        self.label = QLabel(self)
        self.label.setFixedSize(self.sizeColumn - 20, 2)
        self.label.move(0, self.sizeRow + 8)
        self.label.setStyleSheet("background: white")

    def showLine(self):
        self.label.show()

    def hideLine(self):
        self.label.hide()

    def get_height(self):
        return self.sizeRow * (5 if self.count() >= 5 else self.count())

    def get_width(self):
        return self.sizeColumn

    def selectionChanged(self, selected, deselected):
        if len(self.selectedItems()) > 0 and self.status != self.selectedItems()[0].text():
            self.status = self.selectedItems()[0].text()
            self.Change_Status.emit()

    def enterEvent(self, event):
        self.verticalScrollBar().show()
        self.hideLine()
        self.scrollToTop()
        self.clearSelection()
        self.takeItem(0)
        self.setStyleSheet(self.qss + """border: 1px solid white;""")
        self.resize(self.sizeColumn, self.sizeRow * (4 if self.count() >= 3 else self.count()))

    def leaveEvent(self, event):
        self.verticalScrollBar().hide()
        self.insertItem(0, "" if self.status is None else self.status)
        self.setStyleSheet(self.qss + """border: -1px;""")
        self.resize(self.sizeColumn, self.sizeHintForRow(0) + 3)
        self.clearFocus()
        self.scrollToTop()
        self.showLine()

    def edit_status(self, name):
        if self.item(0).text() == "":
            self.takeItem(0)
        self.insertItem(0, name if name is not None else "")


class Algo_changed_widget(QLabel):
    Change_Status = pyqtSignal()

    def __init__(self, algo_list=None, parent=None):
        super(Algo_changed_widget, self).__init__(parent)

        self.label = QLabel("Algorithm:", self)
        self.label.setStyleSheet("""color: white; font-size: 16pt;""")

        self.widget_list = CustomListWidget(self)
        for name in algo_list:
            self.widget_list.addItem(name)
        self.widget_list.Change_Status.connect(self.emit_change)

        self.label.move(0, 0)
        self.widget_list.move(100, 0)
        self.widget_list.showLine()

    @property
    def status(self):
        return self.widget_list.status

    @status.setter
    def status(self, name):
        self.widget_list.status = name
        self.widget_list.edit_status(name)

    def clear(self):
        self.widget_list.status = None
        self.widget_list.edit_status(None)
        self.Change_Status.emit()

    def get_size(self):
        return QSize(self.label.width() + self.widget_list.get_width(), self.widget_list.get_height())

    def emit_change(self):
        self.Change_Status.emit()
