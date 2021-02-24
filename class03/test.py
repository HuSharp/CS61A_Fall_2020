'''
Descripttion: 
version: 
Author: HuSharp
Date: 2021-02-07 09:09:55
LastEditors: HuSharp
LastEditTime: 2021-02-08 10:17:11
@Email: 8211180515@csu.edu.cn
'''
def remove(n, digit):
    '''
    >>> remove(231, 3)
    21
    >>> remove(243123, 2)
    4313
    '''
    kept, digits = 0, 0 # digits 记录当前位数
    while n > 0:
        n, last = n // 10, n % 10
        if last != digit:
            kept += last * (10 ** digits)
            digits += 1
    return kept


def cal_sum(*args):
    ax = 0
    for x in args:
        ax += x
    return ax

def lazy_sum(*args):
    def sum():
        ax = 0
        for x in args:
            ax += x
        return ax
    return sum


def count():
    '''
    >>> f1()
    9
    >>> f2()
    9
    >>> f3()
    9
    '''
    fs = []
    for i in range(1, 4):
        def f():
            return i * i
        fs.append(f)

    return fs
# test:    
f1, f2, f3 = count()
# 因此 返回闭包时牢记一点：
# 返回函数不要引用任何循环变量，或者后续会发生变化的变量。

def count_2():
    '''
    >>> f1()
    1
    >>> f2()
    4
    >>> f3()
    9
    '''
    def f(j):
        def g():
            return j * j
        return g

    # 若是这样，那么返回的则不是函数
    # def m(j):
    #     return j * j
    
    fs = []
    for i in range(1, 4):
        fs.append(f(i))  # f(i)立刻被执行，因此i的当前值被传入f()
    return fs


#********************************************
# 利用闭包返回一个计数器函数，每次调用它返回递增整数：
def createCounter():
    lst = []
    def counter():
        lst.append(0)
        return len(lst)
    return counter

# 测试:
counterA = createCounter()
print(counterA(), counterA(), counterA(), counterA(), counterA()) # 1 2 3 4 5
counterB = createCounter()
if [counterB(), counterB(), counterB(), counterB()] == [1, 2, 3, 4]:
    print('测试通过!')
else:
    print('测试失败!')


#********************************
# 装饰器

def trace1(fn):
    def wrapped(x):
        print('->', fn, '(', x, ')')
        return fn(x)
    return wrapped

@trace1
def triple(x):
    return 3 * x
# 等价 triple = trace1(triple)

