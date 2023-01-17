class Solution: # 60 20
    def maxLength(self, arr: List[str]) -> int:
        # Basically brute force, but with some optm
        strSets = [set()] # each item is a set and represent a str
        for a in arr:
            if len(a) != len(set(a)): # The word contains duplicates & is unusable
                continue
            a = set(a)
            for s in strSets:
                if not s & a:
                    strSets.append(s | a)
        return max(len(s) for s in strSets)
