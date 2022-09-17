class Solution: # 6, 16
    def canMeasureWater(self, cap1: int, cap2: int, target: int) -> bool:
        if cap1 + cap2 < target:
            return False
        if cap1 < cap2:
            cap1, cap2 = cap2, cap1 # Make sure jug1 is the larger jug
            
        q = [(0, 0)]
        visited = set([])
        while q:
            lv1, lv2 = q.pop(0)
            nextStepLevels = (
                (lv1, 0), # empty jug2
                (0, lv2), # empty jug1
                (cap1, lv2), # fill jug1
                (lv1, cap2), # fill jug2
                (min(cap1, lv1 + lv2), 0 if lv2 + lv1 <= cap1 else lv2 - (cap1 - lv1)), # pour jug2 into jug1 as much as possible
                (0 if lv1 + lv2 <= cap2 else lv1 - (cap2 - lv2), min(cap2, lv1 + lv2)) # pour jug1 into jug2 as much as possible
            )
            
            for (newLv1, newLv2) in nextStepLevels:
                if (newLv1, newLv2) not in visited:
                    if newLv1 + newLv2 == target:
                        return True
                    visited.add((newLv1, newLv2))
                    q.append((newLv1, newLv2))
                    
        return False
