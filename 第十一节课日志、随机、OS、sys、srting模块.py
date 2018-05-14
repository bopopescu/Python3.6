#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :2018/4/25 0025 8:52
# @Author :sixgod
'''
日志记录模块 logging
日志的几个级别
debug
info
warning
error
crirical
'''
import logging

# logging.basicConfig(level=logging.DEBUG)
# logger = logging.getLogger(__name__)
#
# logger.debug("debug")
# logger.info("info")
# logger.warning("warning")
# logger.error("error")
# logger.critical("critical")


# if os.name == "nt":
#     pass
# elif os.name == "posix":
#     pass
# import string
# print("".join(random.sample(string.hexdigits+string.punctuation,6)))

# import random
#
# class ShanZi(object):
#     def __init__(self):
#         self.number1 = 0
#         self.number2 = 0
#         self.number3 = 0
#         self.number4 = 0
#         self.number5 = 0
#         self.number6 = 0
#
#     def count(self):
#         for i in range(1,10001):
#             number = random.randint(1,6)
#             if number == 1:
#                 self.number1 += 1
#             if number == 2:
#                 self.number2 += 1
#             if number == 3:
#                 self.number3 += 1
#             if number == 4:
#                 self.number4 += 1
#             if number == 5:
#                 self.number5 += 1
#             if number == 6:
#                 self.number6 += 1
#
#     def cishu(self):
#         print("1:{0}".format(self.number1))
#         print("2:{0}".format(self.number2))
#         print("3:{0}".format(self.number3))
#         print("4:{0}".format(self.number4))
#         print("5:{0}".format(self.number5))
#         print("6:{0}".format(self.number6))
#
# def main():
#     shanzi = ShanZi()
#     shanzi.count()
#     shanzi.cishu()
#
# if __name__ == '__main__':
#     main()

# import random
# import string
#
# print("".join(random.sample(string.hexdigits,6)))


import random

class ShanZi(object):
    def __init__(self):
        self.number1 = 0
        self.number2 = 0
        self.number3 = 0
        self.number4 = 0
        self.number5 = 0
        self.number6 = 0

    def touzhi(self):
        for i in range(1,1001):
            number = random.randint(1,6)
            if number == 1:
                self.number1 += 1
            if number == 2:
                self.number2 += 1
            if number == 3:
                self.number3 += 1
            if number == 4:
                self.number4 += 1
            if number == 5:
                self.number5 += 1
            if number == 6:
                self.number6 += 1

    def count(self):
        print("1:{0}".format(self.number1))
        print("2:{0}".format(self.number2))
        print("3:{0}".format(self.number3))
        print("4:{0}".format(self.number4))
        print("5:{0}".format(self.number5))
        print("6:{0}".format(self.number6))

def main():
        shanzi = ShanZi()
        shanzi.touzhi()
        shanzi.count()

if __name__ == "__main__":
    main()









