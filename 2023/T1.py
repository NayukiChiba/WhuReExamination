"""
程序模拟“随机生成一堆整数”的过程，给定一个目标值 x。
请查询在这堆整数中, 是否存在任意两个数 a and b, 使得 a+b=x。
要求：
算法的时间复杂度必须优于 O(n^2)

若存在解, 输出两个整数, 用空格隔开
若不存在解, 输出 error。
"""

import random

random_numbers = [random.randint(0, 100) for _ in range(20)]
target = random.randint(0, 100)

# 排序耗时O(nlogn)
random_numbers.sort()

left = 0
right = len(random_numbers) - 1
while left < right:
    if random_numbers[left] + random_numbers[right] == target:
        print(random_numbers[left], random_numbers[right], target)
        break
    elif random_numbers[left] + random_numbers[right] <= target:
        left += 1
    else:
        right -= 1

if left >= right:
    print("error")
