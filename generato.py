#!usr/bin/python
#coding:utf8
def fib(num):
	n,a,b = 0, 0, 1
	while n< num:
		yield (b)
		a, b = b ,a+b
		n = n+1
	#return 'done'
f = fib(6)
#print f
#g = (x*x for x in range(10))
for n in f:
	print n,
