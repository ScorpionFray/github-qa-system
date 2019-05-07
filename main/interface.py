# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'interface.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

import sys
import webbrowser


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPalette, QBrush, QPixmap
from PyQt5.QtWidgets import QMainWindow, QApplication
from data_link import send_to
import ResStruct

homepage = []

class Ui_MainWindow(QtWidgets.QMainWindow):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 500)
        MainWindow.setDocumentMode(True)
        #palette = QPalette()
        #palette.setBrush(QPalette.Background, QBrush(QPixmap("../image/background.png")))
        #MainWindow.setPalette(palette)
        MainWindow.setStyleSheet("#MainWindow{border-image:url(../image/background.png);}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.button_send = QtWidgets.QPushButton(self.centralwidget)
        self.button_send.setGeometry(QtCore.QRect(670, 430, 100, 40))
        self.button_send.setText("")
        icon0 = QtGui.QIcon()
        icon0.addPixmap(QtGui.QPixmap("../image/SEND.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_send.setIcon(icon0)
        self.button_send.setIconSize(QtCore.QSize(70, 210))
        '''
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(17)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.button_send.setFont(font)
        '''

        self.button_send.setFocusPolicy(QtCore.Qt.NoFocus)
        self.button_send.setObjectName("button_send")

        self.button_home = QtWidgets.QPushButton(self.centralwidget)
        self.button_home.setGeometry(QtCore.QRect(710, 340, 60, 60))
        self.button_home.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../image/homepage.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_home.setIcon(icon)
        self.button_home.setIconSize(QtCore.QSize(32, 32))
        self.button_home.setObjectName("button_home")
        self.button_refresh = QtWidgets.QPushButton(self.centralwidget)
        self.button_refresh.setGeometry(QtCore.QRect(710, 260, 60, 60))
        self.button_refresh.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../image/refresh-1.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_refresh.setIcon(icon1)
        self.button_refresh.setIconSize(QtCore.QSize(32, 32))
        self.button_refresh.setObjectName("button_refresh")
        self.text_input = QtWidgets.QLineEdit(self.centralwidget)
        self.text_input.setGeometry(QtCore.QRect(50, 430, 590, 40))
        self.text_input.setObjectName("text_input")
        self.text_show = QtWidgets.QTextBrowser(self.centralwidget)
        self.text_show.setGeometry(QtCore.QRect(130, 115, 555, 285))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.text_show.setFont(font)
        self.text_show.setObjectName("text_show")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(150, 30, 480, 65))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        self.label.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)

        self.button_send.clicked.connect(self.func_send)
        self.button_home.clicked.connect(self.func_homepage)
        self.button_refresh.clicked.connect(self.func_clear)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "NJU-github-QASystem"))
        #self.button_send.setText(_translate("MainWindow", "SEND"))
        self.label.setText(_translate("MainWindow", "Input your question please"))
        #self.button_send.clicked.connect(self.func_send())
        #self.button_refresh.clicked.connect()


    def func_send(self):
        question = self.text_input.text()
        self.label.setText(question)
        self.text_input.clear()
        self.text_show.clear()
        #result = data_send.send()
        homepage.clear()
        result= send_to(question,homepage)
        #print("homepage=",str(homepage[0]))
        self.text_show.insertPlainText(result)

    #def func_refresh(self):
    def func_homepage(self):
        if(homepage != ''):
            webbrowser.open_new_tab(str(homepage[0]))
        else:
            self.text_show.clear()
            self.text_show.insertPlainText("Cannot find a homepage")

    def func_clear(self):
        self.text_show.clear()
        self.text_input.clear()
        self.label.setText("Please input your question")
        homepage.clear()