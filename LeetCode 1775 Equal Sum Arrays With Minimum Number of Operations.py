class Solution: # 6 9
    def minOperations(self, nums1: List[int], nums2: List[int]) -> int:
        diff = sum(nums1) - sum(nums2)
        if diff > 0:
            larger, smaller = nums1, nums2
        else:
            larger, smaller = nums2, nums1

        for i in range(len(larger)):
            larger[i] = larger[i] - 1
        for i in range(len(smaller)):
            smaller[i] = 6 - smaller[i]

        steps = sorted(larger + smaller)
        diff = abs(diff)
    
        ans = 0
        while steps and diff > 0:
            diff -= steps.pop()
            ans += 1

        if diff > 0:
            return -1
        else:
            return ans
