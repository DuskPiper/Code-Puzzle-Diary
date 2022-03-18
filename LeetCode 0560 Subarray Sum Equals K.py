class Solution: # 64, 98
    def subarraySum(self, nums: List[int], k: int) -> int:
        ans = 0
        curSum = 0
        sumCount = {0 : 1}
        for num in nums:
            curSum += num
            delta = curSum - k
            if delta in sumCount:
                ans += sumCount[delta]
            sumCount[curSum] = sumCount.get(curSum, 0) + 1
        return ans