#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
关于元类的学习
"""

def choose_class(name):
    if name == "foo":
        class Foo(object):
            pass
        return Foo
    else:
        class Bar(object):
            pass
        return Bar

def te():
    m_cla = choose_class("foo")
    print m_cla
    m_in = m_cla()
    print m_in


class A(object):
    def __init__(self):
        print "Hello"

    @classmethod
    def say(self, s):
        print s

    def _say(self, s):
        print s

    def __say__(self, s):
        print s

    @staticmethod
    def hi(s):
        print s
        return s


class B(A):
    def __init__(self):
        super(B, self).__init__()
        print "B init"




if __name__ == "__main__":
    a = A()
    a.say(000)
    a._say(111)
    try:
        a.__say__(222)
    except Exception as e:
        print e

    A.say(3333)
    try:
        A.__say__(4444)
    except Exception as e:
        print e

    print a.say
    print A.say

    print a.hi(555)
    print A.hi(666)

    print a.hi
    print A.hi

    print a.say == A.say


    b =B()
    try:
        print b.hi(7777)
        b.say(8888)
    except Exception as e:
        print e

