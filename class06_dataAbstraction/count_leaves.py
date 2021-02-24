'''
Descripttion: 
version: 
Author: HuSharp
Date: 2021-02-14 19:10:23
LastEditors: HuSharp
LastEditTime: 2021-02-18 16:49:52
@Email: 8211180515@csu.edu.cn
'''

import tree as TREE
import fib_tree as FIB

def count_leaves(t):
    '''count leaves nums of the tree 
    >>> count_leaves(FIB.fib_tree(0))
    1
    >>> count_leaves(FIB.fib_tree(1))
    1
    >>> count_leaves(FIB.fib_tree(2))
    2
    >>> count_leaves(FIB.fib_tree(3)) 
    3
    >>> count_leaves(FIB.fib_tree(4))
    5
    >>> count_leaves(FIB.fib_tree(5))
    8
    '''
    if TREE.is_leaf(t):
        return 1
    else:
        leavesCnt = [count_leaves(b) for b in TREE.branches(t)]
        return sum(leavesCnt)

leaves = count_leaves(FIB.fib_tree(5))