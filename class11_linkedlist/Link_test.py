'''
Descripttion: 
version: 
Author: HuSharp
Date: 2021-03-03 09:00:27
LastEditors: HuSharp
LastEditTime: 2021-03-08 00:26:07
@Email: 8211180515@csu.edu.cn
'''

class Link :
    empty = ()
    def __init__(self, first, rest=empty):
        assert rest is Link.empty or isinstance(rest, Link)
        self.first = first
        self.rest = rest
        

def sum_link(lnk):
    # if lnk == Link.empty:
    #     return 0
    # return lnk.first + sum_link(lnk.rest)
    res = 0
    while lnk != Link.empty:
        res += lnk.first
        lnk = lnk.rest
    return res

sqaure, odd= lambda x : x * x, lambda x : x % 2 == 1

def range_link(start, end):
    '''
    >>> range_link(3, 6)
    Link(3, Link(4, Link(5)))
    '''
    if start >= end:
        return Link.empty
    else :
        return Link(start, range_link(start+1, end))


def map_link(f, s):
    '''
    >>> map_link(square, range_link(3, 6))
    Link(9, Link(16, Link(25)))
    '''
    if s is Link.empty:
        return s
    else:
        return Link(f(s.first), map_link(f, s.rest))        

# 不用返回值的 map
def map_iter(lnk, f):
    while lnk is not Link.empty:
        lnk.first = f(lnk)
        lnk = lnk.rest
def map_rec(lnk, f):
    if lnk is Link.empty:
        return
    else :
        lnk.first = f(lnk.first)
        map_rec(lnk.rest, f)

def filter_link(f, s):
    '''
    >>> filter_link(odd, range_link(3, 6))
    Link(3, Link(5))
    '''
    if s is Link.empty:
        return s
    if f(s.first):
        return Link(s.first, filter_link(f, s.rest))
    else:
        return filter_link(f, s.rest)

def print_link(link):
    '''
    >>> print_link(range_link(3, 6))
    3
    4
    5
    '''
    while link != Link.empty:
        print(link.first)
        link = link.rest

def display_lnk(lnk):
    if lnk is Link.empty:
        return "NULL"
    strN = "->"
    return strN + str(lnk.first) + display_lnk(lnk.rest)

def add(s, v):
    '''add v to an ordered list s with no repeats, return modified s'''
    sHead = Link(0, s) # 安置一个头指针
    tmp = sHead
    while s != Link.empty:
        if s.first > v:
            tmp.rest = Link(v, s)
            return sHead.rest
        s = s.rest
        tmp = tmp.rest
    # 若直到最后还未找到比 v 大的
    tmp.rest = Link(v)
    return sHead.rest

def add_2(s, v):
    assert s is not Link.empty
    if s.first > v: # 此时进行添加
        s.first, s.rest = v, Link(s.first, s.rest)
    elif s.first < v and s.rest is Link.empty:
        s.rest = Link(v)
    elif s.first < v:
        add_2(s.rest, v)
    return s
    


            