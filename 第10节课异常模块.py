#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :2018/4/22
# @Outhor :sixgod
# class a(object):
#     try:
#         print(2 / 0)
#     except Exception as e:
#         print("除数不能为0")
#         raise e
#     finally:
#         print("lalalla")

# 模块：
# 时间模块：datetime
# from datetime import datetime
# print(datetime.now())
# print(datetime.now().year)
# print(datetime.now().month)
# print(datetime.now().day)
#
# a = datetime.now().strptime("2018-04-22","%Y-%m-%d")
# print(a)
#
# # timedelta
#
# import time
# a = time.time()  #time.time()时间戳 从1970-01-01开始，到现在的秒数
# time.sleep(3)    #暂停3秒
# b = time.time()
# print("{0}".format(b-a))

class Person(object):
    name = 'xxx'
    hair = 'blond'

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __del__(self):
        print('{0} {1}: __del__'.format(Person.name, self.name), end=' ')


def f(flag=False):
    p1 = Person('Jim', '30')
    if flag:
        print(p1.name, Person.name, p1.age, p1.hair, Person.hair)


# f(True)
print('Start.', end=' ')
f()
print('End.', end=' ')


