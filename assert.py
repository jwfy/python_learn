#! /usr/bin/ env python
# -*- coding: utf-8 -*-

""" 本代码主要是说明raise 和 assert 的使用
"""


def fun1(a=3):
    if a > 5:
        print a
    else:
        assert "a is small than 3"


def fun2(a=3):
    try :
        b = a / 0
        #raise "error"
        print b
        raise ZeroDivisionError
    except ZeroDivisionError:
        print "不能除以0啊"
    except Exception as e:
        print e
    print a
    print "use try-except"

def fun3(a=3):
    try:
        b = a / 0
        print b
    except ZeroDivisionError:
        print "使用print 函数 捕获异常"
    except Exception as e:
        print e
    print a
    print "use assert"

def fun4(a=3):
    try:
        if a == 3:
            raise Error
        print a
    except Exception as e:
        print "捕获异常"

qq = Exception()
def fun5(a=3):
    try:
        if a == 3:
            raise ZeroDivisionError
        if a == 4:
            raise qq
    except qq:
        print "haha"
    except ZeroDivisionError:
        print "a==3 "
    except Exception as e:
        print e
    print a-3



if __name__ == "__main__":
    fun1()
    fun2()
    fun3()
    fun4()
    fun4(5)
    fun5()
    fun5(4)
    #fun5(5)

"""
结论：
    使用正常的try-catch 可以捕获异常
    使用 raise *** 可以
"""
