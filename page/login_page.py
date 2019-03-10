# -*- coding: utf-8 -*-
# !/usr/bin/env python
# @File  : login_page.py
# @Author: 杨崇
# @Date  : 2019/3/6
# @Desc  : 登录页
from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class LoginPage(BaseAction):
    # 账号
    user_name_btn = By.XPATH, "//*[@text='请输入账号']"
    # 密码
    user_pwd_btn = By.ID, "com.tpshop.malls:id/pwd_et"
    # 登录按钮
    login_btn = By.XPATH, "//*[@text='登录']"
    # 手机快速注册

    # 找回密码

    # 微信登录

    # QQ登录

    def user_name_input(self, text):
        self.input_text(self.user_name_btn, text)

    def user_pwd_input(self, text):
        self.input_text(self.user_pwd_btn, text)

    def login_click(self):
        self.click(self.login_btn)
