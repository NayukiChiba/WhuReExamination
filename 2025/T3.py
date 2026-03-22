"""
共有 n 个地点（编号 1 到 n），现有 m 条单向通路。
对于每一条通路，输入 u,v,w,x，表示从 u 到 v 耗时 w，且仅在时刻 x 开启。
假设你从地点 1 在时刻 0 出发，问到达地点 n 最短需要多少时间？
"""

n, m = map(int, input("一共有n个地点, m条单向通路: ").split())
graph: dict[int, list[int]] = {i: [] for i in range(1, n + 1)}
for i in range(m):
    start, end, cost, start_time = map(int, input("请输入u, v, w, x: ").split())
    # 构建有向图
    graph[start].append([end, cost, start_time])


# 标记已经被访问的点
visited = set()
# 先设定1到所有的点的距离是inf
distances = {i: float("inf") for i in range(1, n + 1)}
# 设定1到1的距离是0
distances[1] = 0
# 开始Dijkstra算法
for _ in range(n):
    # 先从没有访问的地方开始写起
    unvisited = [node for node in range(1, n + 1) if node not in visited]

    # 如果没有可以访问到的节点, 直接break
    if not unvisited:
        break

    # 每一个都访问一下, 找到距离最短的那一个作为current_node
    current_node = min(unvisited, key=lambda x: distances[x])

    if distances[current_node] == float("inf"):
        break

    # 加入访问节点
    visited.add(current_node)

    # 找到了现存的node, 开始遍历它的neighbor
    for neighbor, cost, start_time in graph[current_node]:
        # 如果neighbor不在已经确定的最短距离中的话, 就更新它的距离
        if neighbor not in visited:
            # 如果 到当前节点的距离 > 结束点的start_time, 那也是不可达
            if distances[current_node] <= start_time:
                # 无论多早到达, 都只能从start_time出发
                distances[neighbor] = min(distances[neighbor], start_time + cost)

# 输出结果
if distances[n] == float("inf"):
    print(-1)
else:
    print(distances[n])
