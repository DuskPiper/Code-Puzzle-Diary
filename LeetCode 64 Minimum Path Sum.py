class Solution(object): # 64%
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        #minPathSum @ (m, n) = min(
        #    minPathSum(m - 1, n),
        #    minPathSum(m, n - 1)
        #) + grid[m][n] 动态规划
        if not grid: return 0
        r, c = len(grid), len(grid[0])
        dp = [[0 for _ in range(c)] for _ in range(r)] # dp grid，用来记录到grid相应点的最短路径长度
        dp[0][0] = grid[0][0]
        for i in range(1, c): # 初始化dp的第一行
            dp[0][i] = dp[0][i - 1] + grid[0][i]
        for i in range(1, r): # 初始化dp的第一列
            dp[i][0] = dp[i - 1][0] + grid[i][0]
        for i in range(1, r): # 开始逐行逐列计算dp所有项
            for j in range(1, c):
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + grid[i][j]
        return dp[-1][-1] # dp最末项即为答案