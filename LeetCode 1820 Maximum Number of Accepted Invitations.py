class Solution: # 32, 63
    def maximumInvitations(self, grid: List[List[int]]) -> int:
        numBoys, numGirls = len(grid), len(grid[0])
        pairs = {} # girl:boy
        
        def dfs(boy, askedGirls):  # I'm a boy, I have a blacklist and whitelist
            for girl in range(numGirls):  # Ask every girl
                if girl not in askedGirls and grid[boy][girl]:   # Ask every girl on whitelist & not on blacklist
                    askedGirls.add(girl)  # Add girl to blacklist (the girl had been asked)
                    if girl not in pairs: # The girl is not yet invited
                        pairs[girl] = boy
                        return True
                    elif dfs(pairs[girl], askedGirls):  # The girl is already invited, so now I'm asking that paired boy to find a substitude
                        pairs[girl] = boy # That paired boy found substitude, so I can pair with girl
                        return True
            return False
        
        for boy in range(numBoys):
            dfs(boy, set([]))
        
        return len(pairs)