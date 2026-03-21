"""
在一个 N×M 的网格矩阵中，包含两种字符：
. 表示空格（需要被保护，且可以放置棋子）。
# 表示障碍物（不需要被保护，且不可放置棋子）。

现定义一种棋子，当它被放置在某个空格 (x,y) 上时，可以保护该位置本身以及其上下左右相邻的 4 个格子（共 5 个）。
请计算：最少需要放置多少个棋子，才能使矩阵中所有的空格 . 都处于被保护状态？
"""

N = 4
M = 4
matrix = [
    ["#", ".", ".", "."],
    [
        ".",
        ".",
        ".",
        ".",
    ],
    [
        ".",
        ".",
        ".",
        ".",
    ],
    [".", ".", ".", "#"],
]

# 定义棋子是否被保护
protected = [[0 for _ in range(M)] for _ in range(N)]

ans = float("inf")


def update_protection(row, col, delta):
    """
    用于更新protected列表, 当(x, y)被放下棋子的时候, 更新protected
    """
    # 保护自己
    protected[row][col] += delta
    # 保护上方
    if row > 0:
        protected[row - 1][col] += delta
    # 保护下方
    if row < N - 1:
        protected[row + 1][col] += delta
    # 保护左边
    if col > 0:
        protected[row][col - 1] += delta
    # 保护右边
    if col < M - 1:
        protected[row][col + 1] += delta


def dfs(row, col, used_pieces):
    """
    args:
        row: 当前准备放置棋子的行
        col: 当前准备放置棋子的列
        used_pieces: 已经使用的棋子个数
    """
    global ans
    if used_pieces > ans:
        return

    # 开始换行
    if col == M:
        # 列走到底了
        row += 1
        col = 0

    # 结束条件: 走完所有的格子
    if row == N:
        # 检查所有的棋盘是不是都已经被保护了
        all_safe = True
        for i in range(N):
            for j in range(M):
                if matrix[i][j] == "." and protected[i][j] <= 0:
                    # 如果矩阵中有'.', 但是没有被保护
                    all_safe = False
                    break  # 跳出循环
            if not all_safe:
                break  # 直接跳出

        if all_safe:
            ans = min(ans, used_pieces)
        return

    # 开始剪枝: 看上方的格子
    need_save_up = False
    if row > 0:
        if matrix[row - 1][col] == "." and protected[row - 1][col] <= 0:
            # 如果有的地方没有被保护, 那就是要必须要放棋子了
            need_save_up = True

    # 如果上方没有被保护, 那么这个地方就必须要放棋子
    if need_save_up:
        if matrix[row][col] == "#":
            # 如果是障碍物, 就放不了, 直接回退
            return
        else:
            # 如果不是障碍物, 就要更新所有的节点了, 每个被保护的都加1
            update_protection(row, col, 1)
            # 多加了1个棋子
            dfs(row, col + 1, used_pieces + 1)
            # 回溯, 不保护
            update_protection(row, col, -1)

    else:
        # 如果不需要保护, 上方是安全的, 那就可以选择放或者不放
        # 选择1: 我不放棋子, 直接走下一步
        dfs(row, col + 1, used_pieces)

        if matrix[row][col] == ".":
            # 如果不是障碍物, 那我就放一个看看
            update_protection(row, col, 1)
            # 多加了1个棋子
            dfs(row, col + 1, used_pieces + 1)
            # 回溯, 不保护
            update_protection(row, col, -1)


dfs(0, 0, 0)
if ans == float("inf"):
    print(-1)
else:
    print(ans)
