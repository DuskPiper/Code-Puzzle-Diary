class Solution(object): # 64%, 1%
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        # 参考LeetCode 62，是动态规划问题，uniquePaths[m, n] = uniquePaths[m - 1, n] + uniquePaths[m, n - 1], 遇到阻挡则阻挡算作0
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        #subUP = [[0] * n] * m #不知道为什么就是蜜汁报错
        subUP = [[0 for _ in range(n)] for _ in range(m)]
        subUP[0][0] = 1 - obstacleGrid[0][0]
        for i in range(1, m):
            subUP[i][0] = subUP[i-1][0] * (1 - obstacleGrid[i][0])
        for i in range(1, n):
            subUP[0][i] = subUP[0][i-1] * (1 - obstacleGrid[0][i])
        for i in range(1, m):
            for j in range(1, n):
                subUP[i][j] = (subUP[i][j - 1] + subUP[i - 1][j]) * (1 - obstacleGrid[i][j])
        #print(subUP)
        return subUP[-1][-1]