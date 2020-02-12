#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020-01-19 17:24
# @Author  : Jinnan Huang
# @Site    : 
# @File    : click.py
# @Software: PyCharm

from pymouse import PyMouse
import time
import sys

start = time.time()
m = PyMouse()
x, y = m.position()[0], m.position()[1]
while True:
    # x = 3704
    # y = 942
    m.move(x, y)
    m.click(x, y)
    end = time.time()
    process_time = end - start
    m.move(x + 19, y - 192)
    m.click(x + 19, y - 192)
    m.move(x + 25, y - 179)
    m.click(x + 25, y - 179)
    m.move(x - 200, y + 53)
    m.click(x - 200, y + 53)
    time.sleep(0.05)
    if process_time > 100:
        break
sys.exit(0)