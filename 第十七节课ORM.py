#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :2018/5/10
# @Outhor :sixgod

# SQLAlchemy
from sqlalchemy import create_engine, MetaData, Column, Integer, String, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# 初始化数据库连接(echo=True打印操作信息):
engine = create_engine("mysql+pymysql://sixgod:123456@47.93.205.208/test")

# 创建DBSession类型:
DBsession = sessionmaker(bind=engine)
session = DBsession()

# 创建表
metadata = MetaData(engine)
user = Table('users',metadata,
        Column('id',Integer,primary_key=True),
        Column('name',String(10)),
        Column('password',Integer),
        Column('email',Integer,unique=True),
        Column('score',Integer)
             )
metadata.create_all(engine)

# 创建对象的基类:
Base = declarative_base()

class User(Base):
    # 表的名字:
    __tablename__ = 'users'

    # 表的结构:
    id = Column(Integer(), primary_key=True)
    name = Column(String(10))
    password=Column(Integer())
    email=Column(Integer(),unique=True)
    score=Column(Integer())


#查询数据
user=session.query(User).filter_by(id=1).one()
print(user.id,user.score)

# for i in user:
#     print(i.id,i.name,i.score)
#添加数据
# u1=User(name='a',password=1,email=1,score=12)
# u2=User(name='b',password=2,email=2,score=15)
# u3=User(name='c',password=3,email=3,score=21)
# session.add_all([u1,u2,u3])
# session.commit()
#删除用户
# u=session.query(User).filter(User.id=='2').one()
# session.delete(u)
# session.commit()
#修改数据：获取一条数据对象，修改属性并提交即可
# user=session.query(User).filter(User.id==1).one()
# user.score=99
# session.commit()
# session.close()
#******************************************
# engine = create_engine("mysql+pymysql://sixgod:123456@47.93.205.208/sqlalchemy")
# metadata  = MetaData(engine)
#
# teacher = Table("teacher",metadata,
#                 Column("id",Integer,primary_key=True),
#                 Column("name",String(10)),
#                 Column("age",Integer)
#                 )
# metadata.create_all(engine)


