#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020-02-11 16:54
# @Author  : Jinnan Huang
# @Site    : 
# @File    : cmd.py
# @Software: PyCharm

import os
import getpass

path = "C:/Users/" + getpass.getuser() + "/Desktop/Input_image"
input_cmd = "C:\\Users\\" + getpass.getuser() + "\\Desktop\\Input_image"
output_cmd = "C:\\Users\\" + getpass.getuser() + "\\Desktop\\Output_txt"

image_list = [x for x in os.listdir(path) if os.path.splitext(x)[1] != '.txt']
print(image_list)
for item in image_list:
    item_name = item[:-4]
    order = "cd/d " + input_cmd + " &&tesseract " + item + " " + item_name + " -l chi_sim+eng"
    cmd = os.system(order)
    print(item + "处理完成！")
temp_txt_list = [x for x in os.listdir(path) if os.path.splitext(x)[1] == '.txt']
cmd2 = os.system("cd/d " + input_cmd + " &&type *.txt >>" + output_cmd + "\\merge.txt")
print("txt合并完成")
for item in temp_txt_list:
    os.remove(path + "/" + item)
    print("临时文件" + item + "已删除!")