'''
Descripttion: 
version: 
Author: HuSharp
Date: 2021-02-09 11:34:48
LastEditors: HuSharp
LastEditTime: 2021-02-09 11:42:18
@Email: 8211180515@csu.edu.cn
'''
def count(s, val):
    '''cnt the val 's nums in s
    >>> count([1,2,3,4,1], 1)
    2
    '''
    total = 0
    for element in s:
        if element == val:
            total += 1

    return total


def count_same(s):
    '''
    >>> for x, y in [(1, 1), (2, 4), (3, 9)]:
            print(x, y)
    1 1
    2 4
    3 9
    '''
    same_count = 0
    for x, y in s:
        if x == y:
            same_count += 1
    return same_count