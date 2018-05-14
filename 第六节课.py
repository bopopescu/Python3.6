#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :2018/4/12
# @Outhor :sixgod
"""
文件操作
参数一：文件名 可以使绝对路径
2：对文件的操作 r读 w写 b二进制 a追加

"""

#全局申明
ENCODING = "utf-8"

# 每次读取文件进行过操作后都需要关闭文件，
# 使用with open("1.txt","r") as f:
#           print(f.read())
# 不用每次都关闭

#读取文件内容
f = open("99乘法表.py","r")
print(f.read())
f.close()
#写入文件，当文件不存在时，直接创建。会覆盖原有文件内容。
a = open("999乘法表.py","w")
a.write("hello")
a.close()
#追加内容,指定编码。
b = open("999乘法表.py","a",encoding=ENCODING)
b.write("hello 哈哈")
b.close()

#文件对象的常用操作
# read()  把文件的所有内容都读取出来，返回一个字符串。
# write() 把字符串data写入到文件中，只接受字符串参数。
#readline() 每次只读取文件的一行数据，返回该行的字符串数据。
#readlines() 读取文件内容，返回一个list，每一行为列表中的一个元素。
# name()    文件名
# fileno()  文件描述符
# close()   关闭文件
# encoding()   文件编码
# closed()      判断文件是否关闭
# seek(offset，whence) offset偏移量（正数向前，负数向后）  whence 0开头 1现在 2末尾
# 控制文件光标，文件需要使用b方式打开。
# tell()          返回文件的光标位置
# truncate(size)     只有写文件用，size保留多少位，0位清空文件。

# 函数  定义：  以关键字def开头，函数名，参数：回车缩进
# def function(arg1,arg2,...):
#     pass
# 函数  调用：   function（1,2,3） 函数名直接传入参数
#封装的一种思想，把细小的功能或者可以缩小的功能封装成一个函数。

# arg1,arg2  形参
# 1,2,3       实参

# def fun(a,*args,**kwargs):
#     pass
# fun(1,2,3,4,a=1,b=2)
# a = 1
# args = 2,3,4            列表
# kwargs = {"a":1,"b":2}  字典

匿名函数：
