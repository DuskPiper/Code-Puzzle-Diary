import heapq
class Solution(object): # 8%, 100%
    def getOrder(self, tasks):
        """
        :type tasks: List[List[int]]
        :rtype: List[int]
        """
        for i in range(len(tasks)):
            tasks[i].append(i)
        tasks.sort(key=lambda t: t[0])
        
        res = []
        curTime = tasks[0][0]
        readyPool = [] # Heap
        
        while tasks or readyPool:
            # Enqueue all ready tasks
            while tasks and curTime >= tasks[0][0]: # Heap-push all ready tasks
                task = tasks.pop(0)
                heapq.heappush(readyPool, (task[1], task[2])) # (processTime, originalIndex)
            
            
            if readyPool:
                # Execute
                processingTime, originalIndex = heapq.heappop(readyPool) # Heap-pop best ready task
                res.append(originalIndex)
                curTime += processingTime
            else: # no ready task now, skip to next ready
                curTime = tasks[0][0]
            
        return res
            
                
                
            
        