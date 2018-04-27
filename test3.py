#!/usr/bin/python
#coding=utf-8
from selenium import webdriver
import time
import random

driver = webdriver.Firefox()
driver.get("https://www.baidu.com")
driver.implicitly_wait(5)
driver.find_element_by_id("kw").send_keys(u"喜地")
driver.find_element_by_id("kw").submit()
s = driver.find_elements_by_css_selector("h3.t>a")
# print s
# exit()
# for i in s:
# 	print i.get_attribute("href")
##设置随机值
t = random.randint(0,9)
##方法一，随机取一个结果获取url地址，直接访问url
# a = s[t].get_attribute("href")
# print a
# driver.get(a)
##方法二，模拟用户点击行为
s[t].click()