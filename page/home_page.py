# -*- coding: utf-8 -*-
# !/usr/bin/env python
# @File  : home.py
# @Author: 杨崇
# @Date  : 2019/3/6
# @Desc  : null
from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class HomePage(BaseAction):
    # 首页

    # 分类

    # 购物车

    # 我的
    mine_btn = By.XPATH, "//*[@text='我的']"

    # 点击我的
    def mine(self):
        self.click(self.mine_btn)
