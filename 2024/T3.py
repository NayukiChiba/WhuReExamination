"""
现有一串神秘的密文 ciphertext，经调查，密文的特点和规则如下：

密文由非负整数组成
数字 0-25 分别对应字母 a-z
请根据上述规则将密文 ciphertext 解密为字母，并返回共有多少种解密结果。
"""

string = "216612"


def decodeAll(ciphertext: str):
    s = str(ciphertext)
    n = len(s)

    # 存放所有解密出的字符串集合
    all_results = []

    # path: 到目前为止已经解密出的字符串
    def backtrack(start: int, path: str):
        # 终止条件：当切分到达末尾，说明找到了一条完整的解密字符串
        if start == n:
            all_results.append(path)
            return

        # 选择 1：切分 1 个字符
        # 数字 0-9 直接转字母
        one_digit = s[start : start + 1]
        char1 = chr(int(one_digit) + 97)  # 通过 ASCII 偏移转为对应字母
        backtrack(start + 1, path + char1)

        # 选择 2：切分 2 个字符
        if start + 1 < n:
            two_digit = s[start : start + 2]
            # 过滤掉带前导 "0" 的并且要求在 10~25 之间的
            if 10 <= int(two_digit) <= 25:
                char2 = chr(int(two_digit) + 97)
                backtrack(start + 2, path + char2)

    # 从下标 0 开始找，起初拼出来的字符串是空 ""
    backtrack(0, "")

    return len(all_results), all_results


count, results = decodeAll(string)
print(f"共有 {count} 种解密结果：")
for res in results:
    print(res)
