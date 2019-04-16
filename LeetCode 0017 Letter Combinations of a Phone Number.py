class Solution(object):
    dic = [None, None, "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
    
    '''recursion'''
    def letterCombinationsRecursion(self, digits): # 9, 5
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits: return []
        if len(digits) == 1: return list(self.dic[int(digits)])
        ans = []
        for comb in self.letterCombinations(digits[:-1]):
            for digit in self.dic[int(digits[-1])]:
                ans.append(comb + digit)
        return ans
    
    '''iteration'''
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits: return []
        q = [""]
        for digit in digits:
            lastSize = len(q)
            for i in xrange(lastSize):
                lastComb = q.pop(0)
                q += [lastComb + letter for letter in self.dic[int(digit)]]
        return q