class Solution: # 93 97
    def maxChunksToSorted(self, arr: List[int]) -> int: 
        maxOfChunks = [] # Monotonic stack
        for n in arr: 
            newMax = n
            while maxOfChunks and maxOfChunks[-1] > n: 
                newMax = max(newMax, maxOfChunks.pop()) # Merge chunks until n is within right chunk
            maxOfChunks.append(newMax) # Add back the merged chunk
        return len(maxOfChunks)