"""
编写程序，显示 2 到 1000 之间（包括 2 和 1000）的所有完数。所谓完数，是指该数的各因子（真约数）之和正好等于该数本身。
例如：6的因子为 1, 2, 3（不包含 6 本身）。因为
1+2+3=6, 所以 6 是一个完数。
"""


def getFactor(num: int) -> list:
    factor = []  # 因子列表
    for i in range(1, num):
        if num % i == 0:
            factor.append(i)

    return factor


def isRes(num: int) -> bool:
    if sum(getFactor(num)) == num:
        return True
    else:
        return False


if __name__ == "__main__":
    for num in range(2, 1001):
        if isRes(num):
            print(num, end=" ")
