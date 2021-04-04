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
    # a = ['A','B','C']#'C','B','D']
    # import sys
    # import copy
    # class solution:
    #     def countOrder(self,n,vichles):
    #         res, path = [], []
    #         vis = [0]*n
    #         # flag = False #whether B is appear
    #         self.dfs(vichles, 0, res, path,vis)
    #         return res
    #
    #     def dfs(self, vichles, index, res, path,vis):
    #         if len(path) == len(vichles):
    #             res.append("".join(copy.deepcopy(path)))
    #             return
    #         if vis[index]: return
    #         vis[index] = 1
    #         for i in range(len(vichles)):
    #             path.append(vichles[i])
    #             self.dfs(vichles, i + 1, res, path,vis)
    #             path.pop()
    #         vis[index] = 0
    # sol = solution()
    # res = sol.countOrder(3,a)
    # print(res)

    from itertools import permutations
    import math
    # res = permutations(a,3)
    # for item in res:
    #     flag = False
    #     for i in item:
    #         if i=='B':
    #             if flag:
    #                 print("-".join(item),end=" ")
    #                 break
    #             else:
    #                 break
    #         elif i=='A':
    #             flag = True
    #     # print(item)
    import sys
    # line = sys.stdin.readline().strip()
    # values = list(map(int, line.split()))
    # N = values[0]
    # COUNT = values[1]
    # loc = []
    # for i in range(1,COUNT+1):
    #     loc.append([values[i*2],values[i*2+1]])
    # load data
    import sys,math

    from itertools import combinations

    a = ['a','d','b','c']
    sum_v = 0
    words = [0]*26
    for item in a:
        idx = ord(item)-ord('a')
        words[idx]+=1
    combine = 1
    comb_l = 0
    for word in words:
        if word!=0:
            combine*=word
            comb_l +=1


    test_l = list(range(comb_l))
    sum_v = 2**len(test_l)-1
    print(sum_v*combine)
    # min_v = math.inf
    # def dfs(table,si,sj,n,now,k,dist):
    #     if now>k:
    #         global min_v
    #         min_v = min(min_v,dist)
    #         print(min_v)
    #     for i in range(n):
    #         for j in range(n):
    #             if table[i][j]==now:
    #                 dist += (abs(i-si)+abs(j-sj))
    #                 dfs(table,i,j,n,now+1,k,dist)
    #     return
    #
    # def findMinCost(table,n,k):
    #     for i in range(n):
    #         for j in range(n):
    #             if table[i][j]==1:
    #                 dfs(table,i,j,n,2,k,0)
    #
    # line = sys.stdin.readline().strip()
    # n,k = list(map(int, line.split()))
    # table = []
    # for i in range(n):
    #     line = sys.stdin.readline().strip()
    #     nums = list(map(int, line.split()))
    #     table.append(nums)
    # findMinCost(table,n,k)
    # if min_v ==math.inf: min_v = -1
    # print(min_v)
