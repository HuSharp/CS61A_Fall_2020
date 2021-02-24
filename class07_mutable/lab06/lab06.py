'''
Descripttion: 
version: 
Author: HuSharp
Date: 2021-02-21 10:02:11
LastEditors: HuSharp
LastEditTime: 2021-02-21 10:23:42
@Email: 8211180515@csu.edu.cn
'''
this_file = __file__


def make_adder_inc(a):
    """
    >>> adder1 = make_adder_inc(5)
    >>> adder2 = make_adder_inc(6)
    >>> adder1(2)
    7
    >>> adder1(2) # 5 + 2 + 1
    8
    >>> adder1(10) # 5 + 10 + 2
    17
    >>> [adder1(x) for x in [1, 2, 3]]
    [9, 11, 13]
    >>> adder2(5)
    11
    """
    "*** YOUR CODE HERE ***"
    add_num = -1
    def adder(b):
        nonlocal add_num
        add_num += 1
        return a + b + add_num
    return adder



def make_fib():
    """Returns a function that returns the next Fibonacci number
    every time it is called.

    >>> fib = make_fib()
    >>> fib()
    0
    >>> fib()
    1
    >>> fib()
    1
    >>> fib()
    2
    >>> fib()
    3
    >>> fib2 = make_fib()
    >>> fib() + sum([fib2() for _ in range(5)])
    12
    >>> from construct_check import check
    >>> # Do not use lists in your implementation
    >>> check(this_file, 'make_fib', ['List'])
    True
    """
    "*** YOUR CODE HERE ***"
    cur_num = 0
    next_num = 1
    def cur_fib():
        nonlocal cur_num, next_num
        cur_num, next_num = next_num, cur_num + next_num
        return next_num - cur_num
    return cur_fib


def insert_items(lst, entry, elem):
    """
    >>> test_lst = [1, 5, 8, 5, 2, 3]
    >>> new_lst = insert_items(test_lst, 5, 7)
    >>> new_lst
    [1, 5, 7, 8, 5, 7, 2, 3]
    >>> large_lst = [1, 4, 8]
    >>> large_lst2 = insert_items(large_lst, 4, 4)
    >>> large_lst2
    [1, 4, 4, 8]
    >>> large_lst3 = insert_items(large_lst2, 4, 6)
    >>> large_lst3
    [1, 4, 6, 4, 6, 8]
    >>> large_lst3 is large_lst
    True
    """
    "*** YOUR CODE HERE ***"
    # pos = []
    # for i in range(len(lst)):
    #     if lst[i] == entry:
    #         pos.append(i)
    # 上面代码修改如下
    '''
    enumerate 用法
    >>> seasons = ['Spring', 'Summer', 'Fall', 'Winter']
    >>> list(enumerate(seasons))
    [(0, 'Spring'), (1, 'Summer'), (2, 'Fall'), (3, 'Winter')]
    >>> list(enumerate(seasons, start=1))       # 下标从 1 开始
    [(1, 'Spring'), (2, 'Summer'), (3, 'Fall'), (4, 'Winter')]
    '''
    pos = [i for i, x in enumerate(lst) if x == entry]

    for i in range(len(pos)):
        lst[ pos[i] + i + 1 : pos[i] + i + 1 ] = [elem]
    return lst

