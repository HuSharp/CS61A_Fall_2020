'''
Descripttion: 
version: 
Author: HuSharp
Date: 2021-02-14 20:28:46
LastEditors: HuSharp
LastEditTime: 2021-02-14 21:42:14
@Email: 8211180515@csu.edu.cn
'''

from tree import *

def print_sums(t, so_far):
    so_far = so_far + label(t)
    if is_leaf(t):
        print(so_far)
    else:
        for b in branches(t):
            print_sums(b, so_far)