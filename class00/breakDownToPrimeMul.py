'''
Descripttion: 
version: 
Author: HuSharp
Date: 2021-02-03 10:44:57
LastEditors: HuSharp
LastEditTime: 2021-02-03 10:51:54
@Email: 8211180515@csu.edu.cn
'''
def prime_factor(n):
    """
    # print the prime factors of n in non_decreasing order
    >>> prime_factor(8)
    2
    2
    2
    >>> prime_factor(9)
    3
    3
    >>> prime_factor(10)
    2
    5
    >>> prime_factor(11)
    11
    >>> prime_factor(12)
    2
    2
    3
    >>> prime_factor(858)
    2
    3
    11
    13
    """
    while n > 1:
        k = smallest_prime_factor(n) # get smallest prime in cur num
        n = n // k # transform n to floorDive k's n
        print(k)
    
# get smallest prime in n
def smallest_prime_factor(n):
    x = 2
    while n % x != 0:
        x = x + 1
    return x

