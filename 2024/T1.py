"""
给定一个数组 prices ，它的第 i 个元素 prices[i] 表示一支给定股票第 i 天的价格。
你只能选择 某一天 买入这只股票，并选择在 未来的某一个不同的日子 卖出该股票。设计一个算法来计算你所能获取的最大利润。
要求：
写出o(n)与o(n^2)复杂度对应两个程序，共30分

Input:
第一行: 输入N，代表数组长度
第二行: 输入N个数，对应prices的具体值

Output:
输出最大利润
"""

N = 6
prices = [2, 6, 1, 4]


def longTime():
    global prices
    profit = -float("inf")
    for i in range(len(prices)):
        for j in range(i, len(prices)):
            profit = max(profit, prices[j] - prices[i])

    print(profit)


def shortTime():
    global prices
    profit = 0
    min_prices = float("inf")

    for price in prices:
        # 如果当前价格比之前最低价格还要低, 说明今天适合买入
        if price < min_prices:
            min_prices = price
        # 否则, 尝试今天卖出, 计算利润并且更新最大利润
        elif price - min_prices > profit:
            profit = price - min_prices
    print(profit)


if __name__ == "__main__":
    longTime()
    shortTime()
