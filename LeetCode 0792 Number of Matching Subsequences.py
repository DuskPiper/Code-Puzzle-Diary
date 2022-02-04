class Solution(object):
    def numMatchingSubseq(self, s, words): # 36%, 63%
        """
        :type s: str
        :type words: List[str]
        :rtype: int
        """
        # 逐字走一遍s，遇到一个char就把正在期待该char的word的期待char更新为该word的下一位char
        charToCharExpecters = collections.defaultdict(list) # 存储char->期待该char的words
        ans = 0
        for w in words:
            charToCharExpecters[w[0]].append(w)
        for c in s:
            cExpecters = list(charToCharExpecters[c])
            charToCharExpecters[c] = []
            for w in cExpecters:
                if len(w) == 1:
                    ans += 1
                else:
                    wCutShort = w[1:]
                    charToCharExpecters[wCutShort[0]].append(wCutShort)
        return ans