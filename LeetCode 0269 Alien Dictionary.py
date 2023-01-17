class Solution: # 68 60
    def alienOrder(self, words: List[str]) -> str:

        # Build prerequisites map
        prerequisites = {}
        for w in words:
            for c in w:
                if c not in prerequisites:
                    prerequisites[c] = set([])
        
        # Populate prerequisites
        for i in range(len(words) - 1):
            cur = words[i]
            nex = words[i + 1]
            minLen = min(len(cur), len(nex))
            if (cur[:minLen] == nex[:minLen] and len(cur) > len(nex)): # Solve corner case ["abc","ab"]
                return ''
            for j in range(minLen):
                if (cur[j] != nex[j]):
                    prerequisites[nex[j]].add(cur[j])
                    break

        # Do topological sort
        q = []
        ans = []
        for c, pre in prerequisites.items():
            if not pre:
                q.append(c)
        while q:
            c = q.pop()
            ans.append(c)
            for key in prerequisites:
                if c in prerequisites[key]:
                    prerequisites[key].remove(c)
                    if not prerequisites[key]:
                        q.append(key)

        if len(ans) == len(prerequisites):
            return ''.join(ans)
        else:
            return ''