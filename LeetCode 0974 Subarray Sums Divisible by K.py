class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        res = 0
        remainderCounter = [1] + [0] * k # 子表和%k的计数；子表为空则余数为0，故counter[0]=1
        curSumRemainder = 0 # 目前为止的和%k的值
        for n in nums:
            curSumRemainder = (curSumRemainder + n % k + k) % k # 额外%k+k是为避免n是负数
            res += remainderCounter[curSumRemainder]
            remainderCounter[curSumRemainder] += 1
        return res