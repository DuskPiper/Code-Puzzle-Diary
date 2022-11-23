class Solution: # 42, 75
    def minMoves(self, nums: List[int]) -> int:
        return sum(nums) - (min(nums) * len(nums))