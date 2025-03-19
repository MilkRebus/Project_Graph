from PyQt6.QtWidgets import QGraphicsScene

from CustomDrawLabel.Drawing_Scene.Primitive_Element import *


class DrawScene(QGraphicsScene):
    def __init__(self, Memory):
        super(DrawScene, self).__init__()
        self.Memory = Memory
        self.dict_item = {"Top": Top, "Arrow": Arrow, "Loop": Loop, "Stick": Stick}

    def drawElement(self, name, cord):
        if name == "Top":
            arr = self.collidingItems(collidingTop(cord))
        else:
            arr = self.collidingItems(focus(cord, 10))
        self.Memory.organize_element(name, arr, cord)
        if self.Memory.get_cord_element(name) is not None and self.Memory.replay(name):
            item = self.dict_item[name](self.Memory.get_cord_element(name))
            self.addItem(item)
            self.Memory.add_element(self.Memory.get_cord_element(name), item, name)

    def setFocusText(self, cord):
        arr = self.collidingItems(focus(cord, 5))
        if len(arr) != 0:
            if arr[0] == self.focusItem():
                self.clearFocus()
            else:
                if arr[0].name == "Text":
                    self.setFocusItem(arr[0].parentItem())
                else:
                    self.setFocusItem(arr[0])
        else:
            self.clearFocus()

    def deleteElement(self, cord):
        arr = self.collidingItems(focus(cord, 5))
        if len(arr) != 0:
            item = arr[0]
            if arr[0].name == "Text":
                item = arr[0].parentItem()
            self.deleteItem(item)

    def marking(self, cord):
        self.clearFocus()
        arr = self.collidingItems(focus(cord, 5))
        if len(arr) != 0 and arr[0].name in ("Text", "Top"):
            item = (arr[0] if arr[0].name == "Top" else arr[0].parentItem())

            if self.Memory.check_ident_mark():
                self.Memory.get_mark_item().clear_mark((self.Memory.mark_name, self.Memory.mark_type), self.Memory.get_color_mark())

            if self.Memory.replay_mark(item.get_cord()):
                self.Memory.add_mark(item.get_cord())
                item.add_mark((self.Memory.mark_name, self.Memory.mark_type), self.Memory.get_color_mark())
        else:
            self.set_state(None)

    def deleteItem(self, item):
        if item.name == "Top" and item.mark:
            self.Memory.delete_mark(item.name_mark)
            item.clear_all_mark()
        elements = self.Memory.delete_element(item.get_cord(), item.name)
        for item_delete in elements:
            self.removeItem(item_delete)

    def drawText(self, key, text):
        if key == 16777220:
            self.clearFocus()
        if self.focusItem() is not None and not (text in ("", " ")):
            item = self.focusItem()
            if item.get_text() is None:
                self.addItem(Text(item.get_cord(), item))
            if key == 16777219:
                item.set_text(None)
            else:
                item.set_text(text)
            self.Memory.save_text(item.get_text(), item.get_cord(), item.name)

    def recover_state(self):
        if len(self.Memory.recovery) != 0:
            info = self.Memory.recovering()
            if info[0] == "add":
                for item in info[1]:
                    self.addItem(item)
            else:
                for item in info[1]:
                    item.clear_all_mark()
                    self.removeItem(item)

    def refund_state(self):
        if len(self.Memory.cancellation) != 0:
            info = self.Memory.refunding()
            if info[0] == "delete":
                for item in info[1]:
                    self.addItem(item)
            else:
                for item in info[1]:
                    item.clear_all_mark()
                    self.removeItem(item)

    def set_light_path(self):
        if self.Memory.cleared_path is not None:
            for item in self.Memory.get_cleared_path():
                item.recolor()
        if self.Memory.light_path is not None:
            for item in self.Memory.get_lighted_item():
                item.recolor(self.Memory.color_path)

    def clear_light_path(self):
        if self.Memory.light_path is not None:
            for item in self.Memory.get_lighted_item():
                item.recolor()

    def clear_mark(self):
        items = self.Memory.pop_marked_items()
        self.Memory.light_path = None
        if items is not None:
            for item in items:
                item.recolor()
