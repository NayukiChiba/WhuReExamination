"""
机器人初始位于坐标原点 (0,0)，且面朝 东方 (East)。
程序接收一串指令字符串，根据指令控制机器人移动。
指令字符含义如下：
.：向当前朝向前进一步。

<：原地逆时针旋转 90°（左转）。

>：原地顺时针旋转 90°（右转）。

请输出执行完所有指令后机器人的最终坐标(x,y)。
"""

operations = [".", "<", ".", "<", "."]


class Robot:
    def __init__(self):
        # 设置东: 0, 南: 1, 西: 2, 北: 3
        self.face = 0  # 面朝的方向
        self.pos = [0, 0]

    def update(self, op):
        """
        切换方向
        """
        if op == "<":
            self.face = (self.face - 1) % 4
        if op == ">":
            self.face = (self.face + 1) % 4

    def move(self, op):
        if op == ".":
            if self.face == 0:
                self.pos[0] += 1
            elif self.face == 1:
                self.pos[1] -= 1
            elif self.face == 2:
                self.pos[0] -= 1
            else:
                self.pos[1] += 1

    def run(self, op):
        if op == "<":
            self.update(op)
        elif op == ">":
            self.update(op)
        elif op == ".":
            self.move(op)
        else:
            print("error")


robot = Robot()
for op in operations:
    robot.run(op)

print(robot.pos)
