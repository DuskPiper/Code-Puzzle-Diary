class Solution: # 60 90
    def busiestServers(self, k: int, arrival: List[int], load: List[int]) -> List[int]:
        busy = [] # heap, (nextIdleTime, serverId)
        freeAfter = []  # heap, free servers after cur server
        freeBefore = list(range(k))  # heap, free servers before cur server
        heapq.heapify(freeBefore)
        counter = [0] * k
        
        for i in range(len(arrival)): # For each task
            t, l = arrival[i], load[i]
            idealServer = i % k
            
            # If just finished one loop, reset minHeaps
            if idealServer == 0: 
                freeAfter = freeBefore
                freeBefore = []
            
            # Free all free-able servers
            while busy and busy[0][0] <= t:
                freedT, freedServer = heapq.heappop(busy)
                if freedServer >= idealServer:
                    heapq.heappush(freeAfter, freedServer)
                else:
                    heapq.heappush(freeBefore, freedServer)
                    
            # Decide which server to pick up this task
            if not freeAfter and not freeBefore:
                continue # No free server, drop task
            serverQ = freeAfter if freeAfter else freeBefore
            server = heapq.heappop(serverQ)
            heapq.heappush(busy, (t+l, server))
            counter[server] += 1
             
        busiest = max(counter)
        ans = [i for i,c in enumerate(counter) if c == busiest]
        return ans
        
        
        
        
        
#         for i in range(len(arrival)):
#             t, l = arrival[i], load[i]
#             priorityServer = i % k
#             for server in list(range(priorityServer, k, 1)) + list(range(0, priorityServer, 1)):
#                 if nextIdle[server] > t:
#                     continue
#                 nextIdle[server] = t + l
#                 counter[server] += 1
#                 break
#             # throw away request
        
#         ans = []
#         busiest = counter[0]
#         for i, c in enumerate(counter):
#             if c == busiest:
#                 ans.append(i)
#             elif c > busiest:
#                 busiest = c
#                 ans = [i]
#         return ans