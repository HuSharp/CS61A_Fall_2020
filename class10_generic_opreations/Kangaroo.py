'''
Descripttion: 
version: 
Author: HuSharp
Date: 2021-02-28 18:39:14
LastEditors: HuSharp
LastEditTime: 2021-03-06 12:03:57
@Email: 8211180515@csu.edu.cn
'''
class Kangaroo:
    def __init__(self):
        self.bags = []

    def put_in_pouch(self, x):
        for i in range(len(self.bags)):
            if self.bags[i] == x:
                print("already in pouch!")
                return
        self.bags.append(x)

    def __str__(self):
        if (len(self.bags) == 0):
            return "The Kangaroo's bag is empty!"
        else:
            return "The Kangaroo's bag include:" + str(self.bags)