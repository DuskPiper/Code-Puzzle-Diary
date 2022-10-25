class Solution: # 69, 64
    def closestNode(self, n: int, edges: List[List[int]], query: List[List[int]]) -> List[int]:
        
        edgeMap = defaultdict(list)
        for e1, e2 in edges:
            edgeMap[e1].append(e2)
            edgeMap[e2].append(e1)
        
        def dfs(source, target, visited):
            visited.add(source)
            if source == target:
                return [source]
            for n in edgeMap[source]:
                if n not in visited:
                    res = dfs(n, target, visited)
                    if res:
                        return [source] + res
            return None
        
        def bfs(sources, targets, visited):
            nextRound = set([])
            for s in sources:
                visited.add(s)
                if s in targets:
                    return s
                for n in edgeMap[s]:
                    if n not in visited:
                        nextRound.add(n)
            return bfs(nextRound, targets, visited)
            
        
        ans = []
        for start, end, target in query:
            route = dfs(start, end, set([]))
            a = bfs(set([target]), set(route), set([]))
            ans.append(a)
            
        return ans
        