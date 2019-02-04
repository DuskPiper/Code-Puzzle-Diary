class Solution:
    def numsSameConsecDiff(self, N, K): # 100% Time, 65% RAM
        """
        :type N: int
        :type K: int
        :rtype: List[int]
        """
        if N == 0: return [1, 2, 3, 4, 5, 6, 7, 8, 9]
        if N == 1: return [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] # corner case写死
        last = range(1, 10) # last是用来存储上一次的结果的，初始化为所有可能开始数字
        for i in range(N - 1): # 每次循环都往后增加一位数字
            cur = set([]) # cur是存储本次可能结果的暂存器
            for num in last:
                end = num % 10 # 上次循环结果的末尾数字
                if end + K < 10: cur.add(num * 10 + end + K)
                if end - K >= 0: cur.add(num * 10 + end - K)
            last = list(cur) # 循环结束，保存本次循环对应长度的所有可能数字
        return last