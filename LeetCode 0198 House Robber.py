class Solution(object):
    def rob(self, nums): # 20, 7
        """
        :type nums: List[int]
        :rtype: int
        """
        '''not in-place'''
        if not nums: return 0
        if len(nums) == 1: return nums[0]
        if len(nums) == 2: return max(nums)
        mid = len(nums) // 2;
        return max(
            self.rob(nums[:mid - 1]) + self.rob(nums[mid + 2:]) + nums[mid],
            self.rob(nums[:mid]) + self.rob(nums[mid + 1:])
        )