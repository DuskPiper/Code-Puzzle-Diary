class Solution(object):
    def longestSubstring(self, s, k): # 79 6
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        for char in set(s): # 挨个字符排查
            if s.count(char) < k: # 找到不满k次的字符
                return max([self.longestSubstring(subString, k) for subString in s.split(char)]) # 按此不满k的字符split，得到子串(不含char本身)分别递归，取所有结果max
        return len(s) # 找不到不满k次的字符，整个string都是满足的