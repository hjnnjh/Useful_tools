#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020-01-11 13:51
# @Author  : Jinnan Huang
# @Site    : 
# @File    : use_copy_paste.py
# @Software: PyCharm

import pyperclip

class Gettext():
    def PasteText(self):
        """
        获取剪贴板内容
        :return: str, 剪贴板中的内容
        """
        return pyperclip.paste()


    def gettext(self):
        """
        删除换行符，返回可用于翻译的文本
        :return: str, 输入翻译的文本
        """
        text = self.PasteText()
        if type(text) is not str:
            raise ValueError('Copy content is not str')
        else:
            result = " ".join(text.split('\r\n'))
            # return text.replace('\r\n','')
            return result

if __name__ == "__main__":
    text = Gettext()
    print(text.gettext())