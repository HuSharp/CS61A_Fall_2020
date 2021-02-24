'''
Descripttion: 
version: 
Author: HuSharp
Date: 2021-02-04 09:07:00
LastEditors: HuSharp
LastEditTime: 2021-02-04 09:09:08
@Email: 8211180515@csu.edu.cn
'''
try:
    print('try...')
    r = 10 / 0
    print('result is:', r)
except ZeroDivisionError as e:
    print('except:', e)
finally:
    print('finally...')
print("END")