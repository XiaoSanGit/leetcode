


visited = [False]
# Template
def dfs(depth):
    if depth==None or visited[depth]:
        return  # if satisfy some situation, back.
    visited[depth] = True
    for i in range(10): # space that next step can reach
        if not visited[i]:
            dfs(i)
    return

# Template
def bfs():
    q = set()
    init = 0
    q.add(init) # q is queue
    while(len(q)):
        i = q.pop()
        if (visited[i]): continue
        for j in range(10): # stauts can reach
            if j:
                q.add(j)
# 找到所有合法解

def trackback(depth):
    if depth==None or visited[depth]:# if satisfy some situation, back.
        return
    visited[depth] = True
    dosomething(depth)

    for i in range(10): # space that next step can reach
        if not visited[i]:
            dfs(i)
        # dosomething(depth) 或者在这do
    undosomething(depth)
    return

#01背包
W = whole_weight()
n = num_items() # V[i] is weight of i
f = [0]*len(W+1)
for i in range(n):
    for j in range(W,V[i]-1,-1):
        f[j] = max(f[j], f[j-V[i]] + W[i])

# N, M, W, V
# dp[0..M] = 0
#
# for i in 1...N:
#     for j in W[i]...M: # 这里必须正向枚举，因为当前计算需要dp[i]对应的其他状态来计算
#         dp[j] = max(dp[j], dp[j - W[i]] + V[i]
#
# return dp[M]

#完全背包
# N, M, W, V, H
# dp[0..M] = 0
#
# for i in 1...N:
#     for j in M...W[i]: # 这里必须逆向枚举，因为当前计算需要dp[i - 1]对应的其他状态来计算
#         for h in 0...min(H[i], j / W[i]):
#             dp[j] = max(dp[j], dp[j - h * W[i]] + h * V[i])
#
# return dp[M]
#如果求组合数就是外层for循环遍历物品，内层for遍历背包。
#如果求排列数就是外层for遍历背包，内层for循环遍历物品。

res = []
path = []

# def backtrack(未探索区域, res, path):
#     if path 满足条件:
#         res.add(path) # 深度拷贝
#         # return  # 如果不用继续搜索需要 return
#     for 选择 in 未探索区域当前可能的选择:
#         if 当前选择符合要求:
#             path.add(当前选择)
#             backtrack(新的未探索区域, res, path)
#             path.pop()
#
class Solution(object):
    def subsets(self, nums):
        res, path = [], []
        self.dfs(nums, 0, res, path)
        return res

    def dfs(self, nums, index, res, path):
        res.append(copy.deepcopy(path))
        for i in range(index, len(nums)):
            path.append(nums[i])
            self.dfs(nums, i + 1, res, path)
            path.pop()

        a = ['A','C','C','B']
        a.sort()