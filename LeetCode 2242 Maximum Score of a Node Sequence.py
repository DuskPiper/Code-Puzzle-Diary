class Solution: # 26 61
    def maximumScore(self, scores: List[int], edges: List[List[int]]) -> int:

        def updateSmallest3(n, l):
            l.append((scores[n], n))
            l.sort()
            if len(l) > 3:
                l.pop(0)
            
        top3neighbors = defaultdict(list)
        for a, b in edges:
            updateSmallest3(a, top3neighbors[b])
            updateSmallest3(b, top3neighbors[a])
            
        ans = -1
        for a, b in edges:
            sa, sb = scores[a], scores[b]
            for sc, c in top3neighbors[a]:
                if c != b:
                    for sd, d in top3neighbors[b]:
                        if d != c and d != a:
                            ans = max(ans, sa + sb + sc + sd)
                            
        return ans
                
        