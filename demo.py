#!usr/bin/python
#-*-coding:utf-8 -*-
from bs4 import BeautifulSoup
import json
import urllib
import urllib2
import re
 
page = 1
url = 'https://www.qiushibaike.com/hot/page/' + str(page)
user_agent = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'
headers = { 'User-Agent' : user_agent }
try:
    request = urllib2.Request(url,headers = headers)
    response = urllib2.urlopen(request)
    html_doc = response.read()
    fout = open("test.html","w")
    fout.write(html_doc)
    soup = BeautifulSoup(html_doc,'html.parser',from_encoding='utf-8')
    txts = soup.find_all('div',class_="article")
    for txt in txts:
        #print txt
        author = txt.find('div',class_='author clearfix')
        author = author.find('h2').get_text()
        if txt.find('div',class_="articleGender")!=None:
            age = txt.find('div',class_="articleGender").get_text()
        else:
            age = 'none'
        contents = txt.find('span').get_text()

        print author
        #print age
        #print contents
        data={}
        data['1']= author
        print json.dumps(data, encoding="UTF-8", ensure_ascii=False)

except urllib2.URLError, e:
    if hasattr(e,"code"):
        print e.code
    if hasattr(e,"reason"):
        print e.reason