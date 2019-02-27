class Solution(object): # 95%, 92%
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        indexes = [s.index(ch) for ch in string.ascii_letters if s.count(ch) == 1]
        return min(indexes) if indexes else -1