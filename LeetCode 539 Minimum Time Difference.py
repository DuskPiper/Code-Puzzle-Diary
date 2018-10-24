class Solution:
    def findMinDifference(self, timePoints): #95.56%
        """
        :type timePoints: List[str]
        :rtype: int
        """
        if len(timePoints) > 1440 : return 0 #抽屉原理，大幅提高效果
        def diff(tp1, tp2):#tp1<tp2 #该函数计算两个时间的分钟差，前提是第一个比第二个小
            h1, m1, h2, m2 = map(int, tp1.split(":") + tp2.split(":"))
            return (h2 - h1) * 60 + m2 - m1
        tps = sorted(timePoints) #string排序
        h, m = map(int, tps[0].split(":"))
        tps.append(str(h + 24) + ':' +str(m)) #把第一项时间+24hr放到最后，语义时间不变但是string大小最大，构成大小回环
        return min([diff(tps[i],tps[i+1]) for i in range(len(tps) - 1)]) #挨个计算每两个时间的差值，返回最小值
    