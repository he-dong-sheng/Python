#coding:utf8
from selenium import webdriver
import time

driver = webdriver.Firefox()
## 启动浏览器后获取cookie
# print driver.get_cookies()
driver.get("http://www.cnblogs.com/yoyoketang/")
## 打开主页后获取cookie
print driver.get_cookies()
## 登录后获取cookie
url = "https://passport.cnblogs.com/user/signin"
driver.get(url)
driver.implicitly_wait(30)
driver.find_element_by_id("input1").send_keys("15290852054")
driver.find_element_by_id("input2").send_keys(u"HEWANG19911104!")
driver.find_element_by_id("signin").click()
time.sleep(3)
print driver.get_cookies()