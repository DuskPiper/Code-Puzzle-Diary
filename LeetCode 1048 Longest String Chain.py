class Solution(object):
    def longestStrChain(self, words): # 91%, 74%
        """
        :type words: List[str]
        :rtype: int
        """
        words = sorted(words, key=len) 
        ans = 1
        bestAnsAtWord = {} # 增长DP，词长度递增，记录递增到该词时的目前最佳长度
        for w in words: # 词长度递增
            bestAnsAtWord[w] = 1
            for pivot in range(len(w)): # 当前词所有可能pred
                pred = w[:pivot] + w[pivot + 1:]
                if pred in bestAnsAtWord: # 如果pred存在于map，说明该词存在于words，那么当前词答案+1
                    bestAnsAtWord[w] = max(bestAnsAtWord[w], bestAnsAtWord[pred] + 1)
            ans = max(ans, bestAnsAtWord[w])
        return ans
        