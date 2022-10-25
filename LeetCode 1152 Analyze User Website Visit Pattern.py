class Solution: # 99 96
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        history = sorted(zip(username, timestamp, website))
        
        userHistory = defaultdict(list)  # user -> (timestamp, website)
        for u, t, w in sorted(zip(username, timestamp, website)):
            userHistory[u].append(w)
            
        counter = collections.Counter()
        for u, ws in userHistory.items():
            counter.update(set(combinations(ws, 3)))
                
        maxCount = max(counter.values())
        maxPatterns = [p for p, c in counter.items() if c == maxCount]

        return sorted(maxPatterns)[0]
                
        