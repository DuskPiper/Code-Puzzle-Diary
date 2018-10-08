class Solution:
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        O(n^2)复杂度
        用一个ll的等长于nums的list来记录nums每一项截止处的片段对应的最长值
        每次外循环就往前推进一项，此项的结果取决于内循环
        内循环查找之前每一项对本项的关系，一旦有前项 < 本项，则说明本项可以增补到前项递增数列中：
            则此时ll[i]就可以update成增补项对应的ll值ll[j]+1了
            此处利用了max_so_far避免了单次大循环多次update，只需要循环末update一个最大值即可
        """
        if not nums:return 0
        ll=[1]*len(nums)#ll[i]最终会是nums[i]的最长子序列长度
        for i,n in enumerate(nums):
            max_so_far=0
            for j in range(i):
                if nums[j]<n:
                    if max_so_far<ll[j]:
                        max_so_far=ll[j]
            ll[i]=max_so_far+1
        return max(ll)