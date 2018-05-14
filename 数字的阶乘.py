#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :2018/4/4 0004 15:52
# @Author :sixgod
number = int(input("number:"))
sum = 1
if number > 0:
    for i in range(1,number+1):
        sum *= i
    print("{0}的阶乘为:{1}".format(number, sum))
elif number == 0:
    print("{0}的阶乘为:0".format(number))
else:
    print("负数没有阶乘")

input("Press <enter>")