class Solution(object):
    def findReplaceString(self, s, indices, sources, targets): # 50%, 98%
        """
        :type s: str
        :type indices: List[int]
        :type sources: List[str]
        :type targets: List[str]
        :rtype: str
        """
        s = list(s)
        for i, sor, tar in zip(indices, sources, targets):
            j = i + len(sor)
            indexedStr = ''.join(s[i:j])
            if sor == indexedStr:
                s[i] = tar
                for i2 in range(i + 1, j, 1):
                    s[i2] = ''
        return ''.join(s)