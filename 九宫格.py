#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :2018/4/11 0011 9:15
# @Author :sixgod
"""
-------------
\ A \ B \ C \
\ D \ E \ F \
\ G \ H \ I \
-------------
填入1-9使横竖斜相加等于15
解析：
A 可能是1-9中的任意一个数字
B 可能是除了A的1-9中的任意一个
C 可能是除了A，B的1-9中的任意一个
D 依次类推。。。
E  。。。
"""

sum = 1
for A in [x for x in range(1,10)]:
    for B in [x for x in range(1,10) if x != A]:
        for C in [x for x in range(1,10) if x != A and x != B]:
            for D in [x for x in range(1,10) if x != A and x != B and x != C]:
                for E in [x for x in range(1,10) if x != A and x != B and x != C and x != D]:
                    for F in [x for x in range(1,10) if x != A and x != B and x != C and x != D and x != E]:
                        for G in [x for x in range(1,10) if x != A and x != B and x != C and x != D and x != E and x != F]:
                            for H in [x for x in range(1,10) if x != A and x != B and x != C and x != D and x != E and x != F and x != G]:
                                for I in [x for x in range(1,10) if x != A and x != B and x != C and x != D and x != E and x != F and x != G and x != H]:
                                    if A+B+C == D+E+F == G+H+I == A+D+G == B+E+H == C+F+I == A+E+I == G+E+C:
                                        print('''
                                        第{9}种方法：
                                        -------------
                                        | {0} | {1} | {2} |
                                        | {3} | {4} | {5} |
                                        | {6} | {7} | {8} |
                                        ------------- '''.format(A,B,C,D,E,F,G,H,I,sum))
                                        sum += 1

input("Press <enter>")