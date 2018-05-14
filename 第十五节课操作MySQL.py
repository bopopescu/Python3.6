#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :2018/5/5
# @Outhor :sixgod
import pymysql

conn = pymysql.connect(host="47.93.205.208",port=3306,user="sixgod",password="123456",db="test")
cur = conn.cursor()

try:
    cur.execute("insert into sixgod(id,name) values(3,'a');") # 执行sql语句
    conn.commit()  # 提交到数据库执行
except:
   conn.rollback() # 如果发生错误则回滚

cur.close()#关闭游标
conn.close()#释放数据库资源


