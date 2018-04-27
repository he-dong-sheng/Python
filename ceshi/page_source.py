#coding:utf8
from selenium import webdriver
import re
import time

driver = webdriver.Firefox()
url = 'http://www.cnblogs.com/yoyoketang/'
driver.get(url)
time.sleep(3)
page = driver.page_source
time.sleep(3)
# print page
url_list = re.findall('href=\"(.*?)\"',page,re.S)
url_all = []
for url in url_list:
	if "http" in url:
		print url
		url_all.append(url)
print url_all