# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pinyin.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(0, 0, 801, 571))
        self.widget.setObjectName("widget")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(280, 50, 171, 41))
        font = QtGui.QFont()
        font.setFamily("华文行楷")
        font.setPointSize(19)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setGeometry(QtCore.QRect(130, 120, 101, 31))
        font = QtGui.QFont()
        font.setFamily("隶书")
        font.setPointSize(16)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setGeometry(QtCore.QRect(450, 120, 101, 31))
        font = QtGui.QFont()
        font.setFamily("隶书")
        font.setPointSize(16)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.waiting = QtWidgets.QTextEdit(self.widget)
        self.waiting.setGeometry(QtCore.QRect(110, 180, 161, 331))
        self.waiting.setReadOnly(True)
        self.waiting.setObjectName("waiting")
        self.buffer = QtWidgets.QTextEdit(self.widget)
        self.buffer.setGeometry(QtCore.QRect(330, 180, 361, 31))
        self.buffer.setReadOnly(True)
        self.buffer.setObjectName("buffer")
        self.text = QtWidgets.QTextEdit(self.widget)
        self.text.setGeometry(QtCore.QRect(330, 220, 361, 291))
        self.text.setReadOnly(True)
        self.text.setCursorWidth(0)
        self.text.setObjectName("text")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "拼音输入法"))
        self.label_2.setText(_translate("MainWindow", "候选词"))
        self.label_3.setText(_translate("MainWindow", "文本"))

