'''
Descripttion: 
version: 
Author: HuSharp
Date: 2021-02-08 17:24:19
LastEditors: HuSharp
LastEditTime: 2021-02-08 17:33:25
@Email: 8211180515@csu.edu.cn
'''

def mov(cur_disk, start_peg, end_peg):
    print('Mov disk '+str(cur_disk) + ' from peg '\
        + str(start_peg) +' to peg ' + str(end_peg) + '.')

def hanoi(n, start_peg, end_peg):
    if n == 1:
        mov(n, start_peg, end_peg)
    else:
        # 备用钉子
        spare_peg = 6 - start_peg - end_peg
        hanoi(n - 1, start_peg, spare_peg)
        mov(n, start_peg, end_peg)
        hanoi(n - 1, spare_peg, end_peg)

hanoi(3, 1, 3)