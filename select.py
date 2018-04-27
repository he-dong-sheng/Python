#!/usr/bin/python
#coding:utf8
from selenium import webdriver
import time
import random
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
## 导入select模块
from selenium.webdriver.support.select import Select

driver = webdriver.Firefox()
url = "https://www.baidu.com"
driver.get(url)
driver.implicitly_wait(3)
## 鼠标移动到“设置”按钮
mouse = driver.find_element_by_link_text("设置")
ActionChains(driver).move_to_element(mouse).perform()
driver.find_element_by_link_text("搜索设置").click()
## 分两步：先定位下拉框，再点选项
# s = driver.find_element_by_id("nr")
# s.find_element_by_xpath('//*[@id="nr"]/option[3]').click()
## 通过索引：select_by_index()
s = driver.find_element_by_id("nr")
Select(s).select_by_index(2)