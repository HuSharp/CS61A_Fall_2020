'''
Descripttion: 
version: 
Author: HuSharp
Date: 2021-02-12 21:21:45
LastEditors: HuSharp
LastEditTime: 2021-02-12 21:31:16
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


# Constructor and selectors 版本一
def rational(n, d):
    """A representation of the rational number N/D.
        and implement of lists
    """
    return [n, d]

def numer(x):
    return x[0]

def denom(x):
    return x[1]


