# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Translator_GUI_v4.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from GetText import Gettext
from ph_divide import get_content, get_former, get_later, add_text
from main import main
from GoogleTranlator import GoogleTranslator

text = ""
content_counter = 1
result = ""

class Ui_Translator_Google(object):
    def setupUi(self, Translator_Google):
        Translator_Google.setObjectName("Translator_Google")
        Translator_Google.resize(919, 686)
        self.centralwidget = QtWidgets.QWidget(Translator_Google)
        self.centralwidget.setObjectName("centralwidget")
        self.textBrowser_origin = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_origin.setGeometry(QtCore.QRect(10, 10, 441, 571))
        self.textBrowser_origin.setStyleSheet("font: 14pt \"微软雅黑\";")
        self.textBrowser_origin.setObjectName("textBrowser_origin")
        self.add_content_button = QtWidgets.QPushButton(self.centralwidget)
        self.add_content_button.setGeometry(QtCore.QRect(10, 590, 291, 61))
        self.add_content_button.setStyleSheet("font: 14pt \"微软雅黑\";")
        self.add_content_button.setObjectName("add_content_button")
        self.translate_2_button = QtWidgets.QPushButton(self.centralwidget)
        self.translate_2_button.setGeometry(QtCore.QRect(310, 590, 291, 61))
        self.translate_2_button.setStyleSheet("font: 14pt \"微软雅黑\";")
        self.translate_2_button.setObjectName("translate_2_button")
        self.clear_content_button = QtWidgets.QPushButton(self.centralwidget)
        self.clear_content_button.setGeometry(QtCore.QRect(610, 590, 291, 61))
        self.clear_content_button.setStyleSheet("font: 14pt \"微软雅黑\";")
        self.clear_content_button.setObjectName("clear_content_button")
        self.textBrowser_translation = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_translation.setGeometry(QtCore.QRect(460, 10, 441, 571))
        self.textBrowser_translation.setStyleSheet("font: 14pt \"微软雅黑\";")
        self.textBrowser_translation.setObjectName("textBrowser_translation")
        Translator_Google.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(Translator_Google)
        self.statusbar.setObjectName("statusbar")
        Translator_Google.setStatusBar(self.statusbar)

        self.retranslateUi(Translator_Google)
        QtCore.QMetaObject.connectSlotsByName(Translator_Google)

        # 槽函数
        self.translate_2_button.clicked.connect(self.abnormal_trans)
        self.add_content_button.clicked.connect(self.get_text)
        self.clear_content_button.clicked.connect(self.clear_content)

    def get_text(self):
        global text, content_counter, result
        if content_counter == 1:
            text = get_content()
        else:
            text += "\r\n" + get_content()
        result = " ".join(text.split('\r\n'))
        self.statusbar.showMessage("获取内容%d"%(content_counter))
        self.textBrowser_origin.clear()
        self.textBrowser_origin.append(result)
        content_counter += 1

    def abnormal_trans(self):
        global result
        raw_text = result
        self.textBrowser_origin.clear()
        self.textBrowser_translation.clear()
        result = main(raw_text)
        if len(result) != 0:
            self.textBrowser_origin.append("%s" % (raw_text))
            self.textBrowser_translation.append("%s" % (result))
            self.statusbar.showMessage("翻译成功！")
        else:
            self.statusbar.showMessage("服务器连接超时，稍后再试")

    def clear_content(self):
        global text, content_counter, result
        self.textBrowser_origin.clear()
        self.textBrowser_translation.clear()
        text = ""
        result = ""
        content_counter = 1
        self.statusbar.showMessage("清除内容成功")


    def retranslateUi(self, Translator_Google):
        _translate = QtCore.QCoreApplication.translate
        Translator_Google.setWindowTitle(_translate("Translator_Google", "Translator"))
        self.add_content_button.setText(_translate("Translator_Google", "增加文本内容"))
        self.translate_2_button.setText(_translate("Translator_Google", "翻译"))
        self.clear_content_button.setText(_translate("Translator_Google", "清除内容"))

