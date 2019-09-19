class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:  # 49, 7
        if len(matrix) <= 1:
            return True
        width = len(matrix[0])
        for row in range(len(matrix) - 1):  # No need for checking last row
            for col in range(width - 1):
                if matrix[row][col] != matrix[row + 1][col + 1]:
                    return False
        return True
