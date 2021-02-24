'''
Descripttion: 
version: 
Author: HuSharp
Date: 2021-02-04 10:54:53
LastEditors: HuSharp
LastEditTime: 2021-02-06 21:08:10
@Email: 8211180515@csu.edu.cn
'''

def cube(k):
    return pow(k, 3)

def summation(n, term):
    ''' sum the first n terms of a sequence
    >>> summation(5, cube)
    225
    '''
    total, k = 0, 1
    while k <= n:
        total, k = total + term(k), k + 1
    return total


# def compose(f, g):
#     return lambda x: f(g(x))

# h = compose(lambda x: x * x, lambda y: y + 1)
# result = h(12)
# print(result)


#*********************************
# 两个对比
# def f(y):
#     return y + 1

# g = lambda x: f
# eight = g(2)(7)
# print(eight)
# two = g(7)(1)
# print(two)

def f(y):
    return y + 1

g = lambda x: f(x)
eight = g(7)
print(eight)
two = g(1)
print(two)


def apply_twice(f, x):
    return f(f(x))

def squre(x):
    return x * x

p = apply_twice(squre, 2)


def make_adder(n):
    def adder(k):
        return k + n
    return adder

add_three = make_adder(3)
result = add_three(4)


def printAll(x):
    print(x)
    return printAll
printAll(1)(2)(3)

print('打印到当前为止的和：')
# 打印 x ，返回 下一个数的和的函数
def printSum(x):
    print(x)
    def nextSum(y):
        return printSum(x + y)
    return nextSum

printSum(1)(2)(3)
