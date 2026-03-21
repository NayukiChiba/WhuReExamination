"""
N 阶魔方阵 是一个 N×N的方阵，由自然数 1,2,…,N^2 组成。
其特点是：每个元素值均不相等，且每行、每列以及主、副对角线上的 N 个元素之和都相等。
请根据以下罗伯法的算法规则，编写程序生成并输出一个 N 阶魔方阵。
构造规则:
1. 构造规则起始位置：数字 1 放置在第一行的正中间。

2. 移动方向：下一个数字的位置总是位于当前数字的右上方（即：行号减 1，列号加 1）。

3. 越界处理：上边界越界：如果行号超出上方边界（行号 < 0），则将其放入该列的最后一行。

4. 右边界越界：如果列号超出右方边界（列号 > N-1），则将其放入该行的最左一列。

5. 特殊情况（已被占位或 N 的倍数）：若当前数字是 N 的整数倍，则下一个数字的位置直接选在当前位置的下方（行号加 1，列号不变）。
"""

# width = input("输入方阵的阶数(只能是奇数): ")
width = 3
row = 0
col = width // 2
matrix = [[0 for _ in range(width)] for _ in range(width)]
matrix[row][col] = 1

matrix[row][col]

for num in range(2, width**2 + 1):
    if (num - 1) % width == 0:
        row = (row + 1) % width
    else:
        row = (row - 1) % width
        col = (col + 1) % width
    matrix[row][col] = num

for i in range(width):
    for j in range(width):
        print(matrix[i][j], end=" ")
    print()
