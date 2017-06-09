#!/usr/bin/python3

# a = 10
# b = 3
# a = b = 10    # 为多个变量赋值 变量内存地址共享
a, b = 10, 3    # 同时为多个变量赋值 变量内存地址不一样
c = a / b    # 除法 结果为浮点型
d = a // b    # 整除 结果为整型
e = a % b    # 取余
f = a * b    # 乘法
g = a ** b    # 乘方 a 的 b 次幂
print(type(c), c)
print(type(d), d)
print(type(e), e)
print(type(g), g)

print(a + b, a - b)
print(b // a)

# a = input('please input first num: ')
# b = input('please input second num: ')

print('sum %.1f' %(float(input('please input first num: '))+float(input('please input second num: '))))
