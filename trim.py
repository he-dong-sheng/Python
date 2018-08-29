#!usr/bin/python
# coding:utf8


def trim_(s):
    while s[:1] == ' ':
        s = s[1:]

    while s[-1:] == ' ':
        s = s[:-1]

    return s


if trim_('hello  ') != 'hello':
    print('测试失败!')
elif trim_('  hello') != 'hello':
    print('测试失败!')
elif trim_('  hello  ') != 'hello':
    print('测试失败!')
elif trim_('  hello  world  ') != 'hello  world':
    print('测试失败!')
elif trim_('') != '':
    print('测试失败!')
elif trim_('    ') != '':
    print('测试失败!')
else:
    print('测试成功!')
