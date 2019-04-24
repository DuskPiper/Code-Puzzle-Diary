class Solution:
    def largestSumOfAverages(self, A: List[int], K: int) -> float: # 57, 8
        calculated = {} # (n, k) -> ans
        def dpRec(n: int, k: int) -> float:
            '''<=> largestSumOfAverage(A[:n], k)'''
            if not k or n < k:
                return 0
            if (n, k) in calculated:
                pass
            elif k == 1:
                calculated[n, k] = sum(A[:n]) / float(n)
            else:
                sumVal, calculated[n, k] = 0, 0
                for i in range(n - 1, 0, -1):
                    sumVal += A[i]
                    calculated[n, k] = max(calculated[n, k], dpRec(i, k - 1) + sumVal / float(n - i)) # DP
            return calculated[n, k]
        return dpRec(len(A), K)
            