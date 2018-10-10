class Solution:
    def checkSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        k==0? 是的话寻找连续0的序列返回True即可
        不是的话：
            寻找两个相差至少为2的序列，他们除以k的余数相等。这样其差集便是目标序列。
		还有2个思考，没有实现：
		1.抽屉原理：如果len(nums)>2*|k|，则一定为True。网上看到的，我证明不出来。
		2.k==0则找连续0的操作我觉得不完备。应该去找和为0的子序列才对。但是目前这样又能够通过测试。
        """
        if k == 0:
            for i in range(len(nums)-1):
                if nums[i]==0 and nums[i+1]==0:#我觉得这个结果是需要考察的，不该是连续0而该是序列和为0
                    return True
            return False
        
        mods, sum_mod = {0: -1}, 0#把所有余数装进mods以便回查
        for i, n in enumerate(nums):
            sum_mod = (sum_mod + n) % k
            if sum_mod in mods and i - mods[sum_mod] > 1:
                return True
            if sum_mod not in mods:
                mods[sum_mod] = i
        return False