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

m_cla = choose_class("foo")
print m_cla
m_in = m_cla()
print m_in
