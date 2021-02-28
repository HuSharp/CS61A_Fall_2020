'''
Descripttion: 
version: 
Author: HuSharp
Date: 2021-02-28 18:09:31
LastEditors: HuSharp
LastEditTime: 2021-02-28 18:31:50
@Email: 8211180515@csu.edu.cn
'''
class Ratio:
    def __init__(self, n, d):
        self.numer = n
        self.demon = d

    def __repr__(self):
        return 'Ratio({0}, {1})'.format(self.numer, self.demon)

    def __str__(self):
        return 'Ratio({0}/{1})'.format(self.numer, self.demon)

    def __add__(self, other):
        
        # 若为 int :Ratio(1, 3) + 1
        if isinstance(other, int):
            n = self.numer + self.demon * other
            d = self.demon
            
        elif isinstance(other, Ratio):
            n = self.numer * other.demon + self.demon * other.numer
            d = self.demon * other.demon    

        elif isinstance(other, float):
            return float(self) + other
        
        g = gcd(n, d)
        return Ratio(n // g, d // g)

    # 对于 1 + Ratio(1, 3) 
    __radd__ = __add__

    def __float__(self):
        return self.numer / self.demon

def gcd(n, d):
    while n != d:
        n, d = min(n, d), abs(n - d)
    return n


