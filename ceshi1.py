# coding:utf-8
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
driver = webdriver.Firefox()
driver.get("http://www.cnblogs.com/yoyoketang/")
# 定位首页"新随笔"
try:
    element = driver.find_element("id", "blog_nav_newpostxx")
except NoSuchElementException as msg:
    print u"查找元素异常%s"%msg

# 点击该元素   # 交流QQ群：232607095
else:
    element.click()