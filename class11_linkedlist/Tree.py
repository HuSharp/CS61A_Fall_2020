'''
Descripttion: 
version: 
Author: HuSharp
Date: 2021-03-06 19:09:41
LastEditors: HuSharp
LastEditTime: 2021-03-08 00:29:27
@Email: 8211180515@csu.edu.cn
'''
class Tree:

    def __init__(self, lable, branches=[]):
        self.lable = lable
        for branch in branches:
            assert isinstance(branch, Tree)
        self.branches = list(branches)

    def __repr__(self):
        if self.branches:
            branch_str = ', ' + repr(self.branches)
        else:
            branch_str = ''
        return 'Tree({0}{1})'.format(repr(self.lable), branch_str)

    def __str__(self):
        '''
        >>> a = ['hello', 'world', '!']
        >>> s = '\n'.join(a)
        >>> s
        'hello\nworld\n!'
        >>> print(s)
        hello
        world
        !
        '''
        return '\n'.join(self.indented())

    # 缩进函数方便观察
    def indented(self):
        lines = []
        for b in self.branches:
            # 对每一个分支都进行缩进， 并将缩进后得到的字符串，加到总共的字符串中
            for line in b.indented():
                lines.append(' ' + line)
        return [str(self.lable)] + lines
                

    def is_leaf(self):
        return not self.branches

def fib_tree(n):
    """A Fibonacci tree.
    >>> print(fib_tree(4))
    3
      1
        0
        1
      2
        1
        1
          0
          1
    """
    if n == 0 or n == 1:
        return Tree(n)
    else :
        left = fib_tree(n-2)
        right = fib_tree(n-1)
        fib_n = left.lable + right.lable
        return Tree(fib_n, [left, right])

def height(tree):
    if tree.is_leaf():
        return 0
    else :
        return 1 + max([height(b) for b in tree.branches])

def leaves(tree):
    if tree.is_leaf():
        return [tree.lable]
    else :
        all_leaves = []
        for b in tree.branches:
            all_leaves.extend(leaves(b))
    return all_leaves
        # return [leaves(b) for b in tree.branches]

# 进行修建
def prune(t, n):
    '''Prune all sub-trees whose label is n'''
    t.branches = [b for b in t.branches if b.label != n]
    for b in t.branches:
        prune(b, n)


def print_tree(t, indent=0):
    print(" " * indent + t.label)
    for b in t.branchesa:
        print_tree(t, indent + 1)