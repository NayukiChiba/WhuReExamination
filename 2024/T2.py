"""
给你一个整数数组 nums ，判断是否存在三元组 [nums[i], nums[j], nums[k]]
满足 i != j、i != k 且 j != k ，同时还满足 nums[i] + nums[j] + nums[k] == 0 。
请你返回所有和为 0 且不重复的三元组。
要求：
写出o(n^3)与o(n^2)对应两个程序，共40分
答案中不可以包含重复的三元组。
"""

nums = [-1, 0, 1, 2, -1, -4]
nums.sort()


def N3Time():
    global nums

    n = len(nums)
    res = []

    for i in range(n):
        # 如果第一个数大于0, 那可以不用玩了
        if nums[i] > 0:
            break

        # i去重, 跳过前一个数字相同的元素
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        for j in range(i + 1, n):
            # 从i+1开始搜索
            if j > i + 1 and nums[j] == nums[j - 1]:
                continue

            for k in range(j + 1, n):
                # k去重
                if k > j + 1 and nums[k] == nums[k - 1]:
                    continue

                if nums[i] + nums[j] + nums[k] == 0:
                    res.append([nums[i], nums[j], nums[k]])
    print(res)


def N2Time():
    global nums

    n = len(nums)
    res = []
    for i in range(n):
        if nums[i] > 0:
            break

        if i > 0 and nums[i] == nums[i - 1]:
            continue

        # 设置双指针
        left = i + 1
        right = n - 1

        while left < right:
            total = nums[i] + nums[left] + nums[right]

            if total == 0:
                res.append([nums[i], nums[left], nums[right]])

                while left < right and nums[left] == nums[left + 1]:
                    left += 1

                while left < right and nums[right] == nums[right - 1]:
                    right -= 1

                left += 1
                right -= 1

            elif total < 0:
                left += 1

            else:
                right -= 1
    print(res)


N3Time()
print("-" * 50)
N2Time()
