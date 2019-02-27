class Solution:
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
		刷推特OA面经看到
		更简单的方法是haystack.find(needle)
        """
        if not needle:return 0
        i=needle[0]
        l=len(needle)
        for j in range(len(haystack)-l+1):
            if haystack[j]==i:
                if haystack[j:j+l]==needle:
                    return j
        return -1
        