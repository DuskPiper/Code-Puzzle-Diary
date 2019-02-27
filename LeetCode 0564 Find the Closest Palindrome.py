class Solution(object): # 96%, 3%
    def nearestPalindromic(self, n):
        """
        :type n: str
        :rtype: str
        """
        if int(n) <= 10: return str(int(n) - 1)
        candidates, distance = [], 999999999 # candidates有两种情况共七个数
        # Case 1: 123 -> 12 -> 111, 121, 131; 1999 -> 19 -> 1881, 1991, 2002
        first_half_varies = map(str, [int(n[:(len(n) + 1) / 2]) + i for i in (-1, 0, 1)]) # 123 -> 11, 12, 13
        for half in first_half_varies: candidates.append(int(half + (half[:-1] if len(n) % 2 else half)[::-1])) # 13 -> 131; 13 -> 1331
        # Case 2: 789 -> 1000 -> 999, 1001, 99, 101 # 其实后面两个是为应对corner case
        candidates += [int("9" * j) + i for i in (0, 2) for j in (len(n), len(n) - 1)]
        # Now pick nearest
        n = int(n)
        for can in candidates:
            if can == n: continue # exclude itsself
            if abs(can - n) < distance: distance, ans = abs(can - n), can
            elif abs(can - n) == distance: ans = min(ans, can)
        return str(ans)