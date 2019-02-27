class Solution: #59%
    def nextClosestTime(self, time):
        """
        :type time: str
        :rtype: str
        """
        def timeDifference(t1, t2, mAll1): #t2 must be the later one #mAll1是当前时间的总分钟数 
            if t1 == t2: return 1440 #如果两个时间一样，则按差一天算
            #h1, m1 = map(int, t1.split(':'))
            h2, m2 = map(int, t2.split(':'))
            #mAll1 = h1 * 60 + m1
            mAll2 = h2 * 60 + m2 #计算时间2的总分钟数
            if mAll2 < mAll1: mAll2 += 1440 #这样分钟差会为负，则往后推一天
            return mAll2 - mAll1 #返回分钟差，为正
        
        h1, m1 = map(int, time.split(':'))
        mAll1 = h1 * 60 + m1 #计算时间1的总分钟数
        digits = set([time[0], time[1], time[3], time[4]]) #取出所有可能数字
        combines = set([]) #所有可能时间
        for d1 in digits: #逐位考量，最后得到合法的时间表达
            if int(d1) > 2: continue
            for d2 in digits:
                if int(d1) == 2 and int(d2) > 4: continue
                for d3 in digits:
                    if int(d3) > 5: continue
                    for d4 in digits:
                        combines.add(d1 + d2 + ':' + d3 + d4) #计入这个合法的时间表达
        
        minDiff = 1440
        ans = time
        for nextTime in combines: #挨个找最小，如果一样算作1440（算最大）
            diff = timeDifference(time, nextTime, mAll1)
            if diff < minDiff:
                minDiff = diff
                ans = nextTime
        return ans
            
        