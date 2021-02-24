'''
Descripttion: 
version: 
Author: HuSharp
Date: 2021-02-08 16:46:29
LastEditors: HuSharp
LastEditTime: 2021-02-08 16:47:45
@Email: 8211180515@csu.edu.cn
'''
def cascade(x):
    if x < 10:
        print(x)
    else:
        print(x)
        cascade(x // 10)
        print(x)

cascade(486)


def cascade_2(x):
    print(x)
    if x >= 10:
        cascade_2(x // 10)
        print(x)

