#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020-01-11 16:18
# @Author  : Jinnan Huang
# @Site    : 
# @File    : main.py
# @Software: PyCharm

import time
from GoogleTranlator import GoogleTranslator
from GetText import Gettext

def main(*t):
    if len(t) == 0:
        translator = GoogleTranslator()
        text = Gettext()
        result = translator.translate(text.gettext())
        return result, text.gettext()
    else:
        translator = GoogleTranslator()
        text = t[0]
        return translator.translate(text)

if __name__ == '__main__':
    main()