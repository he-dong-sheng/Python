#!usr/bin/python
#coding:utf8
print sorted([36, 5, -12, 9, -21])
#按绝对值大小排序
print sorted([36, 5, -12, 9, -21], key=abs)
#对字符串的排序，是按照ASCII的大小比较的
print sorted(['bob', 'about', 'Zoo', 'Credit'])
print sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower)
#反向排序，不必改动key函数，可以传入第三个参数reverse=True
print sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower, reverse=True)

#第一个：按名字排序
L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]

def by_name(t):
    return t[0].lower()
L2 = sorted(L, key=by_name)
print(L2)
#第二个：按分数排序
L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]

def by_score(t):
    return t[1]
L2 = sorted(L, key=by_score, reverse=True)
print(L2)
