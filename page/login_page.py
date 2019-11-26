"""
登录页面
"""
import page
from base.base_page import BasePage


class LoginPage(BasePage):
    id = page.id
    pwd = page.pwd
    login_btn = page.login_btn
    com_btn = page.com_btn

    def input_id(self, text):
        """输入账号"""
        self.input_func(self.id, text)

    def input_pwd(self, text):
        """输入密码"""
        self.input_func(self.pwd, text)

    def click_login_btn(self):
        """点击登录按钮"""
        self.click_func(self.login_btn)

    def click_com_btn(self):
        """点击确定按钮"""
        self.click_func(self.com_btn)
