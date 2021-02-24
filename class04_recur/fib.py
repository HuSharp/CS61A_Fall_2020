'''
Descripttion: 
version: 
Author: HuSharp
Date: 2021-02-08 17:04:38
LastEditors: HuSharp
LastEditTime: 2021-02-08 17:16:59
@Email: 8211180515@csu.edu.cn
'''



def fib(x):
    if x == 0:
        return 0
    elif x == 1:
        return 1
    else:
        return fib(x-1) + fib(x-2)

print(fib(6))