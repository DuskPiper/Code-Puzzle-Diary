class Solution(object): # 95%, 16%
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid: return 0
        ans = 0
        xlen, ylen = len(grid), len(grid[0])
        
        def mark(x, y): # recursion，记录当前岛块已visited，并记录其上下左右
            if grid[x][y] == "1": # 保证不是“0”非岛屿或者“2”已被visited
                grid[x][y] = "2" # 记录方式为标记为“2”
                if x >= 1: mark(x - 1, y) # 左
                if y >= 1: mark(x, y - 1) # 上
                if x < xlen - 1: mark(x + 1, y) # 右
                if y < ylen - 1: mark(x, y + 1) # 下
        
        for x in range(xlen): # main，逐个排查
            for y in range(ylen):
                if grid[x][y] == "1": # 排查到未visit过的岛屿
                    ans += 1
                    mark(x, y) # 标记，思路类似于union find
        return ans