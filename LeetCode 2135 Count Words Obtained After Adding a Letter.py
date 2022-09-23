class Solution: # 29, 31
    def wordCount(self, startWords: List[str], targetWords: List[str]) -> int:
        def getFeature(word):
            l = [0] * 26
            for c in word:
                l[ord(c) - ord('a')] = 1
            return l
        
        startFeatures = set([str(getFeature(word)) for word in startWords])
        
        ans = 0
        for w in targetWords:
            feature = getFeature(w)
            for c in w:
                feature[ord(c) - ord('a')] = 0
                if str(feature) in startFeatures:
                    ans += 1
                    break
                feature[ord(c) - ord('a')] = 1
        return ans
        
            
                