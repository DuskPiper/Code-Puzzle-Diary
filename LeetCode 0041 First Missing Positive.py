class Solution: # 40, 41
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums.append(0)
        length = len(nums)
        for i, n in enumerate(nums):
            if n >= length or n < 0:
                nums[i] = 0
        for n in nums:
            nums[n % length] += length 
            # 从此，nums[i]的值含义变成“原值 + (所有值=i出现次数*length)”；
            # 我们已确保“原值”<length，所以相当于把[i]作2个用处，一是记录原值，而是做i值的counter
            # 因此 n%length 的含义是得到nums[i]的原值，而 n//length 的含义是得到counter值
        for i, n in enumerate(nums):
            if n // length == 0: # decode nums[i]，这样地板除结果就是counter数，而余数是nums[i]原值
                return i
        return length