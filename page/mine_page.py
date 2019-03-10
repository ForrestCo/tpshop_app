# -*- coding: utf-8 -*-
# !/usr/bin/env python
# @File  : mine_page.py
# @Author: 杨崇
# @Date  : 2019/3/6
# @Desc  : null
from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class MinePage(BaseAction):
    # 头像
    avatar_btn = By.CLASS_NAME, "Avatar"
    # 我的订单

    # 我的余额

    # 虚拟订单

    # 拼团订单

    # 我的优惠券

    # 收货地址

    # 分销中心

    def loign(self):
        self.click(self.login_btn)
