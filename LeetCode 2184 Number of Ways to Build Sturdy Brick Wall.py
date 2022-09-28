class Solution: # 18 20
    def buildWall(self, height: int, width: int, bricks: List[int]) -> int:
        
        # Get all possible brick combinations for each row
        def getRowCombinations(width, bricks):
            ans = []
            for b in bricks:
                if b == width:
                    ans.append([b])
                elif b < width:
                    for comb in getRowCombinations(width - b, bricks):
                        ans.append([b] + comb)
            return ans
            
        # Convert combinations for better calculating "are 2 rows fit"
        combs = getRowCombinations(width, bricks)
        for i in range(len(combs)):
            for j in range(1, len(combs[i]), 1):
                combs[i][j] += combs[i][j-1]
                
        def areCombsFit(c1, c2):
            s1 = set(c1[:-1])
            s2 = set(c2[:-1])
            return s1.isdisjoint(s2)
        
        # Generate a dict to list all fit row-combinations for any given row
        nextPossibleCombs = {(width,): [tuple(c) for c in combs]}
        for c in combs:
            possibleCombs = []
            for nextRow in combs:
                if areCombsFit(c, nextRow):
                    possibleCombs.append(tuple(nextRow))
            nextPossibleCombs[tuple(c)] = possibleCombs
        
        ans = 0
        
        # DFS
        @cache # This is essential
        def buildRow(height, belowRowComb):
            nonlocal nextPossibleCombs
            if height == 0:
                return 1
            ans = 0
            for comb in nextPossibleCombs[belowRowComb]:
                ans += buildRow(height - 1, comb)
            return ans
        
        return buildRow(height, (width,)) % (10**9+7)
            
            