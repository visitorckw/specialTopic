# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_countWindow(object):
    def setupUi(self, countWindow):
        countWindow.setObjectName("countWindow")
        countWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(countWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(220, 180, 161, 41))
        font = QtGui.QFont()
        font.setFamily("3ds")
        font.setPointSize(22)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(220, 230, 191, 51))
        font = QtGui.QFont()
        font.setFamily("3ds")
        font.setPointSize(22)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
       
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(430, 190, 101, 31))
        font = QtGui.QFont()
        font.setFamily("3ds")
        font.setPointSize(22)
        self.label_3.setFont(font)
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(430, 240, 111, 41))
        font = QtGui.QFont()
        font.setFamily("3ds")
        font.setPointSize(22)
        self.label_4.setFont(font)
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
       
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(325, 350, 93, 28))
        self.pushButton.setObjectName("pushButton")

        countWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(countWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 25))
        self.menubar.setObjectName("menubar")
        countWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(countWindow)
        self.statusbar.setObjectName("statusbar")
        countWindow.setStatusBar(self.statusbar)

        self.retranslateUi(countWindow)
        QtCore.QMetaObject.connectSlotsByName(countWindow)

    def retranslateUi(self, countWindow):
        _translate = QtCore.QCoreApplication.translate
        countWindow.setWindowTitle(_translate("countWindow", "MainWindow"))
        
        self.label.setText(_translate("countWindow", " time："))
        self.label_2.setText(_translate("countWindow", "score ："))
        self.pushButton.setText(_translate("countWindow", "確認"))