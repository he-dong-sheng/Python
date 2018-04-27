#!usr/bin/python
#coding:utf8
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

## 加载配置文件免登陆
profile_directory = r'C:\Users\Administrator\AppData\Roaming\Mozilla\Firefox\Profiles\wtrzp7i2.profileToolsQA'
profile = webdriver.FirefoxProfile(profile_directory)
driver = webdriver.Firefox(profile)
driver.get('https://www.baidu.com')

## 修改元素的target属性
js = 'document.getElementsByClassName("mnav")[0].target="";'
driver.execute_script(js)
driver.find_element_by_link_text('新闻').click()