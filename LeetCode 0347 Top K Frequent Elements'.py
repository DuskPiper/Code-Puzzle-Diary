class Solution: # 84 45
    def topKFrequent(self, nums: List[int], K: int) -> List[int]:
        count = {}
        for n in nums:
            count[n] = count.get(n, 0) + 1

        pq = []
        for k, v in count.items():
            if len(pq) < K:
                heapq.heappush(pq, (v, k))
            else:
                heapq.heappushpop(pq, (v, k))
        return [x[1] for x in pq]
