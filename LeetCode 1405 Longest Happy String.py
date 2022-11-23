class Solution: # 18 90
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        
        def isValidAdd(s, material):
            if material[0] == 0:
                return False
            if len(s) < 2:
                return True
            return material[1] != s[-1] or material[1] != s[-2]
        
        materials = [[a, 'a'], [b, 'b'], [c, 'c']]
        ans = ''
        while a or b or c:
            materials.sort(reverse=True)
            if isValidAdd(ans, materials[0]):
                ans += materials[0][1]
                materials[0][0] -= 1
            elif isValidAdd(ans, materials[1]):
                ans += materials[1][1]
                materials[1][0] -= 1
            elif isValidAdd(ans, materials[2]):
                ans += materials[2][1]
                materials[2][0] -= 1
            else:
                return ans
        return ans
                
            