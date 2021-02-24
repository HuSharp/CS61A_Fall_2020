'''
Descripttion: 
version: 
Author: HuSharp
Date: 2021-02-21 23:12:44
LastEditors: HuSharp
LastEditTime: 2021-02-21 23:14:47
@Email: 8211180515@csu.edu.cn
'''


def prefixes(s):
    '''
    >>> list(prefixes('asdf'))
    ['a', 'as', 'asd', 'asdf']
    '''
    if s:
        yield from prefixes(s[:-1])
        yield s

def substring(s):
    '''
    >>> list(substring('asdf'))
    ['a', 'as', 'asd', 'asdf', 's', 'sd', 'sdf', 'd', 'df', 'f']
    '''
    if s:
        yield from prefixes(s)
        yield from substring(s[1:])