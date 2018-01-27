# -*- coding: utf-8 -*-
import sys
import os

try:
    from PyQt5.QtWidgets import *
    from PyQt5.QtGui import *
    from PyQt5.QtCore import *
except ImportError:
    from PyQt4.QtGui import *
    from PyQt4.QtCore import *

if __name__ == "__main__":
    from dummy_model import NotesModel, NID_Role
else:
    from aqt import mw, dialogs
    from aqt.qt import *
    import aqt
    from notes_model import NotesModel, NID_Role

from kanji_view import Ui_MainWindow
from config import FILTER_TAGS, USE_CUSTOM_FONT

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.filter_tag = None
        self.model = NotesModel()

        self.setupUi(self)
        self.listView.setModel(self.model)
        self.listView.doubleClicked.connect(self.handle_doubleclick)

        self.filterComboBox.addItems([a for a,b in FILTER_TAGS])
        self.filterComboBox.currentIndexChanged.connect(self.handle_filter_changed)

        self.search_box.editingFinished.connect(self.handle_search_changed)
        self.add_tags_button.clicked.connect(self.handle_add_tags_click)

    def handle_doubleclick(self, index):
        nid = self.model.data(index, NID_Role)
        browser = dialogs.open('Browser', mw)
        # we shouldn't do this but idk if there is a better way
        browser._lastSearchTxt = "nid:" + str(nid)
        browser.model.search("nid:" + str(nid))

    def handle_filter_changed(self, index):
        _, self.filter_tag = FILTER_TAGS[index]
        self.model.update_model(self.filter_tag, self.search_box.text())

    def handle_search_changed(self):
        self.model.update_model(self.filter_tag, self.search_box.text())

    def handle_add_tags_click(self):
        text, res = aqt.utils.getText("Enter the tags to add:", parent=self)
        if res and text:
            self.add_tags_to_all(text)

    def add_tags_to_all(self, tags_str):
        nids = (self.model.data(index, NID_Role) for index in self.listView.selectionModel().selectedIndexes())
        nids = [x for x in nids if x]
        if not nids or not tags_str:
            return
        mw.col.tags.bulkAdd(nids, tags_str, add=True)

def load_fonts():
    if not USE_CUSTOM_FONT:
        return
    font_db = QFontDatabase()
    if __name__ == "__main__":
        font_pth = "./SourceHanSerif-Regular.otf"
    else:
        font_pth = os.path.join(os.path.dirname(__file__), "./SourceHanSerif-Regular.otf")
    kanji_font = QFontDatabase.addApplicationFont(font_pth)
    a = QFont("Source Han Serif", 48)

def ui_show_kanji_browser():
    window = MainWindow()
    window.show()
    mw.kanji_browser = window # so it doesnt get GC'ed

if __name__ == "__main__":
    app = QApplication(sys.argv)
    load_fonts()
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
else:
    load_fonts()
    show_kanji_browser_action = QAction("Show Kanji browser", mw)
    show_kanji_browser_action.setShortcut("Ctrl+K")
    show_kanji_browser_action.triggered.connect(ui_show_kanji_browser)
    mw.form.menuTools.addAction(show_kanji_browser_action)