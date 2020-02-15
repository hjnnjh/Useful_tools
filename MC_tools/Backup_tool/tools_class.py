#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020-02-14 17:55
# @Author  : Jinnan Huang
# @Site    : 
# @File    : tools_class.py
# @Software: PyCharm

import sys, os, getpass, shutil

class MC_tools():
    """
    minecraft小工具
    """
    def __init__(self, mode="test", path_1="C:\\Users\\75542\Desktop\\test_src", path_2="C:\\Users\\75542\Desktop\\test_dst"):
        # 系统用户名
        self._username = getpass.getuser()
        self.mode = mode
        if self.mode == "test":
            self._src_path = path_1
            self._dst_path = path_2
        else:
            self._src_path =  "C:/Users/" + self._username + "/AppData/Roaming/.minecraft/versions/1.14.4-forge-28.2.0/saves"
            if self._username == "75542":
                self._dst_path = "F:/OneDrive/minecraft_source/存档文件"
            if self._username == "hjnnjh":
                self._dst_path = "C:/Users/hjnnjh/OneDrive/minecraft_source/存档文件"

    def get_latest_save(self, path):
        """
        按照存档修改时间排序获取最新存档，加入版本号检查，若不是最大版本号版本则以最大版本版本号版本为准
        :return:str, save's directory
        """
        saves_list = [x for x in os.listdir(path) if os.path.isdir(os.path.join(path, x))]
        saves_list_sorted = sorted(saves_list, key=lambda x: os.path.getmtime(os.path.join(path, x)))
        candidate_save = saves_list_sorted[-1]
        split_saves_list = list(map(lambda x:x.split("_"), saves_list))
        required_list = [x for x in split_saves_list if len(x) == 3]
        version_dict = {}
        for save_name in required_list:
            version_dict[tuple(save_name)] = int(save_name[2])
        max_version_number = version_dict[max(version_dict)]
        if int(candidate_save.split("_")[2]) < max_version_number:
            latest_save = "_".join(max(version_dict))
        else:
            latest_save = candidate_save
        return latest_save


    def Backup_saves(self):
        """
        将本地存档保存到Onedrive文件夹
        :return:
        """
        # 先读取Onedrive中最新存档的文件夹名
        latest_cloud_save = self.get_latest_save(self._dst_path)
        version = int(latest_cloud_save.split('_')[2])
        # 版本增加1
        new_save_name = latest_cloud_save.split('_')[0] + '_' + \
                        latest_cloud_save.split('_')[1] + '_' + \
                        str(version + 1)
        src = os.path.join(self._src_path, self.get_latest_save(self._src_path))
        dst = os.path.join(self._src_path, new_save_name)
        os.rename(src, dst)
        print("重命名成功！")
        # 备份
        shutil.copytree(dst, os.path.join(self._dst_path, new_save_name))
        print("备份成功！")



if __name__ == '__main__':
    Backup_tool = MC_tools(mode="run")
    # tool.get_latest_save(tool._dst_path)
    Backup_tool.Backup_saves()