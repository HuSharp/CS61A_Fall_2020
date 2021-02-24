'''
Descripttion: 
version: 
Author: HuSharp
Date: 2021-02-23 09:45:23
LastEditors: HuSharp
LastEditTime: 2021-02-23 11:14:19
@Email: 8211180515@csu.edu.cn
'''
from math import gcd

class Rational:
    test_num = 0.1
    def __init__(self, numerator, denominator):
        gcd_num = gcd(numerator, denominator)
        self.numerator = numerator // gcd_num
        self.denominator = denominator // gcd_num

    def print(self):
        if self.denominator == 0:
            print('denominator is zero!')
        elif self.denominator == 1:
            print(self.denominator)
        else:
            print(self.numerator, ' / ', self.denominator)

