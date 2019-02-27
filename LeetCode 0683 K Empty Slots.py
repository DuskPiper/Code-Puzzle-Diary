class Solution: #60%
    def kEmptySlots(self, flowers, k):
        """
        :type flowers: List[int]
        :type k: int
        :rtype: int
        """
        bloomed = [] #已经开放的花，有序
        k += 1 #+1是因为要找中间总数为k的，也就是头-尾为k+1，这里就先加了
        for day, flower in enumerate(flowers, 1): #day从1开始算，然后开始按日子开花
            index = bisect.bisect(bloomed, flower) #寻找当前insert位置会在哪儿，之后考虑其前后邻居之距离 #也可以自己写个binary search
            if index < len(bloomed): #考察后邻居
                if bloomed[index] - flower == k: 
                    return day
            if index > 0 and index <= len(bloomed): #考察前邻居
                if flower - bloomed[index - 1] == k: 
                    return day
            bloomed.insert(index, flower) #放进去，保持有序
        return -1 #最后也没找到结果