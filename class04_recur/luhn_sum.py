'''
Descripttion: 
version: 
Author: HuSharp
Date: 2021-02-08 11:25:56
LastEditors: HuSharp
LastEditTime: 2021-02-09 08:57:13
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
    
def luhn_sum(x):
    '''
    >>> luhn_sum(32) # 6 + 2 = 8
    8
    >>> luhn_sum(123456) # 123456->226416(5*2=10->1+0=1)--->2+2+6+4+1+6=21
    21 
    '''
    if x < 10:
        return x
    else:
        all_but_last, last = split(x)
        return luhn_sum_double(all_but_last) + last

def luhn_sum_double(x):
    all_but_last, last = split(x)
    # 对当前 last 进行 2 倍
    # 若大于 9 则取各位数之和，否则变为两倍
    luhn_digit = sum_digits(last * 2)
    if x < 10:
        return luhn_digit
    else:
        return luhn_sum(all_but_last) + luhn_digit
