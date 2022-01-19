class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int: # 14%, 33%
        m, n = len(grid), len(grid[0])
        visited = set([(0, 0, k)])  # (x, y, remaining-bombs), used to avoid repeats
        q = [(0, 0, 0, 0)]  # (x, y, bomb-used, steps-so-far)
        while q:
            (x, y, bombed, step) = q.pop(0) # BFS pop
            if x == m - 1 and y == n - 1: # Reached end
                return step
            for (i, j) in ((x, y - 1), (x, y + 1), (x - 1, y), (x + 1, y)): # go left/right/up/down
                if i >= 0 and j >=0 and i < m and j < n: # step is in grid
                    if grid[i][j] == 0 and (i, j, bombed) not in visited: # step is not walled
                        visited.add((i, j, bombed))
                        q.append((i, j, bombed, step + 1))
                    if grid[i][j] == 1 and bombed < k and (i, j, bombed - 1) not in visited: # step is walled, use a bomb
                        visited.add((i, j, bombed - 1))
                        q.append((i, j, bombed + 1, step + 1))
        return -1