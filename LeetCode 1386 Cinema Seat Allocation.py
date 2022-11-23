class Solution:  # 96, 44
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        occuppied = defaultdict(set)
        for r, c in reservedSeats:
                
            if c in (2,3,4,5):
                occuppied[r].add('L')
            elif c in (6,7,8,9):
                occuppied[r].add('R')
            if c in (4,5,6,7):
                occuppied[r].add('M')
        
        ans = n * 2
        for o in occuppied.values():
            if len(o) == 3:
                ans -= 2
            else:
                ans -= 1
                
        return ans
        