class Solution: # 44%, 63%
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        matrix = [[0 for _ in range(len(colSum))] for _ in range(len(rowSum))]
        # greedy
        for r in range(len(rowSum)):
            for c in range(len(colSum)):
                v = min(rowSum[r], colSum[c])
                matrix[r][c] = v
                rowSum[r] -= v
                colSum[c] -= v
        return matrix