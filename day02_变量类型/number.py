#!/usr/bin/python 3.5
# -*- coding: UTF-8 -*-

# Python 数据类型 数字 numbers
# Python 数字类型包含四大变量类型 整型 长整型 浮点型 复数
# Python 3.0+ 长整型合并入整型中

# int
a = 1001
print('a:', id(a), type(a), a)
del a

# Python 3.0 后无 long 类型
# a = 199308171314L
# print('a:', id(a), type(a), a)
# del a

# float
a = 1.23
print('a:', id(a), type(a), a)
del a

# complex
a = 4j
print('a:', id(a), type(a), a)
del a

# bool
a = True
print('a:', id(a), type(a), a)
del a

if True == 1:
    print(1)
else:
    print(2)

if False == 0:
    print(0)
else:
    print(2)