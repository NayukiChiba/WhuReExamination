"""
给定一个包含 n 个整数的数组，请在其中找出一个连续的子序列，使得该子序列中所有元素的和最大。
你需要输出该子序列的起始位置（从 1 开始计数）、结束位置（从 1 开始计数）以及最大的和。
要求：
算法的时间复杂度应控制在 O(n) 级别。

"""

import random

n = int(input("输入整数: "))
nums = [random.randint(-5, 5) for _ in range(n)]

max_sum = float("-inf")
current_sum = 0

# 记录下标的变量
start = 0
end = 0
temp_start = 0


for i in range(len(nums)):
    # 贪心, 过去的累加和是不是负担?
    if current_sum <= 0:
        current_sum = nums[i]  # 我直接开始单干, 反正都是负数了
        temp_start = i
    else:
        current_sum += nums[i]  # 收益是正数我就一直干

    # 看看当前的成绩有没有被打破
    if current_sum > max_sum:
        max_sum = current_sum  # 记录
        # 打破记录就可以记录index了
        start = temp_start
        end = i

print(f"起始位置: {start + 1}")
print(f"结束位置: {end + 1}")
print(f"最大和: {max_sum}")
