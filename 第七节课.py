#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :2018/4/14
# @Outhor :sixgod
from functools import reduce

# 函数:
# def 定义函数
# 后面跟函数名
# 参数：*args   tuple 元组
#     **args    dict 字典
# return 返回值
# 如：
# def add(x,y):
#     return x+y
# print(add(1,9))

# 匿名函数

# 高阶函数：
# 常用
# sorted(iterable,key,reverse)
# iterable 一个可迭代对象
# key 对什么进行排序
# reverse bool类型，如果为true为反序，默认为false
# a = {"q":1,"w":3,"e":2}
# print(dict(sorted(a.items(),key=lambda x: x[1])))
# print(sorted(a.items(),key=lambda x: x[1]))
#
# def test():
#     for f in range(1,4):
#         return f
#
# q=test()
# print(q)


"""
列表生成式
[exp for val in collection if condition]
[x for x ]
生成器
方法一：(exp for val in collection if condition)
方法二：

(x for x  in range(1,10) if x%2==0)
"""

# return 返回值，下次从头开始执行代码
# yield 返回值，下次取值时从yield下一行代码开始进行
# def jh(a,b):
#     for i in a:
#         for j in b:
#             if i == j:
#                 print(i)
#
# print(jh([1,2,3,4],[2,3]))

# with open("hello.py","r",encoding="utf-8") as f:
#     print(f.read())
#     for i in enumerate(f.read()):
#         print(i)

# f = lambda x:x+x
# b = map(f,[1,2,3,4])
# print(list(b))
# for i in map(f,[1,2,3,4]):
#     print(i)
# def add(x,y):
#     return x+y
# a = reduce(add,[1,2,3,4])
# print(a)
#
# str1="qwe1231"
#
# def is_odd(n):
#     return n % 2 == 1
#
# print(list(filter(is_odd, [1, 2, 4, 5, 6, 9, 10, 15])))

# a=[-4,3,2]
# print(sorted(a,reverse=True))
#
# print(sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower))
# L = dict([('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)])
# for i in L.items():
#     print(i[1])
# print(dict(sorted(L.items(),key=lambda x:x[1],reverse=True)))
# print(sorted(L.items(),key=lambda x:x[1],reverse=True))

# a=list()
# for i in range(1,11):
#     a.append(i*i)
# print(a)
# r = "dsad"
# r = r.title()
# print(r)
#
# a = [x*x for x in range(11) if x%2 == 0]
# print(a)
#
# print([m + n for m in "abc" for n in "123"])

# a = {"a":"1","b":"2"}
# print([k+"="+v for k,v in a.items()])
#
# a = ["a",2,"sda"]
# for i in a:
#     if isinstance(i,str):
#         print(i)
# a = [x for x in range(3)]
# print(a)
# b = (x for x in range(3))
# print(next(b))
# print(next(b))
# print(next(b))
# b = (x for x in range(3))
# for i in b:
#     print(i)
# 1 1 2 3 5 8
# def fib(x):
#     n,a,b = 0,0,1
#     while n<x:
#         yield b
#         a,b = b,a+b
#         n += 1
#     return "done"
# a = fib(3)
# for i in range(3):
#     print(next(a))
# def odd():
#     print('step 1')
#     yield 1
#     print('step 2')
#     yield(3)
#     print('step 3')
#     yield(5)
# a = odd()
# next(a)
# next(a)
# next(a)
#
# def fib(x):
#     n,a,b = 0,0,1
#     while n<x:
#         yield b
#         a,b = b,a+b
#         n += 1
#     return "done"
# for i in fib(6):
#     print(i)

def trangle(n):
    L=[1]
    while len(L)<=n:
        yield L
        L=[1]+[L[x]+L[x+1]for x in range(len(L)-1)]+[1]
for t in trangle(2):
    print(t)

