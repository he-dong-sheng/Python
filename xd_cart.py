#!/usr/bin/python
#coding:utf8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
## 导入select模块
from selenium.webdriver.support.select import Select

def login(user,password):
	driver.get("http://www.xidibuy.com")
	# 设置隐试等待3秒
	driver.implicitly_wait(3)
	# 点登录按钮，输入账号密码后登录
	# html/body/div[1]/div/div/div[1]/div/div[2]/div[1]/a[1]
	## 清空用户名
	driver
	driver.find_element_by_link_text(u'登录').click()
	time.sleep(3)
	## 清空用户名
	driver.find_element_by_id('name').clear()
	time.sleep(3)
	driver.find_element_by_id("name").send_keys(user)
	time.sleep(3)
	driver.find_element_by_id("passwd").send_keys(password)
	time.sleep(3)
	driver.find_element_by_id("submit").click()
	return driver
def search(key):
	## html/body/div[1]/div/div/div[2]/div[1]/form/div[1]/input[1]
	## html/body/div[1]/div/div/div[2]/div[1]/form/div[1]/input[2]
	driver.find_element_by_xpath('html/body/div[1]/div/div/div[2]/div[1]/form/div[1]/input[1]').send_keys(key)
	driver.find_element_by_xpath('html/body/div[1]/div/div/div[2]/div[1]/form/div[1]/input[2]').click()
def cart():
	## 进入详情页
	## html/body/div[4]/div/div[4]/ul/li[1]/div/div[1]/div[1]/a/img
	driver.find_element_by_xpath('html/body/div[4]/div/div[4]/ul/li[1]/div/div[1]/div[1]/a/img').click()
	all_h = driver.window_handles
	# print all_h
	driver.switch_to_window(all_h[1])
	time.sleep(3)
	## 加入购物车
	## html/body/div[4]/div[2]/div[1]/div[2]/div[4]/a[2]
	old_num = driver.find_element_by_id('cartNum').text
	print 'old_num:',old_num
	driver.find_element_by_xpath('html/body/div[4]/div[2]/div[1]/div[2]/div[4]/a[2]').click()
	time.sleep(2)
	new_num = driver.find_element_by_id('cartNum').text
	print 'new_num:',new_num
	

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
	search(u'蜂蜜')
	cart()
