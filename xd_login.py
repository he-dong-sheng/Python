#!/usr/bin/python
#coding:utf8
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

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
def logout():
	driver.find_element_by_xpath("//*[@id='current-user']/a/div/img").click()
	driver.find_element_by_link_text(u"登出").click()
	time.sleep(3)
	driver.quit()
def mouse():
	mouse = driver.find_element_by_link_text("个人中心")
	## 鼠标悬停在搜索设置按钮上
	ActionChains(driver).move_to_element(mouse).perform()
def address():
	driver.find_element_by_xpath('html/body/div[1]/div/div/div[1]/div/div[2]/div[3]/div/a[6]').click()
	all_h = driver.window_handles
	print all_h
	driver.switch_to_window(all_h[1])
	## html/body/div[4]/div[1]/ul/li[5]/a
	driver.find_element_by_xpath('html/body/div[4]/div[1]/ul/li[5]/a').click()
	time.sleep(5)
	## html/body/div[4]/div[3]/div/div/ul/li[2]/div[1]
	# driver.find_element_by_xpath('html/body/div[4]/div[3]/div/div/ul/li[2]/div[1]').click()
	driver.find_element_by_class_name(u'addNewBox-text').click()
	## html/body/div[9]/div[2]/div/div[1]/div[2]/input
	driver.find_element_by_xpath('html/body/div[9]/div[2]/div/div[1]/div[2]/input').send_keys(u'何东升')
	## html/body/div[9]/div[2]/div/div[2]/div[2]/div[1]/div[1]
	# ## 通过索引：select_by_index()  此处不是下拉框，不能用select
	# s = driver.find_element_by_xpath('html/body/div[9]/div[2]/div/div[2]/div[2]/div[1]/div[1]/ins')
	# Select(s).select_by_index(4)
	driver.find_element_by_xpath('html/body/div[9]/div[2]/div/div[2]/div[2]/div[1]/div[1]').click()
	time.sleep(3)
	## 获取省
	## html/body/div[9]/div[2]/div/div[2]/div[2]/div[1]/div[2]/ul[1]/li[4]
	driver.find_element_by_xpath('html/body/div[9]/div[2]/div/div[2]/div[2]/div[1]/div[2]/ul[1]/li[4]').click()
	time.sleep(3)
	## 获取市
	## html/body/div[9]/div[2]/div/div[2]/div[2]/div[2]/div[2]/ul[1]/li[1]
	driver.find_element_by_xpath('html/body/div[9]/div[2]/div/div[2]/div[2]/div[2]/div[2]/ul[1]/li[1]').click()
	time.sleep(3)
	## 获取县区
	## html/body/div[9]/div[2]/div/div[2]/div[2]/div[3]/div[2]/ul[1]/li[4]
	driver.find_element_by_xpath('html/body/div[9]/div[2]/div/div[2]/div[2]/div[3]/div[2]/ul[1]/li[4]').click()
	time.sleep(3)
	## 详细地址
	## html/body/div[9]/div[2]/div/div[3]/div[2]/input
	driver.find_element_by_xpath('html/body/div[9]/div[2]/div/div[3]/div[2]/input').send_keys(u'科学大道169号')
	## 邮编
	## html/body/div[9]/div[2]/div/div[4]/div[2]/input
	driver.find_element_by_xpath('html/body/div[9]/div[2]/div/div[4]/div[2]/input').send_keys(u'450001')
	## 手机号码
	## html/body/div[9]/div[2]/div/div[5]/div[2]/input[1]
	driver.find_element_by_xpath('html/body/div[9]/div[2]/div/div[5]/div[2]/input[1]').send_keys(u'15290852054')
	## 点击提交按钮
	## html/body/div[9]/div[2]/div/div[7]/a
	driver.find_element_by_xpath('html/body/div[9]/div[2]/div/div[7]/a').click()
	return '地址添加成功'

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
	a = address()
	print a

	#logout()