class Solution(object): # 99.9%, 1%
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums: return 0
        ''' 简单易懂的思路
        max_sum_ending_at_i = [nums[0]] # 结束在index i的所有subsequence和的最大值
        for i, n in enumerate(nums):
            if i >= 1:
                max_sum_ending_at_i.append(
                    max(n, max_sum_ending_at_i[-1] + n) # DP：max_sum_ending_at_i第i项取决于第i-1项
                    )
        return max(max_sum_ending_at_i)
        '''
        # 此答案中直接用max_sum_ending_at_i覆盖了nums，节约内存
        for i in range(1, len(nums)): nums[i] = nums[i] if nums[i - 1] < 0 else nums[i - 1] + nums[i]
        return max(nums)
            
            
            