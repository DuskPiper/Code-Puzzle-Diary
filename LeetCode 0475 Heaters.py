class Solution: #9%
    def findRadius(self, houses, heaters):
        """
        :type houses: List[int]
        :type heaters: List[int]
        :rtype: int
        """
        def binary_insert(house, heaters): #二分插入
            i, j = 0, len(heaters) - 1
            while i < j - 1:
                m = (i + j) // 2
                mid = heaters[m]
                if house > mid: i = m
                elif house < mid: j = m
                else: return min(m, j-1)
            return i
        heaters = sorted(heaters)
        heaters.append(float('inf'))
        dist = []
        for house in houses: #逐个找当前house的最小距离
            i = binary_insert(house, heaters)
            dist.append(min(abs(heaters[i] - house), abs(heaters[i + 1] - house)))#house向前/后的heater的最小值，即最近heater
        return max(dist) #所有house的最近heater距离中的最大值
            
            
        
        