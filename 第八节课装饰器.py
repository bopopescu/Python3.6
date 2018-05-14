#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :2018/4/18 0018 9:53
# @Author :sixgod
# def add(fun):
#         def hell(name):
#             print("*******************")
#             fun(name)
#             print("*******************")
#         return hell
# @add
# def hello(name):
#     print("hello {0}".format(name))
#
# hello("sixgod")

# def deco(arg):
#     def _deco(func):
#         def __deco():
#             print("before %s called [%s]." % (func.__name__, arg))
#             func()
#             print("  after %s called [%s]." % (func.__name__, arg))
#         return __deco
#     return _deco

# @deco("mymodule")
# def myfunc():
#     print(" myfunc() called.")
#
# @deco("module2")
# def myfunc2():
#     print(" myfunc2() called.")
#
# myfunc()
# myfunc2()
# import time
# def decorator(name):
#     def dec(fun):
#         def wrapper():
#             print("Author:{0}".format(name))
#             start_time = time.time()
#             fun()
#             end_time = time.time()
#             print(end_time - start_time)
#         return wrapper
#     return dec
# @decorator("sixgod")
# def fun():
#     time.sleep(1)
# fun()
#
# # (' '.join("{0}x{1}={2}".format(x, y, x*y) for x in range(1, y+1) ) for y in range(1, 10))
# # "{0}x{1}={2}".format(x,y,x*y) for x in range(1,y+1) for y in range(1,10))
# print("\n".join(" ".join("{0}x{1}={2}".format(x,y,x*y) for x in range(1,y+1) )for y in range(1,10)))
# def deco(name):
#     def deco_1(fun):
#         def deco_2(x,y):
#             print("Author:{0}".format(name))
#             fun(x,y)
#         return deco_2
#     return deco_1
# @deco("sixgod")
# def add(x,y):
#     print("{0}+{1}={2}".format(x,y,x+y))
# add(1,2)

# number = int(input("number:"))
# for i in range(1,number+1):
#     for j in range(1,number):
#         print("*",end=" ")
#     print("*")

# def f(n):
#     a = n
#     for i in range(1,n):
#         a *= i
#     return  a
# print(f(1))

# def f(n):
#     if n == 1:
#         return 1
#     else:
#         return  n * f(n-1)
# print(f(3))

# def init(data):
#     data["first"] = {}
#     data["middle"] = {}
#     data["last"] = {}
# storage = {}
# init(storage)
#
# me = "sixgod"
# storage["first"]["six"] = [me]


# def lookup(data,label,name):
#     return data[label].get(name)
# print(lookup(storage,"first","six"))
# print(storage["first"]["six"])
#
# def inc(x):
#     x[0]+=1
# foo = [10]
# inc(foo)
# print(foo)

# def hell1(name,age):
#     return name,age
# print(hell1(age="17",name="yjj"))
#
# def f(*name):
#     print("hello {0}".format(name))
# f()

def a(x):
    if x == 0:
        return 1
    else:
        return x * a(x-1)
print(a(1))




