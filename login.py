#!/usr/bin/python
#coding:utf8
from selenium import webdriver
import time
def login(user,password):
	driver.get("http://www.hordehome.com")
	# 设置隐试等待10秒
	driver.implicitly_wait(5)
	# 点登录按钮，输入账号密码后登录
	driver.find_element_by_xpath(".//*[@id='ember724']/header/div/div/div[2]/span/button[2]").click()
	## 清空用户名
	driver.find_element_by_id('name').clear()
	time.sleep(3)
	driver.find_element_by_id("login-account-name").send_keys(user)
	driver.find_element_by_id("login-account-password").send_keys(password)
	time.sleep(3)
	driver.find_element_by_css_selector(".btn.btn-large.btn-primary").click()
	return driver
def logout():
	driver.find_element_by_xpath("//*[@id='current-user']/a/div/img").click()
	driver.find_element_by_link_text(u"登出").click()
	time.sleep(3)
	driver.quit()

if __name__ == "__main__":
	driver = webdriver.Firefox()
	login("15290852054","HEWANG19911104")
	time.sleep(10)#如果不休眠，登出的时候不会出现提示的弹窗
	t = driver.find_element_by_xpath("//*[@id='current-user']/a/div/img").get_attribute("title")
	print t
	if t == '15290852054':
		print "登录成功"
	else:
		print "登录失败"
	#logout()