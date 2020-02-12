# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Translator_GUI_v2.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from GetText import Gettext
from ph_divide import get_half, get_former, get_later, add_text
from main import main
from GoogleTranlator import GoogleTranslator

# 对于横跨两页的特殊情况
former = ""
later = ""

class Ui_Translator_Google(object):
    def setupUi(self, Translator_Google):
        Translator_Google.setObjectName("Translator_Google")
        Translator_Google.resize(803, 587)

        # 添加背景图片
        # self.winpale = QtGui.QPalette()
        # self.winpale.setBrush(self.backgroundRole(), QtGui.QBrush(QtGui.QPixmap('.\\BGpic.png')))
        # self.setPalette(self.winpale)


        self.centralwidget = QtWidgets.QWidget(Translator_Google)
        self.centralwidget.setObjectName("centralwidget")
        self.textBrowser_origin = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_origin.setGeometry(QtCore.QRect(10, 10, 371, 401))
        self.textBrowser_origin.setStyleSheet("font: 14pt \"微软雅黑\";")
        self.textBrowser_origin.setObjectName("textBrowser_origin")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 420, 161, 21))
        self.label.setStyleSheet("font: 14pt \"微软雅黑\";")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(600, 420, 191, 21))
        self.label_2.setStyleSheet("font: 14pt \"微软雅黑\";")
        self.label_2.setObjectName("label_2")
        self.former_button = QtWidgets.QPushButton(self.centralwidget)
        self.former_button.setGeometry(QtCore.QRect(620, 450, 151, 31))
        self.former_button.setStyleSheet("font: 14pt \"微软雅黑\";")
        self.former_button.setObjectName("former_button")
        self.later_button = QtWidgets.QPushButton(self.centralwidget)
        self.later_button.setGeometry(QtCore.QRect(620, 490, 151, 31))
        self.later_button.setStyleSheet("font: 14pt \"微软雅黑\";")
        self.later_button.setObjectName("later_button")
        self.Abnormal_translate = QtWidgets.QPushButton(self.centralwidget)
        self.Abnormal_translate.setGeometry(QtCore.QRect(620, 530, 151, 31))
        self.Abnormal_translate.setStyleSheet("font: 14pt \"微软雅黑\";")
        self.Abnormal_translate.setObjectName("Abnormal_translate")
        self.Normal_translate = QtWidgets.QPushButton(self.centralwidget)
        self.Normal_translate.setGeometry(QtCore.QRect(20, 450, 151, 31))
        self.Normal_translate.setStyleSheet("font: 14pt \"微软雅黑\";")
        self.Normal_translate.setObjectName("Normal_translate")
        self.textBrowser_translation = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_translation.setGeometry(QtCore.QRect(420, 10, 371, 401))
        self.textBrowser_translation.setStyleSheet("font: 14pt \"微软雅黑\";")
        self.textBrowser_translation.setObjectName("textBrowser_translation")
        Translator_Google.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(Translator_Google)
        self.statusbar.setObjectName("statusbar")
        Translator_Google.setStatusBar(self.statusbar)

        self.retranslateUi(Translator_Google)
        QtCore.QMetaObject.connectSlotsByName(Translator_Google)

        # 槽函数
        self.Normal_translate.clicked.connect(self.show_normal_result)
        self.former_button.clicked.connect(self.former_text)
        self.later_button.clicked.connect(self.later_text)
        self.Abnormal_translate.clicked.connect(self.abnormal_trans)

    def show_normal_result(self):
        """
        运行main函数并输出结果至textbrowser
        :return:
        """
        # 每次翻译之前清空textBrowser
        self.textBrowser_origin.clear()
        self.textBrowser_translation.clear()
        if len(main()) != 0:
            self.textBrowser_origin.append("原文：\n%s" % (main()[1]))
            self.textBrowser_translation.append("译文：\n%s" % (main()[0]))
            self.statusbar.showMessage("翻译成功！")
        else:
            self.statusbar.showMessage("服务器连接超时，稍后再试")

    def former_text(self):
        global former
        former = get_former()
        self.statusbar.showMessage("获取前半部分内容")

    def later_text(self):
        global later
        later = get_later()
        self.statusbar.showMessage("获取后半部分内容")

    def abnormal_trans(self):
        raw_text = add_text(former, later)
        self.textBrowser_origin.clear()
        self.textBrowser_translation.clear()
        result = main(raw_text)
        if len(result) != 0:
            self.textBrowser_origin.append("原文：\n%s" % (raw_text))
            self.textBrowser_translation.append("译文：\n%s" % (result))
            self.statusbar.showMessage("翻译成功！")
        else:
            self.statusbar.showMessage("服务器连接超时，稍后再试")

    def retranslateUi(self, Translator_Google):
        _translate = QtCore.QCoreApplication.translate
        Translator_Google.setWindowTitle(_translate("Translator_Google", "Translator"))
        self.label.setText(_translate("Translator_Google", "Normal Situation:"))
        self.label_2.setText(_translate("Translator_Google", "Abnormal Situation:"))
        self.former_button.setText(_translate("Translator_Google", "前半部分"))
        self.later_button.setText(_translate("Translator_Google", "后半部分"))
        self.Abnormal_translate.setText(_translate("Translator_Google", "翻译"))
        self.Normal_translate.setText(_translate("Translator_Google", "翻译"))

