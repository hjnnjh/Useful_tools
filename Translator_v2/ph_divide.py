#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020-01-11 23:48
# @Author  : Jinnan Huang
# @Site    : 
# @File    : ph_button_1.py
# @Software: PyCharm

"""处理一段被两页分开的情况"""
from GetText import Gettext

def get_half():
    half_text = Gettext().gettext()
    return half_text

# push former button
def get_former():
     return get_half()

# push later button
def get_later():
    return get_half()

def add_text(text1, text2):
    all_text = text1 + "\r\n" + text2
    result = " ".join(all_text.split('\r\n'))
    return result
