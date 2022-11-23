class Solution: # 43 48
    def longestPath(self, parent: List[int], s: str) -> int:
        children = defaultdict(list)
        for i, p in enumerate(parent):
            children[p].append(i)
            
        self.ans = 0
        
        def dfs(i):
            largest, second = 0, 0
            for c in children[i]:
                res = dfs(c) 
                if s[c] != s[i]: # "no pair of adjacent nodes have same char"
                    if res > largest:
                        largest, second = res, largest
                    elif largest >= res > second:
                        second = res
            bestPath = largest + second + 1  # Best path at node i is [i's longest child path + i + i's 2nd longest child path]
            self.ans = max(self.ans, bestPath)
            return largest + 1
        
        dfs(children[-1][0])
        return self.ans