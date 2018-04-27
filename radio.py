#!/usr/bin/python
#coding:utf8
import time
from selenium import webdriver

profile_directory = r'C:\Users\Administrator\AppData\Roaming\Mozilla\Firefox\Profiles\wtrzp7i2.profileToolsQA'
profile = webdriver.FirefoxProfile(profile_directory)
driver = webdriver.Firefox(profile)
driver.get('file:///F:/Git/Python/radio.html')
## 点击之前判断是否选中
s = driver.find_element_by_id('boy').is_selected()
print s
driver.find_element_by_id('boy').click()
time.sleep(5)
driver.find_element_by_id('girl').click()
time.sleep(3)
r = driver.find_element_by_id('girl').is_selected()
print r
# driver.find_element_by_id('c1').click()
## //*[@id="c1"]//*[@type="c1"]
c1 = driver.find_element_by_id('c1').is_selected()
print c1
checks = driver.find_elements_by_xpath('//*[@type="checkbox"]')
for i in checks:
	i.click()
c_1 = driver.find_element_by_id('c1').is_selected()
print c_1
