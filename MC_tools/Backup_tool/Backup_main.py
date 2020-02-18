#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020-02-15 11:16
# @Author  : Jinnan Huang
# @Site    : 
# @File    : Backup_main.py
# @Software: PyCharm

import os
from pysrc.tools_class import MC_tools

def main(str):
    Backup_tool = MC_tools(mode=str)
    if Backup_tool.mode == "BKU":
        Backup_tool.Backup_saves()
    if Backup_tool.mode == "PULL":
        Backup_tool.pull2saves()
    if Backup_tool.mode == "Exit":
        pass

if __name__ == '__main__':
    mode_type = input("请输入进行操作的类型（存档【BKU】, 获取存档【PULL】, 退出【Exit】）:")
    main(mode_type)
    os.system("pause")