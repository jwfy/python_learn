#! /sur/bin/env python
# -*- coding: utf-8 -*-

import ipdb

ipdb.set_trace()

class MetaClass(object):
    def __new__(cls, cls_name, cls_parent_name, attr):
        print "Creating cLass", cls_name
        print "cls",cls
        print "cls_parent_name", cls_parent_name
        print "attr", attr
        if attr.get("value"):
            cls.value = value
        if attr.get("desc"):
            cls.desc = desc
        return type(cls_name, cls_parent_name, attr)


"""
也是可以采用再独立出来一个类，让A，B，C去继承的
然后在__init__写入value和desc的用途
"""
class Base:

    def __init__(self, value, desc):
        self.value = value
        self.desc = desc

    def __repr__(cls):
        print "这是由元类构建的函数："
        print cls.__name__
        print "======" + cls.desc + "======"
        print "======" + cls.value + "======"


class A(Base):
    __metaclass__ = MetaClass
    types = "int"
    def __init__(self, value, desc):
        super(A, self).__init__(value, desc)


class B(Base):
    __metaclass__ = MetaClass
    types = "char"
    def __init__(self, value, desc):
        super(B, self).__init__(value, desc)

class C(Base):
    __metaclass__ = MetaClass
    types = "boolean"
    def __init__(self, value, desc):
        super(C, self).__init__(value, desc)


class Test():
    a = A(value="222", desc="这是int类型")
    b = B(value="333", desc="这是字符类型")
    c = C(value="444", desc="这是布尔类型")

if __name__ == "__main__":
    te = Test()
    print te.a
    print te.b
    print te.c
