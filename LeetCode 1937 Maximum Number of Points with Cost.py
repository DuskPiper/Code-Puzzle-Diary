class Solution:
    def maxPoints(self, points: List[List[int]]) -> int: # 29%, 93%
        r, c = len(points), len(points[0])
        # DP
        prevRowAns = points[0]
        for rowNum in range(1, r): # 传统DP：行行递进，将每行的列更新成此含义：“当我抵达这行，选择这列的话，最佳累计结果是多少”
            
            # 第二层DP，分别记录该列从左/右能拿到的最优前值(即把上一行的各列累积值给加权上距离，并顺序找一次记录迄今最好值)
            bestValIfConcatFromLeft, bestValIfConcatFromRight = prevRowAns[:], prevRowAns[:]
            for i in range(1, c):
                bestValIfConcatFromLeft[i] = max(bestValIfConcatFromLeft[i], bestValIfConcatFromLeft[i - 1] - 1)
            for i in range(c - 2, -1, -1):
                bestValIfConcatFromRight[i] = max(bestValIfConcatFromRight[i], bestValIfConcatFromRight[i + 1] - 1)
                
            # 对于新行的每列，找max(left[i], right[i])， 从而确定该列最优解
            rowAns = [v + max(bestValIfConcatFromRight[i], bestValIfConcatFromLeft[i]) for i, v in enumerate(points[rowNum])]
            
            prevRowAns = rowAns[:]
            print('R: ' + str(bestValIfConcatFromRight))
            print(rowAns)
        return max(prevRowAns)