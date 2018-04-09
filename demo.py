#!usr/bin/python
#-*-coding:utf-8 -*-
from bs4 import BeautifulSoup
import json
import urllib
import urllib2
import re
import MySQLdb
# 打开数据库连接
db = MySQLdb.connect("localhost","root","","test",charset='utf8' )
# 使用cursor()方法获取操作游标 
cursor = db.cursor()
 
page = 4
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
        txt_id = txt['id'].encode('UTF-8')
        #txt_id = 'qiushi_tag_120144927'
        query = "select * from employee where TXT_ID=%s"
        n = cursor.execute(query,txt_id) 
        if n:
            continue
        author = txt.find('div',class_='author clearfix')
        author = author.find('h2').get_text()
        if txt.find('div',class_="articleGender")!=None:
            age = txt.find('div',class_="articleGender").get_text()
            sex = txt.find('div',class_="articleGender")

            if sex['class'] == [u'articleGender',u'manIcon']:
                sex = '男'
            else:
                sex = '女'
        else:
            age = 0
            sex = 'None'
        if txt.find('div',class_="thumb"):
            continue
        else:
            content = txt.find('div',class_="content")
            content = content.find('span').get_text()

        #print author,age,content
        TXT_ID = txt_id.encode('UTF-8')
        AUTHOR = author.encode('UTF-8')
        AGE = age
        SEX = sex
        CONTENT = content.encode('UTF-8').strip()

        try:
            # 执行sql语句
            #cursor.execute("INSERT INTO EMPLOYEE(AUTHOR,AGE,CONTENT) VALUES(%s,%s,%s)" % (`AUTHOR`,`AGE`,`CONTENT`))
            sql = "insert into employee(TXT_ID,AUTHOR,AGE,SEX,CONTENT) values(%s,%s,%s,%s,%s)"       
            param = (TXT_ID,AUTHOR,AGE,SEX,CONTENT)
            cursor.execute(sql,param)
            # 提交到数据库执行
            db.commit()
        except:
            # 发生错误时回滚
            db.rollback()

    # 关闭数据库连接
    db.close()

except urllib2.URLError, e:
    if hasattr(e,"code"):
        print e.code
    if hasattr(e,"reason"):
        print e.reason