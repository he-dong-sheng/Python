#!/usr/bin/python
#coding:utf8
from selenium import webdriver
import time
driver = webdriver.Firefox()
driver.get('file:///F:/Git/Python/jiumen.html')
## 纵向底部
js1 = 'document.getElementById("yoyoketang").scrollTop = 10000'
driver.execute_script(js1)

time.sleep(5)
## 纵向顶部
js2 = 'document.getElementById("yoyoketang").scrollTop = 0'
driver.execute_script(js2)

## 横向右侧
js3 = 'document.getElementById("yoyoketang").scrollLeft = 10000'
js3 = driver.execute_script(js3)

time.sleep(5)
## 横向左侧
js4 = 'document.getElementById("yoyoketang").scrollLeft = 0'
js4 = driver.execute_script(js4)