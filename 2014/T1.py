"""
编写程序，计算下列分段函数 y = f(x)的值
根据输入的一个实数x, 按照下面的公式计算y
if x > 0:
    y = \frac{\sqrt{x} + e^x}{5x+5}

if x <= 0:
    y = [\frac{2}{3} + sin(60度)] * |x|

Input
输入包含一个实数 x
Output
输出一个实数y, 表示计算结果。结果保留小数点后4位 (四舍五入)。
"""

import math

x = int(input("输入一个实数: "))
if x > 0:
    y = ((x**0.5) + math.exp(x)) / (5 * x + 5)
    print(f"{y:.4f}")
else:
    y = (2 / 3 + math.sin(math.radians(60))) * abs(x)
    print(f"{y:.4f}")
