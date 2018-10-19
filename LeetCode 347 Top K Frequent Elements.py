class Solution:
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        ct, ans = collections.Counter(nums), []
        k_count = sorted(ct.values(), reverse = True)[k-1] // 找到第k多的元素的数量
        for k,v in ct.items():
            if v >= k_count:ans.append(k)
        return ans
        
        