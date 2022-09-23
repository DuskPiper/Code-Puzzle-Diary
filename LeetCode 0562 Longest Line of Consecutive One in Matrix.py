class Solution: # 32, 79
    def longestLine(self, mat: List[List[int]]) -> int:
        m = len(mat[0])
        n = len(mat)
        ans = 0
        
        for i in range(n):
            for j in range(m):
                if mat[i][j] == 1:
                    mat[i][j] = (                                           # Turn the matrix to DP
                        1 + mat[i][j-1][0] if j > 0 else 1,                 # Horizontal len so far
                        1 + mat[i-1][j][1] if i > 0 else 1,                 # Vertical len so far
                        1 + mat[i-1][j-1][2] if i > 0 and j > 0 else 1,     # Diagnal len so far
                        1 + mat[i-1][j+1][3] if i > 0 and j < m-1 else 1    # A-diagnal len so far
                    )
                    ans = max(ans, max(mat[i][j]))
                else:
                    mat[i][j] = (0, 0, 0, 0)                                # Clear all the "so far"s
        
        return ans