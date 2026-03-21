"""
编写程序，将输入的十进制点分形式的 IP 地址（IPv4）转换为二进制形式显示。
转换规则:
输入格式为A.B.C.D，其中 A、B、C、D 均为 0 到 255 之间的整数。

将每个十进制数转换为对应的 8 位二进制数。

如果转换后的二进制数不足 8 位，需要在高位（左侧）补零。

各段二进制数之间依然用小数点 . 连接。
"""

ip = "128.1.2.128"
ip_split = list(map(int, ip.split(".")))
bin_parts = [f"{num:08b}" for num in ip_split]

result = ".".join(bin_parts)
print(result)
