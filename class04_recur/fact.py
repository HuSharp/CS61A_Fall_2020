'''
Descripttion: 
version: 
Author: HuSharp
Date: 2021-02-08 10:24:46
LastEditors: HuSharp
LastEditTime: 2021-02-08 10:25:11
@Email: 8211180515@csu.edu.cn
'''
def fact(n):
    if n == 0:
        return 1
    else:
        return n * fact(n-1)