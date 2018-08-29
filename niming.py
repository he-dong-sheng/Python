#!usr/bin/python
#coding:utf8
f = lambda x: x*x
print f(5)

#def build(x, y):
#    return lambda: x * x + y * y
#print build(1, 2) #返回的是匿名函数，没名字怎么调用呢？
L = list(filter(lambda n: n % 2==1,range(1,20)))
print L