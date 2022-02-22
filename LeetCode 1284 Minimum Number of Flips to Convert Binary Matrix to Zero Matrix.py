class Solution:
    def minFlips(self, mat: List[List[int]]) -> int: # 48%, 16%
        
        # Check matrix all zero
        def isMatAllZero(mat):
            return sum([sum(row) for row in mat]) == 0
        
        # Flip matrix in place
        def flip(mat, r, c):
            mat[r][c] = 1 - mat[r][c]
            if r > 0: 
                mat[r - 1][c] = 1 - mat[r - 1][c]
            if r < len(mat) - 1: 
                mat[r + 1][c] = 1 - mat[r + 1][c]
            if c > 0:
                mat[r][c - 1] = 1 - mat[r][c - 1]
            if c < len(mat[0]) - 1:
                mat[r][c + 1] = 1 - mat[r][c + 1]
           
        # Recurse solve a given matrix
        def solve(mat, visited, answered):
            matrixFeature = str(mat)
            if matrixFeature in answered: # Same matrix already solved with an answer
                return answered[key]
            elif matrixFeature in visited: # Running into a loop
                return math.inf
            elif isMatAllZero(mat): # Solved just now, returning minStep=0
                return 0
            
            visited.add(matrixFeature)
            minSteps = math.inf # Records min of all BFS trials below
            for i in range(len(mat)):
                for j in range(len(mat[0])):
                    # Try to flip any spot to form a new matrix, and solve it
                    flip(mat, i, j)
                    ans = solve(mat, visited, answered)
                    minSteps = min(minSteps, ans + 1)
                    flip(mat, i, j) # Flip it back for next BFS trial. Bcz we want to make matrix changes in place
            answered[matrixFeature] = minSteps # Register answer
            visited.remove(matrixFeature) # Pop current matrix from visited, for parent to carry out next (unrelated) BFS trial
            return minSteps
            
        # Brute force BFS, recursion
        visited = set()
        answered = {}
        ans = solve(mat, visited, answered)
        return -1 if ans == math.inf else ans
        