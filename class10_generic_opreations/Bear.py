'''
Descripttion: 
version: 
Author: HuSharp
Date: 2021-02-28 17:21:37
LastEditors: HuSharp
LastEditTime: 2021-02-28 17:59:51
@Email: 8211180515@csu.edu.cn
'''
class Bear:
    '''A Bear'''
    def __init__(self):
        self.__repr__ = lambda:'Bear_attr: repr'
        self.__str__ = lambda:'Bear_attr: str'  

    def __repr__(self):
        return 'Bear()'

    def __str__(self):
        return 'a bear!'


b = Bear()
print(b)
print(str(b))
print(repr(b))
print(b.__str__())
print(b.__repr__())


