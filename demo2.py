#/usr/bin/python
#coding:utf8
import MySQLdb
# 打开数据库连接
db = MySQLdb.connect("localhost","root","","test" )

# 使用cursor()方法获取操作游标 
cursor = db.cursor()
AUTHOR = "hhhhhhhhhhhhhhhhhhhhhhhhhhhhhh"
AGE = 16
CONTENT = "CONTENT"
value = ['AUTHOR', 16, 'CONTENT']
# SQL 插入语句
#sql = """INSERT INTO EMPLOYEE(AUTHOR,AGE,CONTENT) VALUES ('hhhhhhhhhhhhhhh', 18, 'test')"""
try:
   # 执行sql语句
   cursor.execute("INSERT INTO EMPLOYEE(AUTHOR,AGE,CONTENT) VALUES(%s,%s,%s)" % (`AUTHOR`,AGE,`CONTENT`))
   #cursor.execute(sql)
   # 提交到数据库执行
   db.commit()
except:
   # 发生错误时回滚
   db.rollback()

# 关闭数据库连接
db.close()