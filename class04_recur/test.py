'''
Descripttion: 
version: 
Author: HuSharp
Date: 2021-02-08 10:17:30
LastEditors: HuSharp
LastEditTime: 2021-02-08 16:40:22
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