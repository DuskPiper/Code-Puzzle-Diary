class Solution(object): # 93%, 2%
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        if len(matrix) > 1:
            n = len(matrix)
            m = n - 1
            def swap(p, q, a, b): matrix[p][q], matrix[a][b] = matrix[a][b], matrix[p][q]
            # Step 1, divide matrix into 4 parts (4个扇叶)
            x = n // 2
            y = n % 2 + x
            # Step 2, 3 swaps, 四个扇叶的四个相应旋转对称的元素，分别参与三轮swap，达到旋转的效果
            for i in range(x):
                for j in range(y):
                    swap(i, j, j, m - i)
                    swap(i, j, m - j, i)
                    swap(m - j, i, m - i, m - j)
            ## LeetCode 满分答案的做法：先纵向翻转图像(matrix.reverse())，再对角线对换(联系现实想像)