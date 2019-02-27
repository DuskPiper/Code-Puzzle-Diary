class Solution(object): # 100% Time, 60% RAM
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        return " ".join(filter(lambda x: x!= " ", s.strip().split()[::-1]))
        # strip(): 或者strip(" ")，剥皮掉空格开始结尾
        # split(): 或者split(" ")，分割词汇为序列
        # [::-1]: 高效版reversed()
        # filter(lambda..., list): 去除空格元素，是Leetcode新加的corner case所以老答案会错
        # " ".join(): 插入新空格成句子