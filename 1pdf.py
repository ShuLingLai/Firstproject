import numpy as np

#變數型態
str = 'Hello,world!'
x = 10
y = 2.0
boolean = True
none = None

print(str)
print(type(str))
print(type(x))
print(type(y))
print(type(boolean))
print(type(none))

#字元的替換
str = str.replace('H','A')
print(str)

#變數轉型
a = 1
b = float(a)
print(b)

b = int(b)
print(b)

#跳脫字元
str = 'my name is \'world\'!'
print(str)
str = 'my name is \\world!'
print(str)
str = 'my name is \bworld!'
print(str)

#輸入與輸出
name = input('enter your name')
print(name)
print('第一次你好啊',name)
print('第二次你好啊{}'.format(name))


weight = 1.23456789
print('my name is {0: .2f}'.format(weight))

m = input('美金價')
twd = float(m) * 30.5
print(twd)
