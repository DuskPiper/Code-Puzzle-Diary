class Solution: # 38, 82
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # find pivot of change
        i = len(nums) - 1
        while i > 0 and nums[i - 1] >= nums[i]: 
            i -= 1
        if i == 0: # no lexicographical larger rearrangement
            nums.reverse()
        else:
            # Find smallest in nums[i:] that's > nums[i - 1]
            pivotVal = nums[i - 1]
            j = len(nums) - 1
            while nums[j] <= pivotVal:
                j -= 1
            # Swap pivot and j
            nums[i - 1], nums[j] = nums[j], nums[i - 1]
            
            # revserse nums[i:-1]
            l, r = i, len(nums) - 1
            while l < r: 
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1
            
                
            