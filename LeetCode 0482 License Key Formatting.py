class Solution: #20%
    def licenseKeyFormatting(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        s = S.replace('-','').upper()
        if not s: return '' #corner case: 空
        ans = ''
        length = len(s) #避免重复访问
        for i in range(1, length + 1):
            ans = s[length - i] + ans #逐个取出放到前面
            if not (i) % K:
                ans = '-' + ans #适时添加‘-’
        if ans[0] == '-': return ans[1:] #corner case：长度整除K，则开头就会有‘-’
        return ans