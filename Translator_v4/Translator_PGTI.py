#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020-01-12 13:22
# @Author  : Jinnan Huang
# @Site    : 
# @File    : main_exec.py
# @Software: PyCharm

import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from Translator_GUI_v4 import *

class mwindow(QtWidgets.QMainWindow,Ui_Translator_Google):
    def __init__(self):
        super(mwindow,self).__init__()
        self.setupUi(self)

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    mWin = mwindow()
    mWin.show()
    sys.exit(app.exec_())