#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :2018/4/26 0026 16:28
# @Author :sixgod
import random

a = []
for i in range(0,10):
    a.append(random.randint(1,1000))
a.sort()
print(a)

