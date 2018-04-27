#!/usr/bin/python
#coding:utf8
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Firefox()

##测试部落
# driver.get("http://www.hordehome.com")
# driver.implicitly_wait(5)
# driver.find_element_by_id("search-button").click()
# driver.find_element_by_id("search-term").clear()
# driver.find_element_by_id("search-term").send_keys("selenium")
# time.sleep(3)
# ##模拟enter键操作回车按钮
# driver.find_element_by_id("search-term").send_keys(Keys.ENTER)

##百度页面设置按钮
driver.get("https://www.baidu.com")
driver.implicitly_wait(5)
#mouse = driver.find_element_by_link_text("设置")
##鼠标悬停在搜索设置按钮上
#ActionChains(driver).move_to_element(mouse).perform()
##鼠标右击设置按钮
#ActionChains(driver).context_click(mouse).perform()