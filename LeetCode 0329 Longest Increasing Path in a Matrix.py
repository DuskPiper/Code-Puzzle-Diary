class Solution: # 94, 38
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int: # dp
        history = {} # DP, (i, j) -> best result for this cell
        m, n = len(matrix), len(matrix[0])
        
        def dfs(i, j):
            if (i, j) in history:
                return history[(i, j)]
            curVal = matrix[i][j]
            leftBest = dfs(i - 1, j) if i > 0 and matrix[i - 1][j] > curVal else 0
            rightBest = dfs(i + 1, j) if i < m - 1 and matrix[i + 1][j] > curVal else 0
            upBest = dfs(i, j - 1) if j > 0 and matrix[i][j - 1] > curVal else 0
            downBest = dfs(i, j + 1) if j < n - 1 and matrix[i][j + 1] > curVal else 0
            curBest = 1 + max(leftBest, rightBest, upBest, downBest)
            history[(i, j)] = curBest
            return curBest
        
        if not matrix: return 0
        ans = 0
        for i in range(m):
            for j in range(n):
                ans = max(ans, dfs(i, j))
        return ans