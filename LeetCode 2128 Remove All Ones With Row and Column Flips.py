class Solution(object):
    def removeOnes(self, grid): # 6%, 63%
        """
        :type grid: List[List[int]]
        :rtype: bool
        """
        # Important method: each row or column shall only be flipped 0 or 1 time, extra flip is useless
        rows = len(grid)
        cols = len(grid[0])
        for r in range(rows): # Flip any row if row[0] == 1
            if grid[r][0] == 1: # Flip this row
                for c in range(cols):
                    grid[r][c] = 1 - grid[r][c]
        for c in range(cols): # Check if any col has same val each (either 0 or 1)
            if sum([grid[r][c] for r in range(rows)]) not in (0, rows):
                return False
        return True