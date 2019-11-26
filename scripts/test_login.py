"""
登录学车不测试用例
"""
import pytest

from common.utils import init_driver
from page.page_factory import PageFactory
from tools.read_data import build_login_data


class TestLogin(object):
    """登录测试用例"""

    def setup(self):
        self.driver = init_driver()
        self.page_factory = PageFactory(self.driver)

    def teardown(self):
        self.driver.quit()

    @pytest.mark.parametrize('id,pwd', build_login_data())
    def test_login(self, id, pwd):
        self.page_factory.home_page.click_mine()  # 点击我的
        self.page_factory.mine_page.click_login()  # 点击登录
        self.page_factory.login_page.input_id(id)  # 输入账号
        self.page_factory.login_page.input_pwd(pwd)  # 输入密码
        self.page_factory.login_page.click_login_btn()  # 点击登录
        self.page_factory.login_page.click_com_btn()  # 点击确定