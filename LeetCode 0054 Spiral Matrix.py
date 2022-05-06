class Solution: # 21, 83
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        left = 0
        right = len(matrix[0]) - 1
        top = 0
        bottom = len(matrix) - 1
        res = []
        
        while left <= right or top <= bottom:
            # left->right
            if top <= bottom:
                i = top
                for j in range(left, right + 1, 1):
                    res.append(matrix[i][j])
                top += 1
            # up->down
            if left <= right:
                j = right
                for i in range(top, bottom + 1, 1):
                    res.append(matrix[i][j])
                right -= 1
            # right->left
            if top <= bottom:
                i = bottom
                for j in range(right, left - 1, -1):
                    res.append(matrix[i][j])
                bottom -= 1
            # bottom->top
            if left <= right:
                j = left
                for i in range(bottom, top - 1, -1):
                    res.append(matrix[i][j])
                left += 1
        return res