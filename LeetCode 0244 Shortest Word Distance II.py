class WordDistance: # 80 21

    def __init__(self, wordsDict: List[str]):
        self.dic = {}
        self.l = len(wordsDict)
        for i, word in enumerate(wordsDict):
            if word not in self.dic:
                self.dic[word] = [i]
            else:
                self.dic[word].append(i)

    def shortest(self, word1: str, word2: str) -> int:
        w1i = self.dic[word1]
        w2i = self.dic[word2]
        i, j = 0, 0
        ans = self.l
        while i < len(w1i) and j < len(w2i):
            ans = min(ans, abs(w1i[i] - w2i[j]))
            if w1i[i] < w2i[j]:
                i += 1
            else:
                j += 1
        return ans
            
        


# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(wordsDict)
# param_1 = obj.shortest(word1,word2)