#!usr/bin/python
#coding:utf8
from bs4 import BeautifulSoup
import urllib2
import cookielib
import re

url1 = "https://www.baidu.com"

#方法一
print '-------第一种方法----------'
response1 = urllib2.urlopen(url1)
print response1.getcode()
print len(response1.read())

#方法二
print "-------第二种方法-----------"
request = urllib2.Request(url1)
request.add_header("user-agent","Moailla/5.0")
response2=urllib2.urlopen(request)
print response2.getcode()
print len(response2.read())

#方法三
print '--------第三种方法-----------'
url2 = "https://cuiqingcai.com"
cj = cookielib.CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
urllib2.install_opener(opener)
response3 = urllib2.urlopen(url2)
print response3.getcode()
print cj
print response3.read()