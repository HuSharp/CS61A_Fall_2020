'''
Descripttion: 
version: 
Author: HuSharp
Date: 2021-02-03 10:34:16
LastEditors: HuSharp
LastEditTime: 2021-02-03 12:10:11
@Email: 8211180515@csu.edu.cn
'''
def fib(x):
    """
    # 输入测试样例
    >>> fib(1)
    0
    >>> fib(2)
    1
    >>> fib(3)
    1
    >>> fib(4)
    2
    >>> fib(8)
    13
    """
    if x == 1:
        return 0
    pred, cur = 0, 1 # init start num
    cnt = 1 # position of num in sequence
    while cnt < x:
        pred, cur = cur, pred + cur
        cnt += 1
    return cur

def fib_simplify(x):
    """
    # 输入测试样例
    >>> fib_simplify(1)
    0
    >>> fib_simplify(2)
    1
    >>> fib_simplify(3)
    1
    >>> fib_simplify(4)
    2
    >>> fib_simplify(8)
    13
    """
    pred, cur = 1, 0 # init start num
    cnt = 1 # position of num in sequence
    while cnt < x:
        pred, cur = cur, pred + cur
        cnt += 1
    return cur

