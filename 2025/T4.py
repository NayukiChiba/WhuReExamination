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

# 1. 接收输入（机考的标准数据读取）
num = int(input())
gravity = list(map(int, input().split()))

# 星球编号一般是 1-N，这里在引力数组头部插一个 0 占位，方便使用 gravity[i] 直接取第 i 个星球的引力
gravity.insert(0, 0)

ways = int(input())

# 2. 构建图的邻接表
# graph[u] = [(v, 实际消耗), ...]
graph = {i: [] for i in range(1, num + 1)}

for _ in range(ways):
    u, v, length = map(int, input().split())
    # 核心：题目要求的消耗计算公式
    cost = length + abs(gravity[u] - gravity[v])

    # 通常星球之间的太空通路是双向的，所以我们存两条边；
    # 如果明确给的是有向图（单向通道），请删掉下一行 v 到 u 的追加
    graph[u].append((v, cost))
    graph[v].append((u, cost))

start_node, end_node = map(int, input().split())

# 3. 朴素版本的 Dijkstra 算法（不使用 heapq）
# distances[i] 用来记录从起始终点到达 i 星球的最小已知消耗，最初均为无穷大
distances = {i: float("inf") for i in range(1, num + 1)}
distances[start_node] = 0

# visited 用于记录已经找到最终最短路径的节点
visited = set()

# 外层循环，最多遍历 num 次（每次找出一个离起点最近的节点）
for _ in range(num):
    # 3.1 找当前距离起点最近且没有被访问过的节点
    # 可以直接通过过滤和 min 函数配合 lambda 简化寻找最小节点的过程
    unvisited = [node for node in range(1, num + 1) if node not in visited]

    # 如果没有可达的未访问节点，提前结束 (根据距离找出代价最小的点)
    if not unvisited or min(unvisited, key=lambda x: distances[x]) == float("inf"):
        break

    current_node = min(unvisited, key=lambda x: distances[x])

    # 提前结束：如果距离最近的点就是终点或者根本不可达
    if current_node == end_node or distances[current_node] == float("inf"):
        break

    # 3.2 标记该节点为已访问
    visited.add(current_node)

    # 3.3 通过该节点去更新它能到达的所有邻居的距离（松弛操作）
    for neighbor, weight in graph[current_node]:
        if neighbor not in visited:
            # 直接使用 min 简化状态转移方程
            distances[neighbor] = min(
                distances[neighbor], distances[current_node] + weight
            )


# 4. 输出结果
if distances[end_node] == float("inf"):
    print("-1")  # 说明无法到达终点星球
else:
    print(distances[end_node])
