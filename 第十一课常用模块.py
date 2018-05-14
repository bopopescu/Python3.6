#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :2018/4/24
# @Outhor :sixgod
'''
datetimne time
from datetime import datetime
import time

time.time()  获取时间戳
time.sleep()   暂停某时刻
datetime.now() 当前日期
datetime.now().year 年
datetime.now().month 月
datetime.now.strftime("%Y-%m-%d")
datetime.now.strptime("%Y-%m-%d")

'''
import sys

'''
日志记录模块 logging
日志的几个级别
debug
info
warning
error
critical
'''
import logging

logging.basicConfig(level=logging.DEBUG)


logger = logging.debug("debug")
logger = logging.info("info")
logger = logging.warning("warning")
logger = logging.error("error")

'''
os 模块

os.name
nt  则为Windows系统
posix  则为Unix系统
os.system(cmd) 执行系统命令，但是没有返回结果
result = os.popen(cmd)
result.read()

os.listdir("C:") 列出目录下的文件 ls
os.chdir("..")  改变目录 cd 
os.getcwd()   #pwd
os.mkdir("test")  mkdir
os.remove("test.txt") 删除文件
os.rmdir("test") 删除目录
os.rename("1.txt","2.txt") 重命名 1改为2
os.linesep() #换行符

if not os.path.exists("test"):
    os.mkdir("test")

os.path.abspath("./") 绝对路径

'''
'''
import sys
print(sys.argv[1])

print(sys.stdout)
f = open("1.log","w")
sys.stdout = f
print("hell")


'''
'''
random 随机模块

print(random.randint(1,100))
随机生成1-100

print(random.randange(1,100,2))
1,3,5,7,9

random.sample([1,2,3,4,5,6,7],2)

import string
print(string.ascii_letters) 大小写字母
print(string.digits)数字
print(string.ascii_lowercase)小写
print(string.ascii_uppercase)大写
print(string.printable)
print(string.punctuation)特殊字符
print(string.hexdigits)16进制


'''
import random
#
# for i in range(1,1001):
#     print(random.randint(1,6))


import string
# print(string.ascii_letters[1:7])

print("".join(random.sample(string.ascii_letters,6)))

