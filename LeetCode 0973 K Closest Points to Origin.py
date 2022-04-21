class Solution: # 94, 60
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        ans = []
        for i, (x, y) in enumerate(points):
            points[i] = (- x * x - y * y, x, y)
        for p in points:
            heapq.heappush(ans, p)
            if len(ans) > K:
                heapq.heappop(ans)
        return [(x, y) for _, x, y in ans]