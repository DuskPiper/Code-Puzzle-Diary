class Solution(object): # 100%, 0%
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        zero_boarder = 0 # 此下标之前的部分已经全是0
        two_boarder = len(nums) - 1 # 此下标之后的部分已经全是2
        i = 0 # iterator
        while i <= two_boarder:
            while i < two_boarder and nums[i] == 2: # 一定要先操作2，先操作0的话，下标zero_boarder跟着移动会漏掉后面的2需要swap的
                # swap(i, two_boarder)
                nums[i] = nums[two_boarder] #这两行是swap
                nums[two_boarder] = 2 #这两行是swap，2是写死的，等同nums[i]
                two_boarder -= 1
            while i > zero_boarder and nums[i] == 0:
                # swap(i, zero_boarder)
                nums[i] = nums[zero_boarder]
                nums[zero_boarder] = 0
                zero_boarder += 1
            i += 1