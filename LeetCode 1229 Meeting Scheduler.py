class Solution: # 92 33
    def minAvailableDuration(self, slots1: List[List[int]], slots2: List[List[int]], duration: int) -> List[int]:

        # Each person won't have intersection w/ themselves, so safe to concat 2 lists
        slots = [s for s in slots1 if s[1] - s[0] >= duration] + [s for s in slots2 if s[1] - s[0] >= duration]
        heapq.heapify(slots)

        while len(slots) >= 2:
            s = heapq.heappop(slots)
            if s[-1] >= slots[0][0] + duration:
                return [slots[0][0], slots[0][0] + duration]
        return []
