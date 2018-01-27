# -*- coding: utf-8 -*-
try:
    from PyQt5.QtWidgets import *
    from PyQt5.QtGui import *
    from PyQt5.QtCore import *
except ImportError:
    from PyQt4.QtGui import *
    from PyQt4.QtCore import *

NID_Role = Qt.UserRole + 1

class NotesModel(QAbstractListModel):
    
    def __init__(self, parent=None):
        super(NotesModel, self).__init__(parent)

    def rowCount(self, parent = QModelIndex()):
        return 20

    def columnCount(self, parent):
        return 1

    def update_model(self, filter_tag, search):
        print(filter_tag, search)

    def data(self, index , role):
        if not index.isValid():
            return None

        if index.row() >= 20 or index.row() < 0:
            return None
        
        if role == Qt.DisplayRole:
            return "学"
        elif role== Qt.FontRole:
            return QFont("Source Han Serif", 48)