"""
编写程序，生成斐波那契数列的前 30 个数，找出其中所有的质数，输出这些质数，并统计它们的个数。
"""


def Fibonacci(num) -> list:
    """
    args:
        num(int):表示斐波那契数列的个数
    """
    res = [1, 1]
    while len(res) < 30:
        res.append(res[-1] + res[-2])
    return res


def isPrime(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


res1 = Fibonacci(30)
res2 = []
for num in res1:
    if isPrime(num):
        res2.append(num)
print(res1)
print(res2)
print(len(res2))
