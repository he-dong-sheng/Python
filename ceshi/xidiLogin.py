# coding:utf-8
from selenium import webdriver
import unittest
import time
class XidiLogin(unittest.TestCase):
    u'''登录喜地客访平台'''
    # @classmethod
    # def setUpClass(cls):
    # 	# profile_directory = r'C:\Users\Administrator\AppData\Roaming\Mozilla\Firefox\Profiles\wtrzp7i2.profileToolsQA'
    # 	# profile = webdriver.FirefoxProfile(profile_directory)
    # 	# cls.driver = webdriver.Firefox(profile)
    #     cls.driver = webdriver.Firefox()
    #     url = "http://www.xidibuy.com"
    #     cls.driver.get(url)
    #     cls.driver.implicitly_wait(30)
    def setUp(self):
        profile_directory = r'C:\Users\Administrator\AppData\Roaming\Mozilla\Firefox\Profiles\wtrzp7i2.profileToolsQA'
        profile = webdriver.FirefoxProfile(profile_directory)
        self.driver = webdriver.Firefox(profile)
        # cls.driver = webdriver.Firefox()
        url = "http://www.xidibuy.com"
        self.driver.get(url)
        self.driver.implicitly_wait(30)

    def login(self, username, psw):
        u'''这里写了一个登录的方法,账号和密码参数化'''
        # 点登录按钮，输入账号密码后登录
        self.driver.find_element_by_link_text(u'登录').click()
        ## 清空用户名
        self.driver.find_element_by_id('name').clear()
        time.sleep(3)
        self.driver.find_element_by_id("name").send_keys(username)
        self.driver.find_element_by_id("passwd").send_keys(psw)
        time.sleep(3)
        self.driver.find_element_by_id("submit").click()

    def is_login_sucess(self):
        u'''判断是否获取到登录账户名称'''
        try:
        	text = self.driver.find_element_by_xpath("html/body/div[1]/div/div/div[1]/div/div[2]/div[1]/a[1]").text
        	print text
        	return True
        except:
            return False
    def get_error_info(self):
        error_info = self.driver.find_element_by_xpath('html/body/div[1]/div/div[1]/div[3]/p').text
        try:
            print error_info
            return True
        except:
            return False

    def test_01(self):
        u'''成功  用户名：hedongsheng'''
        self.login(u"15290852054", u"HEWANG19911104")  # 调用登录方法
        # 判断结果
        result = self.is_login_sucess()
        self.assertTrue(result)
        
    def test_02(self):
        u'''失败  密码错误'''
        self.login(u"15290852054", u"HEWANG19911104xx")  # 调用登录方法
        # 判断结果   
        result = self.get_error_info()
        self.assertTrue(result)

    def test_03(self):
        u'''失败  用户名错误'''
        self.login(u"15290852054xx", u"HEWANG19911104")  # 调用登录方法
        # 判断结果   
        result = self.get_error_info()
        self.assertTrue(result)

    def test_04(self):
        u'''失败  密码为空'''
        self.login(u"15290852054", u"")  # 调用登录方法
        # 判断结果   
        result = self.get_error_info()
        self.assertTrue(result)

    def test_05(self):
        u'''失败  用户名为空'''
        self.login(u"", u"HEWANG19911104")  # 调用登录方法
        # 判断结果   
        result = self.get_error_info()
        self.assertTrue(result)

    def test_06(self):
        u'''失败  用户名密码为空'''
        self.login(u"", u"")  # 调用登录方法
        # 判断结果   
        result = self.get_error_info()
        self.assertTrue(result)

    # @classmethod
    # def tearDownClass(cls):
    #     cls.driver.quit()
    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()