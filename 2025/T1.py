"""
给定一个长度为 N 的整数数组 A。你需要完成 M 次操作，操作分为两种类型：
修改操作：格式为 1 x y，将数组中第 x 个位置的元素值修改为 y。
查询操作：格式为 2 x y，输出数组中从第 x 个位置到第 y 个位置（包含 x 和 y）之间的最大值。

第一行输入两个整数 N 和 M。
第二行输入 N 个整数，表示数组的初始状态。
接下来 M 行，每行包含三个整数 op x y。

"""


def update(position: int, y: int, arr: list[int]):
    """
    如果是字符2
    把第x个位置的元素值修改为y
    args:
        position: 位置
        y: 修改值
        arr: 原数组
    """

    arr[position] = y


def query(position1: int, position2: int, arr: list[int]):
    return max(arr[position1:position2])


N, M = map(int, input("输入两个整数: ").split())
arr = list(map(int, input("输入数组: ").split()))
for i in range(M):
    op, x, y = map(int, input("输入op, x, y: ").split())
    if op == 1:
        update(x, y, arr)
    if op == 2:
        print(query(x, y, arr))
