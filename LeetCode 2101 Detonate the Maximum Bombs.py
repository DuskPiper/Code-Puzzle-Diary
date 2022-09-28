class Solution: # 50, 42
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        
        self.impactTree = defaultdict(list)
        
        for i, (x, y, r) in enumerate(bombs):
            for j, (bx, by, br) in enumerate(bombs):
                if i != j and (x - bx) * (x - bx) + (y - by) * (y - by) <= r * r:
                    self.impactTree[i].append(j)
            
        def getImpact(i, visited):
            visited.add(i)
            for child in self.impactTree[i]:
                if child not in visited:
                    visited.add(child)
                    getImpact(child, visited)
        
        ans = 0
        for i in range(len(bombs)):
            impact = set()
            getImpact(i, impact)
            ans = max(ans, len(impact))
            
        return ans
                    
                    
                