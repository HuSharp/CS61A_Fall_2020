'''
Descripttion: 
version: 
Author: HuSharp
Date: 2021-02-14 19:46:41
LastEditors: HuSharp
LastEditTime: 2021-02-19 10:29:09
@Email: 8211180515@csu.edu.cn
'''

import tree as TREE
import fib_tree as FIB


def increment_leaves(t):
    '''Return a tree like t but leaves value increable 1
    but this function just increable leaves, not root
    '''
    if TREE.is_leaf(t):
        return TREE.tree(TREE.label(t) + 1)

    else:
        bs = [increment_leaves(b) for b in TREE.branches(t)]
        return TREE.tree( TREE.label(t), bs)

def increment(t):
    '''Return a tree like t but leaves value increable 1
    and this function not only increable leaves, but also root
    '''
    return TREE.tree( TREE.label(t) + 1, [increment(b) for b in TREE.branches(t) ] )
