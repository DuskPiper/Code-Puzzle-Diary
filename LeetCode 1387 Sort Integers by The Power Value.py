class Solution: # 57, 27
    def getKth(self, lo: int, hi: int, k: int) -> int:
        self.powers = {1:0}
        
        def getPower(n):
            if n in self.powers:
                return self.powers[n]
            elif n % 2:
                self.powers[n] = getPower(3 * n + 1) + 1
            else:
                self.powers[n] = getPower(n // 2) + 1
            return self.powers[n]
        
        ps = [(getPower(i), i) for i in range(lo, hi + 1)]
        
        return heapq.nsmallest(k, ps)[-1][1]
                