"""
Input
输入包含一行，为一个字符串。
字符串长度不超过 255。
字符串中不包含空格、制表符等空白字符。

Output
输出一行，表示按 ASCII 码从小到大排序后的字符串。
"""

str = input("输入一行字符串:")
str = sorted(str)
res = ""
for ch in str:
    res += ch
print(res)
