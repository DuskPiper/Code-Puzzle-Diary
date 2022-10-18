class Solution: # 64, 63
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        
        # Djikstra
        m, n = len(heights[0]), len(heights)
        efforts = [[math.inf] * m for _ in range(n)]
        efforts[0][0] = 0
        minHeap = [(0, 0, 0)]  # (totalEffort, i, j)
        heapq.heapify(minHeap)
        
        while minHeap:
            e, i, j = heapq.heappop(minHeap)
            if e > efforts[i][j]: # Already found a better way to i,j. Skipping this.
                continue
            efforts[i][j] = e # Update to new e, which is better
            
            # Add next steps
            for (ni, nj) in ((i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)):
                if 0 <= ni < n and 0 <= nj < m:
                    newEffort = max(e, abs(heights[i][j] - heights[ni][nj]))  # quote "A route's effort is the maximum absolute difference in heights between two consecutive cells of the route."
                    if newEffort < efforts[ni][nj]:
                        efforts[ni][nj] = newEffort
                        heapq.heappush(minHeap, (newEffort, ni, nj))
            
        return efforts[-1][-1]