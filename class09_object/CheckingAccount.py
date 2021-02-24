'''
Descripttion: 
version: 
Author: HuSharp
Date: 2021-02-23 12:19:41
LastEditors: HuSharp
LastEditTime: 2021-02-23 12:20:14
@Email: 8211180515@csu.edu.cn
'''
from Account import Account
class CheckingAccount(Account):
    """A bank account that charges for withdrawals.

    >>> ch = CheckingAccount('Jack')
    >>> ch.balance = 20
    >>> ch.withdraw(5)
    14
    >>> ch.interest
    0.01
    """