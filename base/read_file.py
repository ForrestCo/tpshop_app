# -*- coding: utf-8 -*-
# !/usr/bin/env python
# @File  : read_file.py
# @Author: 杨崇
# @Date  : 2019/3/4
# @Desc  : null
import yaml


class ReadYaml:
    def __init__(self, file_path):
        self.file_path = file_path
        self.data = self.return_data()

    def return_data(self):
        with open(self.file_path, 'r') as fp:
            data = yaml.load(fp)
            return data

    def result(self):
        temp = self.data['user_info']
        res_li = []
        for i in temp.values():
            li = []
            for j in i.values():
                li.append(j)
            res_li.append(li)
        return res_li


if __name__ == '__main__':
    read_file = ReadYaml('../data/config.yaml')
    print(read_file.return_data())
    read_file.result()
