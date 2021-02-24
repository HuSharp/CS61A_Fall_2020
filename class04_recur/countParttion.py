'''
Descripttion: 
version: 
Author: HuSharp
Date: 2021-02-08 17:53:24
LastEditors: HuSharp
LastEditTime: 2021-02-09 11:29:34
@Email: 8211180515@csu.edu.cn
'''

'''
The number of partitions of a positive integer n,
using parts up to size m,
is the number of ways in 
which n can be expressed as 
the sum of positive integer parts up to m 
in increasing order
'''

# 函数对象有一个__name__属性，可以拿到函数的名字：
def trace(f):
    def g(n, m):
        print(f.__name__ + '(' + str(n) + ',' + str(m) + ') was called')
        result = f(n, m)
        print(f.__name__ + '(' + str(n) + ',' + str(m) + ')->' + str(result))
        return result
    return g


# n 表示总共多少巧克力， m 表示最多不超过多少
@trace
def count(n, m):
    if n == 0:
        return 1 
    elif n < 0 or m == 0:
        return 0

    # 划分为子问题，子问题分为两类：
    # 一是用最大值为 m 的来划分
    # 二是用最大值非 m 的来划分
    else:
        return count(n - m, m) + count(n, m - 1)
        # return count(n - m, min(m, n-m)) + count(n, m - 1)
count(2, 2) 