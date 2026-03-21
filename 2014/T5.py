"""
编写程序，使用递归方法计算：用 1 分、2 分和 5 分的硬币凑成 1 元（100 分），一共有多少种不同的凑法？

规则说明:
1. 目标金额为 1 元，即 100 分。

2. 可用的硬币面额为：1 分、2 分、5 分。

3. 每种硬币的数量不限。

4. 请尝试设计一个递归函数来完成计数逻辑（虽然循环也可以解决，但本题考察递归思维）。

输出一个整数，表示共有多少种凑法。

"""

"""
思路: 
可以把100元分成1+99， 2+98 ...， 50+50

"""


def getWay(price, maxCoin=5) -> int:
    # 恰好凑满
    if price == 0:
        return 1
    # 超出金额
    if price < 0:
        return 0

    ways = 0

    # 最接近你原来的“拆分”写法：每次拆一个硬币出来
    # 用 maxCoin 限制后续只能用不大于当前的硬币，避免重复计数
    if maxCoin >= 1:
        ways += getWay(price - 1, 1)
    if maxCoin >= 2:
        ways += getWay(price - 2, 2)
    if maxCoin >= 5:
        ways += getWay(price - 5, 5)

    return ways
