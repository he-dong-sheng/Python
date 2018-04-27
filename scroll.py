#!/usr/bin/python
#coding:utf8
from selenium import webdriver
import time
driver = webdriver.Firefox()
url = "https://news.baidu.com/"
driver.get(url)
#print driver.name
## 方法一 滚动到底部
# js = "var q=document.documentElement.scrollTop=10000"
# driver.execute_script(js)

## 方法二 滚动到底部
js = "window.scrollTo(0,document.body.scrollHeight)"
driver.execute_script(js)
#driver.implicitly_wait(10)
time.sleep(3)

## 滚动到顶部
# js = "window.scrollTo(0,0)"
# driver.execute_script(js)

## 聚焦元素
target = driver.find_element_by_id("city_name")
driver.execute_script("arguments[0].scrollIntoView();",target)