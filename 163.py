#!/usr/bin/python
# coding:utf8
from selenium import webdriver

driver = webdriver.Firefox()

driver.get("http://mail.163.com")
driver.implicitly_wait(5)
# 切换iframe
driver.switch_to_frame("x-URS-iframe")
driver.find_element_by_name("email").send_keys("15290852054")
driver.find_element_by_name("password").send_keys("HEWANG19911104")
driver.find_element_by_id("dologin").click()
# 释放iframe,重新回到主页上去
driver.switch_to_default_content()
