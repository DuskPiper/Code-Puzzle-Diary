class Solution: # 84 30
    def removeDuplicates(self, nums: List[int]) -> int: 
        placeholder = 10001
        leng = len(nums)
        i, j = 0, 0
        while i < leng:
            while j < leng and nums[j] == nums[i]:
                j += 1
            if j - i > 2:
                for k in range(i+2, j):
                    nums[k] = placeholder
            i = j
        nums.sort()
        k = nums.index(placeholder) if placeholder in nums else len(nums)
        return k
