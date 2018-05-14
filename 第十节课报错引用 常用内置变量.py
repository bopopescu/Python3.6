#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :2018/4/23 0023 15:53
# # @Author :sixgod
# try:
#     print('try...')
#     r = 10 / 0
#     print('result:', r)
# except ZeroDivisionError:
#     raise ZeroDivisionError()
# finally:
#     print('执行我！')
# print('END')





def foo(s):
    return 10 / int(s)

def bar(s):
    return foo(s) * 2

# def main():
#     try:
#         bar('0')
#     except Exception as e:
#         logging.exception(e)
#
# main()
# print('END')

from datetime import datetime
# import time
#
# now = time.time()
# print(datetime.utcfromtimestamp(now))
cday = datetime.strptime("2015-6-1",'%Y-%m-%d')
print(cday)





