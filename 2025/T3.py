"""
宇宙中有 num 个星球。实际消耗的 Cost 不仅包含过路费，还受引力差影响
从星球 i 移动到星球 j 的实际消耗公式为:
Cost = length+∣g_i−g_j∣
请计算从起点星球 start 到终点星球 end 的最小总消耗
Input:
第一行输入 num
第二行输入 num 个整数，表示每个星球的引力值
第三行输入 ways
接下来 ways 行，每行包含三个整数 start, end, length
最后一行输入两个整数 Start 和 End
"""

num = 3
gravity = [10, 20, 15]
ways = 3
length = {(1, 2): 5, (2, 3): 2, (1, 3): 20}
start = 1
end = 3
all_ways = {}
for key, value in length.items():
    # 开始星球
    start_star = key[0]
    # 终点星球
    end_star = key[1]
    # 把长度加上引力差
    length[key] = value + abs(gravity[start_star - 1] - gravity[end_star - 1])

    # 先获每一个点相连的区域，如果字典里没有这个键，就初始化一个空列表
    if start_star not in all_ways:
        all_ways[start_star] = []
    all_ways[start_star].append(end_star)


# 这里的逻辑只针对简单的两段路径
res = float("inf")
# 如果有直达的路径，先算进去
if (start, end) in length:
    res = min(res, length[(start, end)])

# 如果有通过中转的点
if start in all_ways:
    for mid in all_ways[start]:
        # 需要确保中转点能到终点
        if (mid, end) in length:
            res = min(res, length[(start, mid)] + length[(mid, end)])

print(res)
