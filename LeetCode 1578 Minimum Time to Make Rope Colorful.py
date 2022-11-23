class Solution: # 9 26
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        ans = 0
        i = 0
        while i < len(colors):
            start = i
            while i < len(colors) - 1 and colors[i] == colors[i+1]:
                i += 1
            if start != i:
                ans += sum(neededTime[start : i+1]) - max(neededTime[start : i+1])
            i += 1
        return ans