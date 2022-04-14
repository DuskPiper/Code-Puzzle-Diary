class Solution(object): # 32, 97
    def findBuildings(self, heights):
        """
        :type heights: List[int]
        :rtype: List[int]
        """
        highest = 0
        res = []
        for i in range(len(heights) - 1, -1, -1):
            if heights[i] > highest:
                res.append(i)
                highest = heights[i]
        return reversed(res)