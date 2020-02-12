#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020-01-19 17:02
# @Author  : Jinnan Huang
# @Site    : 
# @File    : ordinate.py
# @Software: PyCharm

from pymouse import PyMouse

mou = PyMouse()
a = mou.position()
mou.move(3723, 750)
print(a)