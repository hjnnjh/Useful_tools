#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020-02-15 11:16
# @Author  : Jinnan Huang
# @Site    : 
# @File    : Backup_main.py
# @Software: PyCharm

import os
from Backup_tool.tools_class import MC_tools

def main(username):
    Backup_tool = MC_tools(mode=username)
    Backup_tool.Backup_saves()

if __name__ == '__main__':
    username = input("请输入备份类型（test or run）:")
    main(username)
    os.system("pause")