#!/usr/bin/python
import MySQLdb
import sys

#user = input('Please write you name:')
#pwd = input('Please write you password(1-8):')

# conn = MySQLdb.connect(host=input("Host ip:"),port=int(input("Port:")),user=input("User:"),passwd=input("Passwd:"),db=input("DB:"),charset='utf8')
conn = MySQLdb.connect(host=input("Host ip:"),port=3306,user="root",passwd="123456",db=input("DB:"),charset='utf8')
cur = conn.cursor()
# sys.stdout.write('\033[2A')
a=cur.execute(input("請輸入查詢內容："))
print ("{0}".format(a))
input('Press <enter>:')
name = input('name:')
sql='select user from users where user='
b = cur.execute(sql)
print ("{0}".format(b))
#print user,pwd
#cur.execute("insert into users values('user',123)")

cur.close()
conn.commit()
conn.close()

input('Press <enter>:')




