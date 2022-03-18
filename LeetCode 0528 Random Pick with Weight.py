class Solution: # 96%, 53%

    def __init__(self, w: List[int]):
        for i in range(1, len(w)):
            w[i] += w[i - 1]
        self.w = w
        self.maxVal = w[-1]

    def pickIndex(self) -> int:
        tarVal = random.randint(1, self.maxVal)
        # Binary Search
        #return bisect.bisect_left(self.w, tarVal)
        l, h = 0, len(self.w) - 1
        while l < h:
            mid = (l + h) // 2
            if self.w[mid] >= tarVal:
                h = mid
            else:
                l = mid + 1
        return l
        
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()