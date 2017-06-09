#!/usr/bin/python 3.5
# -*- coding: UTF-8 -*-

# Python 每个变量在使用前都必须赋值 变量赋值以后该变量才会被创建
# Python 变量定义、赋值无需类型声明 基本的赋值运算符 =
# Python 五大标准数据类型 numbers string list tuple dictionary
# Python

i = 1
print(id(i), type(i), i)
del i

i = 'ab'
print(id(i), type(i), i)
del i

i = 'a.com#lala$x**///\\n\n'    # Python 中单引号支持解析转义字符
print(id(i), type(i), i)
del i

i = ('alsjfdsikfjskdjoaseifrhfjsdnao093274;ajasilef\\r9//.,.><><{dfs\}'
    'fsahsdhfaosfdsfdsdfdsf')
print(id(i), type(i), i)
del i

i = ['lalala', 1993, 10]
print(id(i), type(i), i)
del i

i = 'c', 12, [1, 'hello']
print(id(i), type(i), i)
del i