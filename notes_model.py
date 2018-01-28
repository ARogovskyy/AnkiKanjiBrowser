# -*- coding: utf-8 -*-
try:
    from PyQt5.QtWidgets import *
    from PyQt5.QtGui import *
    from PyQt5.QtCore import *
except ImportError:
    from PyQt4.QtGui import *
    from PyQt4.QtCore import *

from aqt import mw, utils

NID_Role = Qt.UserRole + 1

class NotesModel(QAbstractListModel):
    
    def __init__(self, parent=None):
        super(NotesModel, self).__init__(parent)
        self.filter_tag = self.search = ''
        self.update_model(None, None)

    def update_model(self, filter_tag, search):
        if filter_tag == self.filter_tag and search==self.search:
            return
        self.beginResetModel()
        self.filter_tag, self.search = filter_tag, search
        filters = ["kanji:_*"]
        if filter_tag:
            filter_tag = 'tag:' + filter_tag
            filters.append(filter_tag)
        if search:
            filters.append(search)
        
        search_pattern = ' '.join(('('+x+')' for x in filters))
        self.internal_list = []
        for noteId in mw.col.findNotes(search_pattern):
            note = mw.col.getNote(noteId)
            kanji_field = next((x for x in note.keys() if x.lower() == 'kanji'), None)
            if kanji_field and note[kanji_field]:
                self.internal_list.append((noteId, note[kanji_field][0]))
        self.endResetModel()

    def rowCount(self, parent = QModelIndex()):
        return len(self.internal_list)

    def columnCount(self, parent):
        return 1
    
    def data(self, index , role):
        if not index.isValid():
            return None

        if index.row() >= len(self.internal_list) or index.row() < 0:
            return None
        
        if role == Qt.DisplayRole:
            _, kanji_val = self.internal_list[index.row()]
            return kanji_val
        elif role == Qt.FontRole:
            return QFont("Source Han Serif", 48)
        elif role == NID_Role:
            nid, _ = self.internal_list[index.row()] 
            return nid        
