'''
Descripttion: 
version: 
Author: HuSharp
Date: 2021-02-21 15:33:00
LastEditors: HuSharp
LastEditTime: 2021-02-21 15:34:07
@Email: 8211180515@csu.edu.cn
'''
def next_even(start, end):
    even = start + (start % 2)
    while even < end:
        yield even
        even += 2