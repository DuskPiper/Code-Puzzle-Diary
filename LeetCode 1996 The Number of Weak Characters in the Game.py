class Solution: # 82, 72
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        
        properties.sort(key=lambda x: (-x[0], x[1]))
        
        ans = 0
        maxDef = 0
        for a, d in properties:
            if d < maxDef:
                ans += 1
            else:
                maxDef = d
                
        return ans