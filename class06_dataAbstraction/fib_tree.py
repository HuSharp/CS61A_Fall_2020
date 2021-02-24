'''
Descripttion: 
version: 
Author: HuSharp
Date: 2021-02-14 18:56:32
LastEditors: HuSharp
LastEditTime: 2021-02-14 19:46:08
@Email: 8211180515@csu.edu.cn
'''
import tree as TreeBuild

def fib_tree(n):
    ''' Fib Tree
    >>> fib_tree(0)
    [0]
    >>> fib_tree(1)
    [1]
    >>> fib_tree(2)
    [1, [0], [1]]
    >>> fib_tree(3)
    [2, [1], [1, [0], [1]]]
    >>> fib_tree(4)
    [3, [1, [0], [1]], [2, [1], [1, [0], [1]]]]
    >>> fib_tree(5)
    [5, [2, [1], [1, [0], [1]]], [3, [1, [0], [1]], [2, [1], [1, [0], [1]]]]]
    >>> TreeBuild.leaves(fib_tree(4))
    [0, 1, 1, 0, 1]
    >>> TreeBuild.leaves(fib_tree(5))
    [1, 0, 1, 0, 1, 1, 0, 1]
    '''
    if n <= 1:
        return TreeBuild.tree(n)
    else:
        left, right = fib_tree(n-2), fib_tree(n-1)
        return TreeBuild.tree(TreeBuild.label(left) + TreeBuild.label(right), [left, right] )

