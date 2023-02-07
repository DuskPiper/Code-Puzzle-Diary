class Solution: # 93 6
    def rob(self, nums: List[int]) -> int:
        
        cache = {}

        # DP with recursion
        def getBest(start, end):
            if start == end: return nums[start]
            if start > end: return 0
            if (start, end) in cache: return cache[(start, end)]

            best = max(
                nums[start] + getBest(start + 2, end),
                getBest(start + 1, end)
            )
            cache[(start, end)] = best
            return best

        return max(
            nums[0] + getBest(2, len(nums) - 2),
            getBest(1, len(nums) - 1)
        )
            