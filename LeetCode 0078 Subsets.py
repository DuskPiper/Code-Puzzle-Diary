class Solution(object):
    def subsets(self, nums): # 100, 90
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # DP
        if not nums: return [[]]
        decreaseAns = self.subsets(nums[:-1])
        last = nums[-1]
        ans = [d + [nums[-1]] for d in decreaseAns]
        return decreaseAns + ans
            
        