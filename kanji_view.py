# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\kanji_view.ui'
#
# Created by: PyQt5 UI code generator 5.10
#
# WARNING! All changes made in this file will be lost!


try:
    from PyQt5 import QtCore, QtGui, QtWidgets
except ImportError:
    from PyQt4 import QtCore, QtGui
    QtWidgets = QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(1)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.search_box = QtWidgets.QLineEdit(self.widget)
        self.search_box.setObjectName("search_box")
        self.horizontalLayout.addWidget(self.search_box)
        self.filterComboBox = QtWidgets.QComboBox(self.widget)
        self.filterComboBox.setObjectName("filterComboBox")
        self.horizontalLayout.addWidget(self.filterComboBox)
        self.verticalLayout.addWidget(self.widget)
        self.widget_2 = QtWidgets.QWidget(self.centralwidget)
        self.widget_2.setObjectName("widget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget_2)
        self.horizontalLayout_2.setContentsMargins(9, 0, -1, -1)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.add_tags_button = QtWidgets.QPushButton(self.widget_2)
        self.add_tags_button.setFlat(False)
        self.add_tags_button.setObjectName("add_tags_button")
        self.horizontalLayout_2.addWidget(self.add_tags_button)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.verticalLayout.addWidget(self.widget_2)
        self.listView = QtWidgets.QListView(self.centralwidget)
        self.listView.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.listView.setResizeMode(QtWidgets.QListView.Adjust)
        self.listView.setViewMode(QtWidgets.QListView.IconMode)
        self.listView.setObjectName("listView")
        self.verticalLayout.addWidget(self.listView)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Kanji Browser"))
        self.search_box.setPlaceholderText(_translate("MainWindow", "Search pattern"))
        self.add_tags_button.setText(_translate("MainWindow", "Add tags"))

