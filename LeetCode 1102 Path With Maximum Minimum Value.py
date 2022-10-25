class Solution: # 34 16
    def maximumMinimumPath(self, grid: List[List[int]]) -> int:
        
        m = len(grid)
        n = len(grid[0])
        
        visited = set([(0, 0)])
        neighbors = []  # max heap
        if m > 1: neighbors.append((-grid[1][0], 1, 0))
        if n > 1: neighbors.append((-grid[0][1], 0, 1))
        heapq.heapify(neighbors)
        
        ans = grid[0][0]
        while neighbors:
            nextExpansion, i, j = heapq.heappop(neighbors)
            nextExpansion = -nextExpansion
            ans = min(ans, nextExpansion)
            visited.add((i, j))
            
            if i == m - 1 and j == n - 1:
                return ans
            
            visited.add((i, j))
            for di, dj in ((0, 1), (0, -1), (1, 0), (-1, 0)):
                if 0 <= i + di < m and 0 <= j + dj < n and (i + di, j + dj) not in visited:
                    heapq.heappush(neighbors, (-grid[i+di][j+dj], i+di, j+dj))
                