#!/usr/bin/python 3.5
# -*- coding: UTF-8 -*-

# Python 数据类型 字符串
# 字符串定义 单引号或双引号标识 两者效果一致没有区别
# 定义多行字符串使用 三个单引号或双引号

a = 'mikenut@qq.com'
print(a[0:4])
print(a[-8:])

# a[0] = 'x'    # 不可赋值更改

b = r'Hello \t World'   # 无论单引号双引号都解析转移字符 但 r 可取消转义
print(b)
del b

c = 'Mike Lee \\n'    # 取消转义亦可使用转义符 \
print(c)

d = u'mikenut%40qq.com'   # u
# print(d)

e = '''Hello, Mike.
This is Joey.
Come with me!'''
# print(e)

f = 'love'
print(f + 'you')    # 连接字符串
print(f * 3)    # 重复字符串 n 次