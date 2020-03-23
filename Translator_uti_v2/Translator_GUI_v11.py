# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Translator_GUI_v11.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from GetText import Gettext
from ph_divide import get_content, get_former, get_later, add_text
from main import main
from GoogleTranlator import GoogleTranslator
from functools import partial
import re
from YoudaoTranslator import Youdao, Youdao_translator

text = ""
content_counter = 1
result = ""

class Ui_Translator_Google(object):
    def setupUi(self, Translator_Google):
        Translator_Google.setObjectName("Translator_Google")
        Translator_Google.resize(870, 651)
        self.centralwidget = QtWidgets.QWidget(Translator_Google)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.textBrowser_origin = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_origin.setStyleSheet("font: 14pt \"微软雅黑\";")
        self.textBrowser_origin.setObjectName("textBrowser_origin")
        self.gridLayout.addWidget(self.textBrowser_origin, 0, 0, 1, 3)
        self.textBrowser_translation = QtWidgets.QTextBrowser(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(14)
        self.textBrowser_translation.setFont(font)
        self.textBrowser_translation.setObjectName("textBrowser_translation")
        self.gridLayout.addWidget(self.textBrowser_translation, 0, 3, 1, 3)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setStyleSheet("font: 14pt \"微软雅黑\";")
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)
        self.add_content_button = QtWidgets.QPushButton(self.centralwidget)
        self.add_content_button.setMinimumSize(QtCore.QSize(0, 72))
        self.add_content_button.setStyleSheet("font: 14pt \"微软雅黑\";")
        self.add_content_button.setObjectName("add_content_button")
        self.gridLayout.addWidget(self.add_content_button, 1, 1, 2, 1)
        self.add_new_paragragh_button = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(14)
        self.add_new_paragragh_button.setFont(font)
        self.add_new_paragragh_button.setObjectName("add_new_paragragh_button")
        self.gridLayout.addWidget(self.add_new_paragragh_button, 1, 2, 1, 2)
        self.translate_2_button = QtWidgets.QPushButton(self.centralwidget)
        self.translate_2_button.setStyleSheet("font: 14pt \"微软雅黑\";")
        self.translate_2_button.setObjectName("translate_2_button")
        self.gridLayout.addWidget(self.translate_2_button, 1, 4, 1, 1)
        self.clear_content_button = QtWidgets.QPushButton(self.centralwidget)
        self.clear_content_button.setMinimumSize(QtCore.QSize(0, 72))
        self.clear_content_button.setStyleSheet("font: 14pt \"微软雅黑\";")
        self.clear_content_button.setObjectName("clear_content_button")
        self.gridLayout.addWidget(self.clear_content_button, 1, 5, 2, 1)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setStyleSheet("font: 14pt \"微软雅黑\";")
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)
        self.add_new_paragragh_button_2 = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(14)
        self.add_new_paragragh_button_2.setFont(font)
        self.add_new_paragragh_button_2.setObjectName("add_new_paragragh_button_2")
        self.gridLayout.addWidget(self.add_new_paragragh_button_2, 2, 2, 1, 2)
        self.translate_2_button_2 = QtWidgets.QPushButton(self.centralwidget)
        self.translate_2_button_2.setStyleSheet("font: 14pt \"微软雅黑\";")
        self.translate_2_button_2.setObjectName("translate_2_button_2")
        self.gridLayout.addWidget(self.translate_2_button_2, 2, 4, 1, 1)
        Translator_Google.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(Translator_Google)
        self.statusbar.setObjectName("statusbar")
        Translator_Google.setStatusBar(self.statusbar)

        self.retranslateUi(Translator_Google)
        QtCore.QMetaObject.connectSlotsByName(Translator_Google)

        # 信号与各个槽连接
        self.add_content_button.clicked.connect(partial(self.get_text, mode="add_text"))
        self.add_new_paragragh_button.clicked.connect(partial(self.get_text, mode="add_ph", engine="Google"))
        self.add_new_paragragh_button_2.clicked.connect(partial(self.get_text, mode="add_ph", engine="Youdao"))
        self.translate_2_button.clicked.connect(self.abnormal_trans)
        self.translate_2_button_2.clicked.connect(self.youdao_trans)
        self.clear_content_button.clicked.connect(self.clear_content)

    def get_text(self, mode, engine=None):
        """
        2 engines
        :param mode: str
        :return: None
        """
        global text, content_counter, result
        if mode == "add_text":
            if content_counter == 1:
                text = get_content()
            else:
                text += "\r\n" + get_content()
        if mode == "add_ph" and engine == "Google":
            text += " " + 20 * ("," + ".") + "?"
        if mode == "add_ph" and engine == "Youdao":
            text += " " + 'P' + 100 * (",") + "."
        result = " ".join(re.split(r'[\s]+', text))
        assert len(result) != 0
        self.statusbar.showMessage("获取内容%d" % (content_counter))
        self.textBrowser_origin.clear()
        self.textBrowser_origin.append(result)
        content_counter += 1

    def abnormal_trans(self):
        """
        Google engine
        :return:
        """
        global result
        raw_text = result
        self.textBrowser_origin.clear()
        self.textBrowser_translation.clear()
        result_t = main(raw_text)
        if len(result_t) != 0:
            self.textBrowser_origin.append("%s" % (raw_text))
            self.textBrowser_translation.append("%s" % (result_t))
            self.statusbar.showMessage("翻译成功！")
        else:
            self.statusbar.showMessage("服务器连接超时，稍后再试")

    def youdao_trans(self):
        """
        Youdao engine
        :return:
        """
        global result
        text_wait4trans = result
        self.textBrowser_origin.clear()
        self.textBrowser_translation.clear()
        yd_trans = Youdao_translator(text_wait4trans)
        result_t = yd_trans.Yd_translate()
        if len(result_t) != 0:
            self.textBrowser_origin.append("%s" % (text_wait4trans))
            self.textBrowser_translation.append("%s" % (result_t))
            self.statusbar.showMessage("翻译成功！")
        else:
            self.statusbar.showMessage("服务器连接超时，稍后再试")

    def clear_content(self):
        """
        for 2 engines
        :return:
        """
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
        self.label.setText(_translate("Translator_Google", "Google"))
        self.add_content_button.setText(_translate("Translator_Google", "增加文本内容"))
        self.add_new_paragragh_button.setText(_translate("Translator_Google", "G增加新的段落"))
        self.translate_2_button.setText(_translate("Translator_Google", "Google翻译"))
        self.clear_content_button.setText(_translate("Translator_Google", "清除内容"))
        self.label_2.setText(_translate("Translator_Google", "Youdao"))
        self.add_new_paragragh_button_2.setText(_translate("Translator_Google", "Y增加新的段落"))
        self.translate_2_button_2.setText(_translate("Translator_Google", "Youdao翻译"))