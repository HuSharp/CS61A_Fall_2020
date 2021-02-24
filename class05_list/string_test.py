'''
Descripttion: 
version: 
Author: HuSharp
Date: 2021-02-09 12:09:41
LastEditors: HuSharp
LastEditTime: 2021-02-09 12:32:09
@Email: 8211180515@csu.edu.cn
'''
def reverse(str):
    '''法一：交换前后两个, 递归实现
    >>> reverse('asdf')
    'fdsa'
    '''
    if str == '':
        return ''
    elif len(str) == 1:
        return str
    return str[len(str) - 1] + reverse(str[1 : -1]) + str[0]

print(reverse('qweasdf'))

def reverse_2(str):
    '''法二：将第一个放在后面
    >>> reverse_2('asdf')
    'fdsa'
    '''
    if str == '':
        return ''
    return reverse_2(str[1:]) + str[0]

print(reverse_2('asdf'))