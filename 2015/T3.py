"""
有一个袋子，里面装有2个红球，3个绿球，5个黄球。现在从袋子中随机摸出 8 个球。
请编写程序，计算并打印出所有可能的颜色组合。
"""

for RED in range(3):
    for GREEN in range(4):
        for YELLOW in range(6):
            if RED + GREEN + YELLOW == 8:
                print(f"Red: {RED}, Green: {GREEN}, Yellow: {YELLOW}")
