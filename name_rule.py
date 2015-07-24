#! /usr/bin/env python
# -*- coding: utf-8 -*-

# time: 2015-07-03

"""
主要是涉及到python里面变量名的使用规则
"""

class TestA(object):

    def __init__(self):
        self._c = 0
        self.__d = 0
        print "类对象的初始化"

    def __sum1(self, a, b):
        """
        似有函数，以2个下划线开头
        """
        self._c = a + b
        self.__d = 5

    def sum2(self, a, b):
        """
        普通函数
        """
        self._c = a + b
        self.__d = 10

    def _deal(self):
        print self._c
        print self.__d


if __name__ == "__main__":
    a = TestA()
    try:
        a.sum2(3,4)
        print a._c
        print a.__d
    except Exception as e:
        print e

    try:
        a.__sum1(3,5)
        print a._c
        print a.__d
    except Exception as e:
        print e

    a._deal()

"""
结果如下


类对象的初始化
7
'TestA' object has no attribute '__d'
'TestA' object has no attribute '__sum1'
7
10


说明了 __**  均是属于似有函数，子类无法调用，只能是通过函数内部其他可以调用
的函数去调用执行似有函数

a.__sum1 函数就无法执行，然后跳出了try-catch了，直接输出了no attribute ...

所以在a._deal 函数执行的时候，_c 和 __d 均是执行sum2 函数所赋值的值

"""




