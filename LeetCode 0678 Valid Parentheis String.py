class Solution:
    def checkValidString(self, s):
        """
        :type s: str
        :rtype: bool
		刷面经看到推特的OA有这个
        """
        cmin = 0#必须要配对的"("
        cmax = 0#可以配对的"("
        for i in s:
            if i == '(':#遇见"("则通通+1
                cmax += 1
                cmin += 1
            if i == ')':#遇见")"则“可以配对”-1、“必须配对”也-1，但不必为负
                cmax -= 1
                cmin = max(cmin - 1, 0)
            if i == '*':#遇见"#"则“可以配对”+1算作"("、“必须配对”-1算作")"但不必为负
                cmax += 1
                cmin = max(cmin - 1, 0)
            if cmax < 0:#“可以配对”一旦为负，就是在过去的序列种")"已经多于"("了，此时不必继续，直接无效答案
                return False
        return cmin == 0#“必须配对”必须被精准抵消，“可以配对”不必，因为多出来的是"*"