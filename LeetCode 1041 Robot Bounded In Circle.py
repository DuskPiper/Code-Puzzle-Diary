class Solution: # 95 73
    def isRobotBounded(self, instructions: str) -> bool:
        x, y, dx, dy = 0, 0, 0, 1
        for i in instructions:
            if i == 'G':
                x += dx
                y += dy
            elif i == 'L':
                dx, dy = -dy, dx
            elif i == 'R':
                dx, dy = dy, -dx
        if x == 0 and y == 0: return True # Corner case, 只要单轮运动后回0，那一定可循环
        if dy != 1: return True # 只要单轮运动后，方向不保持起始方向，则一定循环(如朝左右则4轮为循环，如超下则2轮)
        