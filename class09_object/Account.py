'''
Descripttion: 
version: 
Author: HuSharp
Date: 2021-02-23 12:16:32
LastEditors: HuSharp
LastEditTime: 2021-02-23 23:24:31
@Email: 8211180515@csu.edu.cn
'''
class Account:
    """An account has a balance and a holder.

    >>> a = Account('John')
    >>> a.holder
    'John'
    >>> a.deposit(100)
    100
    >>> a.withdraw(90)
    10
    >>> a.withdraw(90)
    'Insufficient funds'
    >>> a.balance
    10
    >>> a.interest
    0.02
    """
    interest = 0.02 # A class Attribute
    def __init__(self, account_holder):
        self.holder = account_holder
        self.balance = 0
    
    def deposit(self, amount):
        self.balance = self.balance + amount
        return self.balance

    def withdraw(self, amount):
        """Subtract amount from balance if funds are available."""
        if amount > self.balance:
            return 'Insufficient funds'
        self.balance = self.balance - amount
        return self.balance



class CheckingAccount(Account):
    """A bank account that charges for withdrawals.
    活期账户 需要收取相关手续费
    >>> ch = CheckingAccount('Jack')
    >>> ch.balance = 20
    >>> ch.withdraw(5)
    14
    >>> ch.interest
    0.01
    """

    withdraw_fee = 1
    interest = 0.02

    def withdraw(self, amount):
        # 需要扣除 withdraw_fee 手续费
        return Account.withdraw(self, amount + self.withdraw_fee)


class Bank:
    """A bank has accounts and pays interest.

    >>> bank = Bank()
    >>> john = bank.open_account('John', 10)
    >>> jack = bank.open_account('Jack', 5, CheckingAccount)
    >>> john.interest
    0.02
    >>> jack.interest
    0.01
    >>> john.interest = 0.06
    >>> bank.pay_interest()
    >>> john.balance
    10.2
    >>> jack.balance
    5.05
    """
    def __init__(self):
        self.accounts = [] # 账户列表

    def open_account(self, holder, amount, kind=Account):
        account = kind(holder)
        account.deposit(amount)
        self.accounts.append(account)

        return account

    def pay_interest(self):
        ''' 支付利息 '''
        for a in self.accounts:
            a.deposit(a.interest * a.balance)

class SavingAccount(Account):
    """A bank account that charges for deposits."""
    deposit_fee = 2 # 每次存钱时收取的手续费

    def deposit(self, amount):
        return Account.deposit(self, amount - self.deposit_fee)

# 多重继承
class AsSeenOnTVAccount(CheckingAccount, SavingAccount):
    """A bank account that charges for everything."""
    def __init__(self, account_holder):
        self.holder = account_holder
        self.balance = 1 # 免费给的钱数
        
