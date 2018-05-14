#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :2018/5/8
# @Outhor :sixgod
import pymysql

conn = pymysql.connect(host="47.93.205.208",port=3306,user="sixgod",passwd="123456",db="test")
cur = conn.cursor()

cur.execute("show tables;")
cur.execute("select * from sixgod")
data = cur.fetchall()
print(data)

cur.close()
conn.close()

