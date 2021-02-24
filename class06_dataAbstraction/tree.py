'''
Descripttion: 
version: 
Author: HuSharp
Date: 2021-02-14 18:15:33
LastEditors: HuSharp
LastEditTime: 2021-02-14 20:11:25
@Email: 8211180515@csu.edu.cn
'''
def tree(label, branches=[]):
    for branch in branches:
        assert is_tree(branch), 'branches must tree!  '
    return [label] + list(branches)

def label(tree):
    return tree[0]

def branches(tree):
    return tree[1:]

def is_tree(tree):
    if type(tree) != list or len(tree) < 1:
        return False
    for branch in branches(tree):
        if not is_tree(branch):
            return False
    return True

''' 若为 leaf 那么 branch 为空 而
>>>bool([])
False
'''
def is_leaf(tree):
    return not branches(tree)

def leaves(tree):
    '''Return a list containing the leaf labels  of tree
    >>> leaves(FIB.fib_tree(5))

    '''
    if is_leaf(tree):
        return [label(tree)]
    else:
        return sum( [leaves(b) for b in branches(tree)] , [])

def print_tree(tree, level=0):
    print(level * 5 *' ' + str(label(tree)))
    for b in branches(tree):
        print_tree(b, level + 1)