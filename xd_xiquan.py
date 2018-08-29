#!/usr/bin/python
#coding:utf8
# import sys
# reload(sys)
# sys.setdefaultencoding('utf-8')
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
## 导入select模块
from selenium.webdriver.support.select import Select


def login(user,password):
	driver.get("http://www.xidibuy.com")
	# 设置隐试等待10秒
	driver.implicitly_wait(3)
	# 点登录按钮，输入账号密码后登录
	# html/body/div[1]/div/div/div[1]/div/div[2]/div[1]/a[1]
	# driver.find_element_by_xpath("html/body/div[1]/div/div[2]/div[1]/a[1]").click()
	driver.find_element_by_link_text(u'登录').click()
	## 清空用户名
	driver.find_element_by_id('name').clear()
	time.sleep(3)
	driver.find_element_by_id("name").send_keys(user)
	driver.find_element_by_id("passwd").send_keys(password)
	time.sleep(3)
	driver.find_element_by_id("submit").click()
	return driver

def mouse():
	mouse = driver.find_element_by_link_text("个人中心")
	## 鼠标悬停在搜索设置按钮上
	ActionChains(driver).move_to_element(mouse).perform()
def xiquan():
	driver.find_element_by_xpath('html/body/div[1]/div/div/div[1]/div/div[2]/div[3]/div/a[1]').click()
	all_h = driver.window_handles
	print all_h
	driver.switch_to_window(all_h[1])
	driver.find_element_by_xpath('html/body/div[4]/div[2]/div[1]/div[2]/input').send_keys('123456')
	driver.find_element_by_xpath('html/body/div[4]/div[2]/div[1]/div[2]/a').click()
	## html/body/div[4]/div[2]/div[1]/div[3]/p  error-wrap
	## html/body/div[4]/div[2]/div[1]/div[3]/p
	# info = driver.find_element_by_xpath('html/body/div[4]/div[2]/div[1]/div[3]/p').text
	info = driver.find_element_by_tag_name('p').text
	time.sleep(3)
	print type(info)
	# print len(info)
	print info
	# return info

if __name__ == "__main__":
	profile_directory = r'C:\Users\Administrator\AppData\Roaming\Mozilla\Firefox\Profiles\wtrzp7i2.profileToolsQA'
	profile = webdriver.FirefoxProfile(profile_directory)
	driver = webdriver.Firefox(profile)
	login("15290852054","HEWANG19911104")
	time.sleep(10)#如果不休眠，登出的时候不会出现提示的弹窗
	t = driver.find_element_by_xpath("html/body/div[1]/div/div/div[1]/div/div[2]/div[1]/a[1]").text
	# print t
	if t == u'您好，hedongsheng':
		print "登录成功"
	else:
		print "登录失败"
	mouse()
	xiquan()
	# info = xiquan()
	# print "喜地券兑换结果"
	# print info
