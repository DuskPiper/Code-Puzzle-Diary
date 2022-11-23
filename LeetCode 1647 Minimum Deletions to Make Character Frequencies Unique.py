class Solution: # 83 55
    def minDeletions(self, s: str) -> int:
        counter = {}
        for c in s:
            if c not in counter:
                counter[c] = 1
            else:
                counter[c] += 1
        rCounter = {}
        for k, v in counter.items():
            if v not in rCounter:
                rCounter[v] = [k]
            else:
                rCounter[v].append(k)

        ans = 0
        for count in sorted(rCounter.keys()):
            while len(rCounter[count]) > 1:
                c = rCounter[count].pop()
                cCount = count
                while cCount in rCounter and cCount > 0:
                    cCount -= 1
                if cCount:
                    rCounter[cCount] = [c]
                ans += count - cCount

        return ans