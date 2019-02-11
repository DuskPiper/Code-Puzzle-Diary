class Solution(object): # 7% Time, 7% RAM
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        for _ in range(k): # k轮循环，每轮删除一位
            flag = True # 记录本轮是否在for中删除数字，删除了则为False，未删除则删除最后一位
            for i in range(len(num) - 1): # 逐位检查
                if num[i] > num[i + 1]: # 如果本位大于下一位，则删除本位
                    num = num[:i] + num[i + 1:] #删除本位
                    flag = False
                    break; # 删除最后一位
            if flag: num = num[:-1] # 本轮外循环未删除数字则删除最后一位
        return num.lstrip('0') or "0" # 去除前面的0，并且返回空为“0”