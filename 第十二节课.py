#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :2018/4/27 0027 8:30
# @Author :sixgod
'''
加密 hashlib


'''
import codecs
import hashlib
# python 2
# m = hashlib.md5()
# src = "123456"
# m.update(src)
# print(m.hexdigest())

# python 3
# md5 = hashlib.md5("123".encode("utf-8"))
# src = bytes("123456",encoding="utf-8")
# md5.update(src)
# print(md5.hexdigest())
import random

'''
频繁进行读写，可以先写到内存中，之后再统一刷新。
StringIO 只能存字符串
bytesIO 进行相对应的二进制转换，可以存很多类型

'''
from io import StringIO,BytesIO

bytesIO = BytesIO()
bytesIO.write("123".encode("utf-8"))
print(bytesIO.getvalue())

stringIO = StringIO()
stringIO.write("123")
print(stringIO.getvalue())
# stringIO.truncate(0) #清除
# print(stringIO.getvalue())
# test = dict(a=1)
# print(bytes(str(test).encode("utf-8")))

'''
json 模块 把字符串转换成python对象使用json.loads()
            吧python对象转换为字符串json.dumps()
            操作文件json.load()
joon.dump(s,f) 把字符串s直接写入到文件中去            
           
'''

# json.loads()
# a= '''[{"a":1},{"b":2}]'''
# a = json.loads(a)
# print(a[0]["a"])

# json.dumps()
# 将python对象转化为字符串

# a = dict(b=1,c=2)
# with codecs.open("1.txt","w") as f:
#     json.dump(a,f)
import hashlib

# md5 = hashlib.md5()
# md5.update("123".encode("utf-8"))
# print(md5.hexdigest())

#
# db = {
#     "michael": "e10adc3949ba59abbe56e057f20f883e",
#     "bob": "878ef96e86145580c38c87f0410ad153",
#     "alice": "99b1c2188db85afee403b1536010c2c9"}
#

# def login(user,password):
#     pwd = db.get(user)
#     print(pwd)
#     md5 = hashlib.md5()
#     md5.update(password.encode("utf-8"))
#     pd = md5.hexdigest()
#     print(pd)
#     if pwd == pd:
#         return 1
#
# login("michael","123456")

# md5 = hashlib.md5()
# md5.update("dsad".encode("utf-8"))
# print(md5.hexdigest())
# s = "123456"
# print(hashlib.md5(s.encode("utf-8")).hexdigest())
# import json
# test = '[{"a": 1, "aa": 11, "aaa": 111}, {"b": 2, "bb": 22, "bbb": 222}, {"c":3}]'
# print(type(test))
# newTest = json.loads(test)
# print(type(newTest))
# print(newTest[0]["a"])
# xxx = json.dumps(newTest)
# print(type(xxx))
#
# test = {"a": 1, "b": 2}
# with codecs.open("1.txt", "w") as f:
#     json.dump(test, f)
#
# with codecs.open("1.txt","r") as f:
#     a = json.load(f)
#     print(a)
#     print(type(a))









