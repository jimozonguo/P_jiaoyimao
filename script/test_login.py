import os, sys
import pytest
import time

from selenium.webdriver.common.by import By
sys.path.append(os.getcwd())
from base.base_driver import init_driver
from page.page_login import PageLogin #导入此页面类
from appium import webdriver
from base.base_yaml import yml_data_with_filename_and_key
import allure


#辅助函数：用于再处理测试数据
def data_with_key(key):
    return yml_data_with_filename_and_key("data_login", key)


class TestLogin:
    def setup(self):
        self.driver = init_driver()
        self.page_login = PageLogin(self.driver)
        time.sleep(5);#为了手动把固定弹窗点掉

    def teardown(self):
        self.driver.quit()

    @allure.step(title="测试“登录”模块")
    @pytest.mark.parametrize("dict_data", data_with_key("test_login"))
    def test_login(self,dict_data):
        allure.attach('', '步骤1：点击“我的”选项卡')
        #步骤1：点击“我的”
        self.page_login.click_my();
        allure.attach('', '步骤2：点击“登录/注册”')
        # #步骤2：点击“登录/注册”
        self.page_login.click_loginReg();
        allure.attach('', '步骤3：点击“UC”')
        # #步骤3：点击“UC”
        self.page_login.click_uc();
        allure.attach('', '步骤4：输入账号:%s'%(dict_data["username"]))
        # #步骤4：输入账号"13760453683"
        self.page_login.inputZanhao(dict_data["username"]);
        allure.attach('', '步骤5：输入密码:%s' % (dict_data["pwd"]))
        # #步骤5：输入密码"JIMOqinyu319"
        self.page_login.inputPwd(dict_data["pwd"]);
        allure.attach('', '步骤6：点击“登录”按钮')
        #步骤6：点击“登录”按钮
        self.page_login.click_login();
        allure.attach('', '步骤7：判断测试是否通过')
        # #步骤7：判断登录是否成功
        #ret=self.page_login.is_toast_exist(message=dict_data["toast"],timeout=10);
        ret = self.page_login.is_toast_exist(message=dict_data["toast"],is_screenshot=True,screenshot_name=dict_data["screen"],timeout=10);
        #把截取到的图片上传到Allure报告而已，不是真正截图
        allure.attach(open('./screen/' + dict_data["screen"] + '.png', 'rb').read(), "本次截图", allure.attachment_type.PNG)
        assert ret