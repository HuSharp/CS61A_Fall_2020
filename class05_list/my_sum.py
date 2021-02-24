'''
Descripttion: 
version: 
Author: HuSharp
Date: 2021-02-09 11:50:30
LastEditors: HuSharp
LastEditTime: 2021-02-09 11:58:17
@Email: 8211180515@csu.edu.cn
'''
def mySum(L):
    if L == [] :
        return 0
    return L[0] + mySum(L[1:])

def sum_iter(x):
    total = 0
    for i in range(0, x + 1):
        total += i
    return total

def sum_rec(x):
    if x == 0:
        return 0
    return sum_rec(x-1) + x