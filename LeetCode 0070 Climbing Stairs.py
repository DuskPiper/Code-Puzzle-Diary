class Solution(object): # 97%, 100%
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        # climbStairs(n) = climbStairs(n - 1) + climbStairs(n - 2)
        # climbStairs(1) = 1
        # climbStairs(2) = 2
        ''' Recursion which exceeds time
        def climb(n):
            if n <= 1: return 1
            elif n == 2: return 2
            else: return climb(n - 1) + climb(n - 2)
        return climb(n)
        '''
        if n <= 1: return 1
        climbn = [1, 2]
        for i in range(2, n): climbn.append(climbn[i - 1] + climbn[i - 2])
        return climbn[n - 1]