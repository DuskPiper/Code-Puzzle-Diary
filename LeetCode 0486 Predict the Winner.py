class Solution: # 82, 58
    def PredictTheWinner(self, nums: List[int]) -> bool:
        
        cache = {}
        
        def getBestScore(i, j):
            if i > j: return 0
            if i == j: return nums[i]
            if (i, j) in cache: return cache[(i, j)]
            ans = max( # 当前玩家有以下2个选择
                nums[i] + min(getBestScore(i+1, j-1), getBestScore(i+2, j)), # min()是因为下一步玩家会选对自己有利的一步(更大的分)，所以当前玩家只能得更小的分
                nums[j] + min(getBestScore(i+1, j-1), getBestScore(i, j-2))
            )
            cache[(i, j)] = ans
            return ans

        bestScoreA = getBestScore(0, len(nums)-1)
        scoreB = sum(nums) - bestScoreA
        return bestScoreA >= scoreB