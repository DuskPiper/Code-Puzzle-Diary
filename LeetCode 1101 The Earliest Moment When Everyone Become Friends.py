class Solution:
    def earliestAcq(self, logs: List[List[int]], n: int) -> int:
        
        def findGroupIndexForPerson(groups, person):
            for i, group in enumerate(groups):
                if person in group:
                    return i
            return -1
        
        if n == 2: return logs[0][0]
        
        logs.sort(key=lambda x: x[0])
        groups = []
        for [timestamp, x, y] in logs:
            xGroupI = findGroupIndexForPerson(groups, x)
            yGroupI = findGroupIndexForPerson(groups, y)
            if xGroupI >= 0 and yGroupI >= 0: # Merge groups
                if xGroupI < yGroupI:
                    groups[xGroupI].update(groups[yGroupI])
                    groups.pop(yGroupI)
                    if len(groups[xGroupI]) == n: return timestamp
                elif xGroupI > yGroupI:
                    groups[yGroupI].update(groups[xGroupI])
                    groups.pop(xGroupI)
                    if len(groups[yGroupI]) == n: return timestamp
            elif xGroupI >= 0:
                groups[xGroupI].add(y)
                if len(groups[xGroupI]) == n: return timestamp
            elif yGroupI >= 0:
                groups[yGroupI].add(x)
                if len(groups[yGroupI]) == n: return timestamp
            else: # New group
                groups.append(set([x, y]))
                
        return -1