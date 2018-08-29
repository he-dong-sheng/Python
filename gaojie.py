#!usr/bin/python
#coding:utf8
def add(x,y,f):
	return f(x) + f(y)
print(add(-5, 6, abs))

max, min = min, max
print(max(1, 2, 3, 4, 5))
print(min(1, 2, 3, 4, 5))
####
print list(map(str, [1, 2, 3, 4, 5, 6, 7, 8, 9]))
###
def fn(x, y):
	return x * 10 + y
res = reduce(fn, [1, 3, 5, 7, 9])
print res
####
def char2num(s):
	digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
	return digits[s]
print reduce(fn, map(char2num, '13579'))#'13579'不是一个整体，是单独的字符

def normalize(name):
	return name[0].upper() + name[1:].lower()
# 测试:
L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)

def prod(L):
	def f(x,y):
		return x*y
	return reduce(f,L)
print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))
if prod([3, 5, 7, 9]) == 945:
    print('测试成功!')
else:
    print('测试失败!')

def str2float(s)
	DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
	def char2num(s):
	    return DIGITS[s]
	dp = s.find('.')
	if dp>0:
	    return reduce(lambda x,y:x*10+y,([0]+list(map(char2num, s[:dp]))))+reduce(lambda x,y:x*0.1+y,(list(reversed(list(map(char2num, s[(dp+1):]))))+[0]))
	else:
	    return reduce(lambda x,y:x*10+y,([0]+list(map(char2num, s))))

print('str2float(\'123.456\') =', str2float('123.456'))
if abs(str2float('123.456') - 123.456) < 0.00001:
    print('测试成功!')
else:
    print('测试失败!')
