"""
输入一个正整数 n，将其分解为若干个正整数之和。请编程输出所有可能的分解方案。
规则要求:
分解出的数字之和必须等于n
分解出的数字顺序应当从大到小排列（例如 4+2 是合法的，而 2+4 被视为与 4+2 重复，不予输出）。
输出所有方案时，请按照字典序（第一位数字大的排前面）输出。
例如数字 6 的分解包括：6 5+1 4+2 4+1+1...以此类推。
"""


def dfs(remain: int, maxPart: int, path: list[int]):
    """
    args:
        remain(int): 表示还有多少没有被分解
        maxPart(int): 表示你最大可以表示多少
        path(list): 分解序列
    """

    if remain == 0:
        # 如果剩余0, 那就是分解完成了
        print("+".join(map(str, path)))
        return

    # 如果没有分解完, 那就接着分解
    upper = min(remain, maxPart)
    # 限制你的上界, 不能超过当前的剩余和最大限度
    for part in range(upper, 0, -1):
        path.append(part)
        dfs(remain - part, part, path)
        # dfs结束之后，path再取出当前栈顶元素，进入下一个分支
        path.pop()


num = 6
dfs(num, num, [])
