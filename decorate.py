#! /usr/bin/ env python
# -*- coding: utf-8 -*-

""" 本代码主要是说明装饰器的使用
1: 说明了装饰器中可以想被装饰的函数中传值（类里面，函数没有成员或者变量一说）
"""

import ipdb

def deco(func):
    def f(self, *args, **kwargs):
        ipdb.set_trace()
        self.aaa = 111
        return func(self, *args, **kwargs)
    return f


def deco1(v1):
    def wrap(func):
        def f(self, *args, **kwargs):
            print v1
            for k, v in kwargs.items():
                print k,v
            self.v1 = v1
            return func(self, *args, **kwargs)
        return f
    return wrap

"""
v1 就是 装饰器 传入的 值
func 就算被包装的函数
self 就算类 args等都是其他函数
"""

class A:

    @deco
    def test1(self, a):
        try:
            print a
            print self.aaa
        except Exception as e:
            print e
        
    @deco
    def test2(self, a):
        try:
            print a
            print self.aaa
        except Exception as e:
            print e

    @deco1(3333)
    def test3(self, *args, **kwargs):
        print 11111
        print self.v1



if __name__ == "__main__":
    a = A()
    a.test1(1)
    a.test2(2)
    ipdb.set_trace()
    a.test3(3, 222, a=3, b=4)
