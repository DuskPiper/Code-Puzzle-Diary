class Solution: # 35, 99
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        
        def distSq(p1, p2):
            return (p1[0] - p2[0]) * (p1[0] - p2[0]) + (p1[1] - p2[1]) * (p1[1] - p2[1])
        
        dists = [
            distSq(p1, p2),
            distSq(p1, p3),
            distSq(p1, p4),
            distSq(p2, p3),
            distSq(p2, p4),
            distSq(p3, p4)
        ]
        dists.sort()
        
        return dists[0] == dists[1] == dists[2] == dists[3] and dists[3] != dists[4] and dists[4] == dists[5]