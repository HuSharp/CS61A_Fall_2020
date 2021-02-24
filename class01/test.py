'''
Descripttion: 
version: 
Author: HuSharp
Date: 2021-02-04 09:33:36
LastEditors: HuSharp
LastEditTime: 2021-02-04 09:35:18
@Email: 8211180515@csu.edu.cn
'''
def f():
    return g()

def g():
    return 10 / 0

def main():
    f()

main()