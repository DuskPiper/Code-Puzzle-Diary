class Solution: # 98, 11
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        nei = defaultdict(set)
        for c1, c2 in roads:
            nei[c1].add(c2)
            nei[c2].add(c1)
            
        top1, top2 = 0, 0
        for k, v in nei.items():
            l = len(v)
            if l > top1:
                top1, top2 = l, top1
            elif top1 > l > top2:
                top2 = l
            
        top2cities = [c for c in range(n) if len(nei[c]) in (top1, top2)]
        
        ans = 0
        for i, j in combinations(top2cities, 2):
            ans = max(ans, len(nei[i]) + len(nei[j]) - int(i in nei[j]))
            
        return ans
        
        