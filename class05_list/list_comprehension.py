'''
Descripttion: 
version: 
Author: HuSharp
Date: 2021-02-09 12:01:25
LastEditors: HuSharp
LastEditTime: 2021-02-09 12:08:55
@Email: 8211180515@csu.edu.cn
'''
def list_create(n):
    '''
    >>> list_create(3)
    [0, 1]
    >>> list_create(4)
    [0, 1, 2]
    >>> list_create(8)
    [0, 1, 2, 4]
    >>> list_create(12)
    [0, 1, 2, 3, 4, 6]
    '''
    return [0, 1] + [x for x in range(2, n) if n % x == 0] 