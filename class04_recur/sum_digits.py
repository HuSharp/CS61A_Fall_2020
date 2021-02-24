'''
Descripttion: 
version: 
Author: HuSharp
Date: 2021-02-08 10:19:53
LastEditors: HuSharp
LastEditTime: 2021-02-08 10:21:12
@Email: 8211180515@csu.edu.cn
'''
def split(x):
    return x // 10, x % 10

def sum_digits(x):
    if x < 10:
        return x
    else:
        all_but_last, last = split(x)
        return sum_digits(all_but_last) + last

        