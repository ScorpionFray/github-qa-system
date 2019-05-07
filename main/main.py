'''
Created on 2018.12.6

@author:

'''
import sys
from user import UserStruct
from interface import Ui_MainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtGui import QPalette, QBrush, QPixmap
import ResStruct

if __name__ == "__main__":
    ResStruct.res_storage=UserStruct.User("init")
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())




