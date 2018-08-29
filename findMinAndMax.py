#!usr/bin/python
#coding:utf8
def findMinAndMax(L):
	if len(L) == 0:
		return (None, None)
	Min = Max= L[0]
	for x in L:
		if Min > x:
			Min = x

		if Max <x:
			Max = x

	return(Min,Max)
# 测试
if findMinAndMax([]) != (None, None):
    print('测试失败!')
elif findMinAndMax([7]) != (7, 7):
    print('测试失败!')
elif findMinAndMax([7, 1]) != (1, 7):
    print('测试失败!')
elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
    print('测试失败!')
else:
    print('测试成功!')
