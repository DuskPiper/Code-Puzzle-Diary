class Solution: # 18, 76
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        while len(nums1) + len(nums2) > 2:
            if nums1 and nums2:
                if nums1[0] < nums2[0]:
                    nums1.pop(0)
                else:
                    nums2.pop(0)  
            elif nums1: 
                nums1.pop(0)
            elif nums2: 
                nums2.pop(0)
                
            if nums1 and nums2:
                if nums1[-1] > nums2[-1]:
                    nums1.pop(-1)
                else:
                    nums2.pop(-1)
            elif nums1:
                nums1.pop(-1)
            elif nums2:
                nums2.pop(-1)
                
        nums = sorted(nums1 + nums2)
        return sum(nums) / float(len(nums))