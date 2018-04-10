#!/usr/bin/python
# -*- coding: UTF-8 -*-
import MySQLdb
#html输出器

class HtmlOutputer(object):
    def __init__(self):
        self.datas = []

    def collect_data(self, data):
        if data is None:
            return
        self.datas.append(data)

    def output_html(self):
        fout = open('output.html', 'w')

        fout.write("<html>")
        fout.write("<body>")
        fout.write("<table>")
        if len(self.datas) == 0:
            print "no data "

        for data in self.datas:
            fout.write("<tr>")
            fout.write("<td>%s</td>" % data['url'])
            # 默认为ascii，所以要在后面修改为utf8
            fout.write("<td>%s</td>" % data['title'].encode('utf8'))
            fout.write("<td>%s</td>" % data['summary'].encode('utf8'))
            fout.write("</tr>")

        fout.write("</table>")
        fout.write("</body>")
        fout.write("</html>")

        fout.close()

    def output_mysql(self):
        # 打开数据库连接
        db = MySQLdb.connect("localhost","root","","test",charset='utf8')
        # 使用cursor()方法获取操作游标 
        cursor = db.cursor()
        if len(self.datas) == 0:
            print "no data "
        for data in self.datas:
            url = data['url']
            title = data['title']
            summary = data['summary'].strip()
        try:
            # 执行sql语句
            #cursor.execute("INSERT INTO EMPLOYEE(AUTHOR,AGE,CONTENT) VALUES(%s,%s,%s)" % (`AUTHOR`,`AGE`,`CONTENT`))
            sql = "insert into baike(url,title,summary) values(%s,%s,%s)"   
            param = (url,title,summary)
            cursor.execute(sql,param)
            # 提交到数据库执行
            db.commit()
        except:
            # 发生错误时回滚
            db.rollback()
            # 关闭数据库连接
            db.close()