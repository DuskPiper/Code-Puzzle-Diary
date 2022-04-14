class Solution(object): # 88 60
    def countSubIslands(self, grid1, grid2):
        """
        :type grid1: List[List[int]]
        :type grid2: List[List[int]]
        :rtype: int
        """
        def dfs(i, j):
            if i < 0 or i >= len(grid2) or j < 0 or j >= len(grid2[0]) or grid2[i][j] != 1:
                return True
            grid2[i][j] = 0
            isCurValid = grid1[i][j] == 1
            isSurroundingValid = all([dfs(i + 1, j), dfs(i - 1, j), dfs(i, j + 1), dfs(i, j - 1)])
            return isCurValid and isSurroundingValid
        
        ans = 0
        for i in range(len(grid2)):
            for j in range(len(grid2[0])):
                if grid2[i][j] == 1:
                    ans += int(dfs(i, j))
        return ans
            
            
            
        