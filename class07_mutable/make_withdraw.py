'''
Descripttion: 
version: 
Author: HuSharp
Date: 2021-02-19 13:29:18
LastEditors: HuSharp
LastEditTime: 2021-02-20 11:54:18
@Email: 8211180515@csu.edu.cn
'''
def make_withdraw(balance):
    def withdraw(amount):
        nonlocal balance
        if amount > balance:
            return 'Insufficient funds'
        balance -= amount
        return balance
    return withdraw


def make_withdraw_list(balance):
    b = [balance]
    def withdraw(amount):
        nonlocal balance
        if amount > b[0]:
            return 'Insufficient funds'
        b[0] -= amount
        return b[0]
    return withdraw

def pra(x):
    def p(y):
        x = x + 1
    return p


withdraw = make_withdraw(100)
withdraw(25)
withdraw(25)
withdraw(60)
withdraw(15)
