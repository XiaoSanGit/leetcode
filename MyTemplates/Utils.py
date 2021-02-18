import time
import os
import numpy as np

def calculate_time(func,*input):
    eplipse = []
    for i in range(10):
        s_t = time.time()
        func(*input)
        f_t = time.time()

        eplipse.append(s_t-f_t)
    avgtime = np.average(eplipse)
    print(avgtime)
    return avgtime


# def multi(*p):
#     sum = 1
#     for arrs in p:
#         for arr in arrs:
#             sum *= int(arr)
#     print("乘积结果为:{}".format(sum))
# nums = input("请输入参数乘积的数值，用空格隔开：")
# multi(nums.split())

if __name__ == '__main__':
    def foo(x,y,z):
        print(x+y+z)
        return
    calculate_time(foo,1,2,3)