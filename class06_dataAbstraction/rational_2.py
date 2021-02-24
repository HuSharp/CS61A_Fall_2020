'''
Descripttion: 
version: 
Author: HuSharp
Date: 2021-02-12 21:31:33
LastEditors: HuSharp
LastEditTime: 2021-02-12 21:33:03
@Email: 8211180515@csu.edu.cn
'''

def add_rational(x, y):
    """The sum of rational numbers X and Y."""
    nx, dx = numer(x), denom(x)
    ny, dy = numer(y), denom(y)
    return rational(nx * dy + ny * dx, dx * dy)

def mul_rational(x, y):
    """The product of rational numbers X and Y."""
    return rational(numer(x) * numer(y), denom(x) * denom(y))

def rationals_are_equal(x, y):
    """True iff rational numbers X and Y are equal."""
    return numer(x) * denom(y) == numer(y) * denom(x)

def print_rational(x):
    """Print rational X."""
    print(numer(x), "/", denom(x))

    
# Constructor and selectors 版本二
def rational(n, d):
    """A representation of the rational number N/D.
        and implement of lists
    """
    def select(name):
        if name == 'n':
            return n
        elif name == 'd':
            return d
    return select

def numer(x):
    return x('n')

def denom(x):
    return x('d')
