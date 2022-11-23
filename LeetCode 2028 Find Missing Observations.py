class Solution: # 37 11
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        s = mean * (n + len(rolls)) - sum(rolls)
        if s > n * 6 or s < n:
            return []
        ceil = math.ceil(s / float(n))
        diff = ceil * n - s
        return [ceil - 1] * diff + [ceil] * (n - diff)