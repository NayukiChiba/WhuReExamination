"""
给定 n 组测试案例。对于每个案例，包含 k 条关于节点间连通性的描述信息
描述信息的格式为 x y op:
op 为 1: 表示x 和 y 是连通的
op 为 0: 表示x 和 y 是不连通的
请判断每个案例中的所有信息是否存在逻辑矛盾
args:
    n: 测试案例有多少组
    k: 有多少个点
    x, y, op
"""

n = int(input("一共有测试组的组数为: "))
res = []
for i in range(n):
    link: list[list[tuple[int, int]]] = [[], []]
    k = int(input("一共有多少条信息? :"))
    for j in range(k):
        x, y, op = map(int, input("输出x, y, op: ").split())
        # 把op==1和op==0分开放
        link[op].append((x, y))
    # 开始找父亲
    parent = {}

    def find(x):
        """
        x: 找到x的根节点
        """
        if x not in parent:
            # 如果x不在这个并查集中, 那么自己就是自己的父亲, 就是根节点
            parent[x] = x
        if parent[x] != x:
            # 如果自己不是自己的父亲, 说明父亲不是根节点
            parent[x] = find(parent[x])
        return parent[x]

    # 开始合并
    def union(x, y):
        """
        如果把x和y合并成一个集合, 公用一个父亲
        """
        root_x = find(x)
        root_y = find(y)
        if root_x != root_y:
            parent[root_x] = root_y

    # 1. 开始处理连通的部分
    for way in link[1]:
        # way: ltuple(int, int)
        x, y = way
        union(x, y)

    # 2. 开始处理不连通的部分
    has_conflict = False
    for no_way in link[0]:
        x, y = no_way
        if find(x) == find(y):
            has_conflict = True
            break

    if has_conflict:
        res.append("NO")
    else:
        res.append("YES")

for i in range(len(res)):
    print(res[i])
