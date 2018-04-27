#!/usr/bin/python
#coding:utf8
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
## 导入select模块
from selenium.webdriver.support.select import Select

def login(user,password):
    driver.get("http://www.xidibuy.com")
    # 设置隐试等待10秒
    driver.implicitly_wait(3)
    # 点登录按钮，输入账号密码后登录
    driver.find_element_by_link_text(u'登录').click()
    ## 清空用户名
    driver.find_element_by_id('name').clear()
    time.sleep(3)
    driver.find_element_by_id("name").send_keys(user)
    driver.find_element_by_id("passwd").send_keys(password)
    time.sleep(3)
    driver.find_element_by_id("submit").click()
    return driver

if __name__ == "__main__":
    profile_directory = r'C:\Users\Administrator\AppData\Roaming\Mozilla\Firefox\Profiles\wtrzp7i2.profileToolsQA'
    profile = webdriver.FirefoxProfile(profile_directory)
    driver = webdriver.Firefox(profile)
    login("15290852054","HEWANG19911104")
    time.sleep(10)#如果不休眠，登出的时候不会出现提示的弹窗
    t = driver.find_element_by_xpath("html/body/div[1]/div/div/div[1]/div/div[2]/div[1]/a[1]").text
    print t
    if t == u'您好，hedongsheng':
        print "登录成功"
    else:
        print "登录失败"