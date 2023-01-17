class Solution: # 83 80
    def canJump(self, nums: List[int]) -> bool:
        if nums[0] >= len(nums) - 1:
            return True
        frontier = nums[0]
        end = len(nums) - 1
        i = 0
        while i < frontier:
            i += 1
            if nums[i] + i > frontier:
                frontier = nums[i] + i
                if frontier >= end:
                    return True
            
        return False