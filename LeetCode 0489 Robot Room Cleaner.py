# """
# This is the robot's control interface.
# You should not implement it, or speculate about its implementation
# """
#class Robot:
#    def move(self):
#        """
#        Returns true if the cell in front is open and robot moves into the cell.
#        Returns false if the cell in front is blocked and robot stays in the current cell.
#        :rtype bool
#        """
#
#    def turnLeft(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def turnRight(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def clean(self):
#        """
#        Clean the current cell.
#        :rtype void
#        """

class Solution: # 57, 13
    def cleanRoom(self, robot):
        """
        :type robot: Robot
        :rtype: None
        """
        visited = set()
        
        def dfs(x, y, dx, dy): # x, y是相对起点的坐标(因为不知道绝对坐标)；(dx, dy)属于[(0, 1), (0, -1), (1, 0), (-1, 0)]，表示方向
            # 清洁当前
            robot.clean()
            visited.add((x, y))
            
            # 向四个方向DFS尝试，从来的方向开始尝试，逐渐左转四次以尝试所有方向，结束时是原方向
            for direction in range(4):
                if (x + dx, y + dy) not in visited and robot.move():
                    dfs(x + dx, y + dy, dx, dy) # 算得新的相对坐标，并保留原本方向；保留的目的是为了方便返回
                robot.turnLeft() 
                dx, dy = -dy, dx # 方向坐标左转
            
            #结束四个方向后仍然是来的时候的方向，因此掉头、归位、掉头保持方向
            robot.turnLeft()
            robot.turnLeft()
            robot.move()
            robot.turnLeft()
            robot.turnLeft()
            
        dfs(0, 0, 0, 1) # 初始方向是上，因此dx, dy = 0, 1
                
                
            
        