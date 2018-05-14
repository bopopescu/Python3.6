#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :2018/4/28
# @Outhor :sixgod
import random
import re

import os
#
# s = "www.aa.a1.com"
# reg = re.compile(r"(a1)")
#
# print(reg.groups(s))


# print(reg.match(s).group(0))
# print(reg.match(s).group(1))
# print(reg.match(s).group(2))
# print(reg.match(s).group(2,3))
# print(reg.match(s).groups())

# s = "ab<h1>xxx</h1>dsafasdf<html>sdfads</html>"
# reg = re.compile(r"(<(?P<tag>\w+)>(.*)</(?P=tag)>)")
# print(reg.match(s))
# print(reg.search(s).group(3))
# print(reg.findall(s))
# print(reg.findall(s)[1])
# print(reg.findall(s)[2])
# reg.split(s)
# reg.findall(s)
# reg.groups(s)


# os.system("ipconfig")
import string

import time

print(os.popen("ipconfig"))

print(string.punctuation)

from datetime import datetime

print(datetime.now())
print(time.time())
print(random.randint(1,2))