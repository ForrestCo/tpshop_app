# -*- coding: utf-8 -*-
# !/usr/bin/env python
# @File  : card_page.py
# @Author: 杨崇
# @Date  : 2019/3/6
# @Desc  : null
from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class CardPage(BaseAction):
    # 登录
    login_btn = By.XPATH, "//*[@text='登录']"

    def login(self):
        self.click(self.login_btn)
