class Solution: # 59 78
    def arraySign(self, nums: List[int]) -> int:
        negCount = 0
        for n in nums:
            if n == 0:
                return 0
            negCount += n < 0
        return -1 if negCount % 2 else 1