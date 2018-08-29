#!usr/bin/python
#coding:utf8
#在代码运行期间动态增加功能的方式，称之为“装饰器”（Decorator）
def now():
	print('2018-4-4')
f = now
f()
now.__name__
f.__name__