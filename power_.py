#!usr/bin/python
#coding:utf8

def power_(x,n):
	s=1
	while n>0:
		n=n-1
		s=s*x

	return s

print power_(5,5)

