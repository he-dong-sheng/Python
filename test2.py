#!/usr/bin/python
#coding:utf8
from selenium import webdriver
#导入time模块
import time
# browser = webdriver.Firefox()
browser = webdriver.Chrome()
#browser.get('https://www.baidu.com')
browser.get("http://bj.ganji.com")
##browser.page_source是获取网页的全部html
#print(browser.page_source)
##设置休眠时间3秒，也可以是小数，单位是秒
time.sleep(3)
##等待3秒后刷新页面
#browser.refresh()
#browser.get("http://hordehome.com")
#time.sleep(5)
##返回上一页
#browser.back()
#time.sleep(3)
##切换到下一页
#browser.forward()
##设置窗口大小
#browser.set_window_size(540,960)
#time.sleep(2)
##将浏览器窗口最大化
#browser.maximize_window()
##截屏，设置指定的保存路径+文件名称+后缀
#browser.get_screenshot_as_file("D:\\h_test\\b1.jpg")
##退出有两种，close和quit
##close用于关闭当前窗口，适合于多个窗口使用
#browser.close()
##quit用于结束进程，关闭所有的窗口
#browser.quit()
##通过id定位百度搜索框，并输入"python"
#browser.find_element_by_id("kw").send_keys("python")
##在firePath中copy出对应的xpath地址(先Ctrl+A，然后Ctrl+C)
#browser.find_element_by_xpath(".//*[@id='kw']").send_keys("python")
h = browser.current_window_handle
print h
browser.switch_to_window(h)
print browser.title