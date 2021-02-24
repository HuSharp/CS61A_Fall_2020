'''
Descripttion: 
version: 
Author: HuSharp
Date: 2021-02-21 22:59:41
LastEditors: HuSharp
LastEditTime: 2021-02-21 23:12:36
@Email: 8211180515@csu.edu.cn
'''

def countdown_1(k):
    if k > 0:
        yield k
        for i in countdown_1(k-1):
            yield i

def countdown(k):
    if k > 0:
        yield k
        yield from countdown(k-1)
    else:
        yield 'Blast off'

