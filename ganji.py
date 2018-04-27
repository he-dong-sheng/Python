#!/usr/bin/python
#coding:utf8
from selenium import webdriver
import time
import random

driver = webdriver.Firefox()

driver.get("http://bj.ganji.com")
driver.implicitly_wait(5)
##获取当前窗口句柄s
h = driver.current_window_handle
print h
driver.find_element_by_link_text("全职").click()
all_h = driver.window_handles
print all_h
##方法一：判断句柄，不等于首页就切换
# for i in all_h:
# 	if i != h:
# 		driver.switch_to_window(i)
# 		print driver.title
##方法二：获取list里面第二个直接切换
driver.switch_to_window(all_h[1])
print driver.title
##关闭新窗口
driver.close()
##切换到首页句柄
driver.switch_to_window(h)
##打印当前的title,无法获取第一个页面的标题
print driver.title