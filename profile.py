#!/usr/bin/python
#coding:utf8
# from selenium import webdriver
## 配置文件地址
# profile_directory = r'C:\Users\Administrator\AppData\Roaming\Mozilla\Firefox\Profiles\wtrzp7i2.profileToolsQA'
# ## 加载配置文件
# profile = webdriver.FirefoxProfile(profile_directory)
# ## 启动浏览器配置
# driver = webdriver.Firefox(profile)
from selenium import webdriver

browser = webdriver.Chrome()
browser.get('http://baidu.com')