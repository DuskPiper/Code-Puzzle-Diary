class Solution: # 17 25
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        vacant = list(range(n))  # roomIndex
        occupied = []  # (availableTime, roomIndex)
        heapq.heapify(vacant)
        usage = [0] * n
        
        meetings.sort()
        for start, end in meetings:
            
            while occupied and occupied[0][0] <= start: # Clear backlog
                t, room = heapq.heappop(occupied)
                heapq.heappush(vacant, room)
                    
            if vacant:  # Immediately start meeting
                room = heapq.heappop(vacant)
                heapq.heappush(occupied, (end, room))
                usage[room] += 1
            else:  # Wait for next available room
                t, room = heapq.heappop(occupied)
                heapq.heappush(occupied, (t + end - start, room))
                usage[room] += 1
                
        maxUsage = max(usage)
        return usage.index(maxUsage)
                
                
                    
                