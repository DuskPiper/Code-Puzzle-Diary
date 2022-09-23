class Solution: # 17, 12
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        pq = [(grid[0][0], 0, 0)]
        visited = set()
        t = max(grid[0][0], grid[n-1][n-1])
        
        while True:
            curT, i, j = heapq.heappop(pq) # BFS, always take the lowest possible next-tile
            visited.add((i, j))
            t = max(t, curT) # Record highest point ever been to 
            if i == n - 1 and j == n - 1:
                return t
            for x, y in ((i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)):
                if 0 <= x < n and 0 <= y < n and (x, y) not in visited:
                    heapq.heappush(pq, (grid[x][y], x, y))
        
        
# Brute Force        
#         self.n = len(grid)
#         self.t = max(grid[0][0], grid[self.n-1][self.n-1])
#         self.visited = set()
        
#         def search(i, j):
#             if (i, j) in self.visited or i < 0 or i >= self.n or j < 0 or j >= self.n or grid[i][j] > self.t:
#                 return False
#             if i == self.n - 1 and j == self.n - 1:
#                 return True
#             self.visited.add((i, j))
#             return any([search(i-1, j), search(i+1, j), search(i, j-1), search(i, j+1)])
        
#         while not search(0, 0):
#             self.t += 1
#             self.visited = set()
            
#         return self.t
        