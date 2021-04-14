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
    # import sys
    # for line in sys.stdin:
    #     a = line.split()
    #     print(int(a[0]) + int(a[1]))
    #
    #
    # import sys
    # if __name__ == "__main__":
    #     # 读取第一行的n
    #     n = int(sys.stdin.readline().strip())
    #     ans = 0
    #     for i in range(n):
    #         # 读取每一行
    #         line = sys.stdin.readline().strip()
    #         # 把每一行的数字分隔后转化成int列表
    #         values = list(map(int, line.split()))
    #         for v in values:
    #             ans += v
    #     print(ans)
    from itertools import combinations

    import sys
    from collections import defaultdict
    def findMagic(s,k):
        n = len(s)
        if n%k!=0: return -1
        has = [0]*26
        for c in s:
            has[ord(c)-ord('a')] += 1
        flag = True
        for i in has:
            if not i or i%k==0: continue
            else:
                flag = False
                break
        if flag: return s
        for c in s:
            i = ord(c)-ord('a')
            if has[i]%k==0:
                continue
        return -1

    # import math
    # for num in range(2,51):
    #     a = str(oct(math.factorial(num)))
    #     cnt = 0
    #     for c in a[::-1]:
    #         if c=="0":
    #             cnt +=1
    #         else:
    #             break
    #     print(num,"--",cnt,"---",a)  # 8, per 4 and
    #         #5-1 10-2 15-4 20-7 25-9