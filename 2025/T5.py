"""
你有 n 项工作可以选择去做。对于每一项工作，给出了开始时间 x、结束时间 y 和报酬 z。
同一时间只能做一项工作。
可以在一项工作结束的时刻立即开始另一项工作。
你需要从这 n 项工作中选择若干项，使得在不时间冲突的前提下，获得的总报酬最大。
"""

# dp[i]表示"前i个"工作最大获得的报酬, 1 <= i <= n
# 当我们碰到第i个工作是否要选择的时候, 有两个选择
# 1. 不选工作i, 这样的话, dp[i] = dp[i-1], 因为第i个工作没选没报酬
# 2. 选择工作i, 为了时间不冲突, 所以我们要找到开始时间之前那个结束时间
# - 比如我们5点开始的任务i, 但是任务(i-1)要6点结束, 那么我们上一个任务就不能是i-1
# - 我们记上一个任务是p[i], 任务p[i]在4点结束, 是离任务i开始时间最近的结束任务
# 综上, dp[i] = max(dp[i-1], price[i] + dp[p[i]])
n = int(input("获取n个任务: "))
missions: list[list[int]] = [[] for _ in range(n)]
for i in range(n):
    missions[i] = list(map(int, input("输入三个整数: ").split()))
# 按照结束时间sort一下mission
missions.sort(key=lambda x: x[1])
# 获取mission之后, 规定一下
dp = [0 for _ in range(n + 1)]
p = [0 for _ in range(n + 1)]
for i in range(1, n + 1):
    start_time = missions[i - 1][0]
    price = missions[i - 1][2]
    # 开始获取p[i]
    for j in range(i - 1, 0, -1):
        if missions[j - 1][1] <= start_time:
            p[i] = j
            break
    dp[i] = max(dp[i - 1], price + dp[p[i]])

print(dp[n])
