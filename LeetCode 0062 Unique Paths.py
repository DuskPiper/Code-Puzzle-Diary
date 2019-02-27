class Solution(object): # 99%, 1%
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        # KEY: uniquePaths(m, n) = uniquePaths(m - 1, n) + uniquePaths(m, n - 1)
        '''
        # recursion solution
        subUP = {}
        def uniquePathsHelper(m, n):
            if m == 1 or n == 1: return 1
            mUP = subUP.get((m - 1, n), None)
            nUP = subUP.get((m, n - 1), None)
            if mUP and nUP: ans = mUP + nUP
            elif mUP: ans = mUP + uniquePathsHelper(m, n - 1)
            elif nUP: ans = nUP + uniquePathsHelper(m - 1, n)
            else: ans = uniquePathsHelper(m, n - 1) + uniquePathsHelper(m - 1, n)
            subUP[(m, n)] = ans
            return ans 
        return uniquePathsHelper(m, n)
        '''
        # iteration solution
        subUP = [[1] * n] * m
        for i in range(1, m):
            for j in range(1, n):
                subUP[i][j] = subUP[i - 1][j] + subUP[i][j - 1]
        return subUP[m - 1][n - 1]