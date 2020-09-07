import os, sys
sys.path.append(os.getcwd())
from base.page_base import PageBase #导入页面基类
from selenium.webdriver.common.by import By

class PageLogin(PageBase):
    #这些是抽取元素特征
    ele_my=By.XPATH,["text,我的,1","resource-id,com.jym.mall:id/indicator_tab_tv,1"]
    ele_loginReg=By.XPATH,["text,登录/注册,1","resource-id,com.jym.mall:id/user_account,1"]
    ele_uc=By.ID,"com.jym.mall:id/btn_login_uc"
    ele_zanhao=By.XPATH,"text,手机/邮箱/用户名/九游号,1"
    ele_login=By.XPATH,["text,登录,1","resource-id,com.jym.mall:id/login_normal,1"]
    # button_XXX1=By.ID,"resource-id属性的值";
    # button_XXX2=By.CLASS_NAME,"class属性的值";
    # button_XXX3=By.XPATH,"text,设";#包含
    # button_XXX4=By.XPATH,"text,设备,1";#精确
    # button_XXX5=By.XPATH,["index,5,1","text,设"];#多条件并且

    def __init__(self, driver):
        PageBase.__init__(self, driver)
        self.driver=driver;

    #这里写各种被脚本类调用的各种功能函数
    def click_my(self):
        self.click(self.ele_my)

    def click_loginReg(self):
        self.click(self.ele_loginReg);

    def click_uc(self):
        self.click(self.ele_uc)

    def inputZanhao(self,zanhao):
        self.input_text(self.ele_zanhao,zanhao)

    def inputPwd(self,pwd):
        eles=self.driver.find_elements_by_id("com.jym.mall:id/login_input");
        ele_pwd=eles[1];
        ele_pwd.send_keys(pwd);

    def click_login(self):
        self.click(self.ele_login)

