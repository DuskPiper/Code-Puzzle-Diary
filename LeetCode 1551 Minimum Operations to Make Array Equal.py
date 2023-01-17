class Solution: # 39 60
    def minOperations(self, n: int) -> int:
        num = 1
        s = 0
        while num < n:
            s += n - num
            num += 2
        return s