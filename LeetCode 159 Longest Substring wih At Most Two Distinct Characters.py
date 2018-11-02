class Solution: #81%
    def lengthOfLongestSubstringTwoDistinct(self, s):
        """
        :type s: str
        :rtype: int
        """
        start = 0 #检查窗口开始指针
        kinds = 0 #当前窗口总种数（合法是<=2）
        dic = {} #当前窗口字符数量统计
        ans = 0 
        for end, char in enumerate(s): #end是检查窗口结束指针，随着for循环后移；char是后移时右边新增的字符
            if dic.get(char, 0): dic[char] += 1 #新增字符存在字典中，此时种类不会增加，仅仅计数增加
            else: #新增字符不存在字典中，种类数+1
                dic[char] = 1
                kinds += 1
            while kinds > 2: #保证当前for循环结束的时候kinds大小合法
                dic[s[start]] -= 1 #窗口左指针准备右移，如果弹出的左字符仅此一个，弹出后kinds就要-1
                if not dic.get(s[start], 0): kinds -= 1 #弹出后不再有该字符，则kinds-=1
                start += 1 #完成窗口指针右移
            if end - start + 1 > ans: ans = end - start + 1 #记录最大值
        return ans