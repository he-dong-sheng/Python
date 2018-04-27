#!/usr/bin/python
#-*-coding:utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
from selenium import webdriver
import time
url = 'file:///F:/Git/Python/table.html'
driver = webdriver.Firefox()
driver.get(url)
time.sleep(3)

## //*[@id="myTable"]/tbody/tr[2]/td[1]    Xpath
## #myTable > tbody > tr:nth-child(2) > td:nth-child(1)  Css
# print driver.find_element_by_css_selector('#myTable>tbody>tr:nth-child(2)>td:nth-child(1)').text
t = driver.find_element_by_xpath(".//*[@id='myTable']/tbody/tr[2]/td[1]").text
print '',t
