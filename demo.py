#!usr/bin/python
#coding:utf8
from bs4 import BeautifulSoup
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
    authors = soup.find_all('div',class_="author clearfix")
    contents = soup.find_all('div',class_="content")
    for author in authors:
    	#print author
    	print author.find('h2').get_text()
    	#print author.find('div',class_="articleGender womenIcon")
    	#print author.find('div',class_="content")
    	#data['author'] = author.find('h2').get_text()
    	#data['sex']= author.find('div',class_="articleGender womenIcon")
    	#p = re.compile('<div class="articleGender (.*?)">(.*?)</div>')
    #print len(authors)
    #print authors
    for content in contents:
    	print content.find('span').get_text()

except urllib2.URLError, e:
    if hasattr(e,"code"):
        print e.code
    if hasattr(e,"reason"):
        print e.reason