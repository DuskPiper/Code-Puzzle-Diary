class Solution: # 48 80
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[str]:

        ans = []
        i = lower
        nums.append(upper+1)
        for n in nums:
            if i < n:
                ans.append(self.format(i, n-1))
            i = n + 1
        return ans

    def format(self, start, end) -> str:
        if start == end:
            return str(start)
        else:
            return f'{start}->{end}'
