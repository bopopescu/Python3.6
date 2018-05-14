#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :2018/4/4 0004 16:37
# @Author :sixgod
a = 1
while 1:
    b = a*9
    a = str(a)
    b = str(b)
    if a == b[::-1]:
        print("{0}*9={1}".format(int(a),b))
        continue
    a = int(a)
    a += 1




