#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :2018/4/4 0004
# @Author :sixgod
str1 = input("str:")
shuzi,zimu,kongge,qita = 0,0,0,0
for i in str1:
    if i.isdigit():
        shuzi += 1
    elif i.isspace():
        kongge += 1
    elif i.isalpha():
        zimu += 1
    else:
        qita += 1
print("数字：{0} "
      "字母：{1}"
          "空格：{2}"
          "其他：{3}".format(shuzi,zimu,kongge,qita))












