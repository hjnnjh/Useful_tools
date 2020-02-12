#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020-02-08 19:40
# @Author  : Jinnan Huang
# @Site    : 
# @File    : click4twitch.py
# @Software: PyCharm

from pymouse import PyMouse
import time
import sys

start = time.time()
m = PyMouse()
i = 0

while True:
    x, y = m.position()[0], m.position()[1]
    m.click(x, y)
    i += 1
    if i%2 == 1:
        m.move(x + 50, y + 50)
    else:
        m.move(x - 50, y - 50)
    end = time.time()
    process_time = end - start
    time.sleep(60)
    if process_time > 43200:
        break
sys.exit(0)