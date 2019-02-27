class Solution(object): # 99%, 77%
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        i = m + n # i是iterator，从nums1末尾开始向前
        m -= 1 # m作为nums1的游标，从有效尾部开始
        n -= 1 # n作为nums2的游标，从尾部开始
        while m >= 0 and n >= 0: # 当两个游标都有余量时
            i -= 1
            if nums1[m] > nums2[n]:
                nums1[i] = nums1[m]
                m -= 1
            else:
                nums1[i] = nums2[n]
                n -= 1
        while n >= 0: # 如果m用完了，n还没有用完，则直接复制过去
            nums1[n] = nums2[n]
            n -= 1