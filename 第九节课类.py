#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :2018/4/20 0020 9:20
# @Author :sixgod
# class Student(object):
#
#     def __init__(self, name, score):
#         self.name = name
#         self.score = score
#
#     def print_score(self):
#         print("{0}:{1}".format(self.name,self.score))
#
#     def get_grade(self):
#         if self.score >= 90:
#             return "A"
#         elif self.score >= 60:
#             return "B"
#         else:
#             return "C"
# student = Student("a",99)
# print(student.name)
# student.name = 99
# print(student.name)
#
# print(student.name,student.get_grade())



# class A(object):
#     #
#     def __init__(self, name):
#         self.name = name
#         print("init class A")
#     def hello(self):
#         print("hello {0}".format(self.name))
# a = A("ajing")
# a.hello()



# class Animal(object):
#     def run(self):
#         print("Animal is running")
#
# class Cat(Animal):
#     def run(self):
#         print("this is cat!")
#     def name(self):
#         print("name is doudou!")
# class Dog(Animal):
#     pass
#
# dog = Dog()
# cat = Cat()
# dog.run()
# cat.run()

class Student(object):

    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    def get__name(self):
        return self.__name

    def get__score(self):
        return self.__score

    def set__score(self,score):
        if 0 <= score <= 100:
            self.__score = score
        else:
            raise ValueError("bad score")
    def print_score(self):
        print("{0}:{1}".format(self.__name,self.__score))
student = Student("a",-60)
print(student.get__name())
print(student.get__score())
print(student.set__score(60))



class Student(object):
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender
    def get__gender(self):
        return self.__gender
    # def set__gender(self,gender):
    #     if gender == "男" and gender == "女":
    #          self.__gender = gender
    #     else:
    #          raise ValueError("bad gender")

bart = Student('Bart', 'male')
print(bart.get__gender())
# if bart.get__gender() != 'male':
#     print('测试失败!')
# else:
#     bart.set__gender('female')
#     if bart.get__gender() != 'female':
#         print('测试失败!')
#     else:
#         print('测试成功!')