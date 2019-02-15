class Solution(object): # 69%, 100%
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        # 这个网格的每一项表示对应的两个子串之间的编辑距离，左上角当然是1或者0，因为是最短的子串
        # 由此动态规划，最右下角为答案，也就是两个子串就是word1和word2本身
        #   _ h o r s e < word1
        # _ 0 1 2 3 4 5
        # r 1 1 2 2 3 4
        # o 2 2 x y
        # s 3 3
        # ^ word2
        #    ^ y = min(x, 2, 2) + 1 如果对应字符不同的话；对应字符相同则是特殊情况，因为不再需要额外操作 比如这里x其实该等于左上角的1，因为相当于两个子串同时去除末尾各自的相等的这个元素o
        #      x位置的编辑距离是其左、上、左上中最小值+1
        #      左和上可以分别表示删除和添加（不分先后），左上表示更改，这三种操作离当前格的距离都算作1，因为都是一次操作
    
        # Initialize
        l1, l2 = len(word1), len(word2)
        if not l1: return l2
        if not l2: return l1
        grid = [[0 for _ in range(l1 + 1)] for _ in range(l2 + 1)]
        for col in range(l1 + 1): grid[0][col] = col 
        for row in range(l2 + 1): grid[row][0] = row
        # Calc
        for col in range(1, l1 + 1):
            for row in range(1, l2 + 1):
                if word1[col - 1] == word2[row - 1]: # 对应字符相同是特殊情况，因为不再需要额外操作、相当于两个子串同时去除末尾各自的相等的这个元素o
                    grid[row][col] = grid[row - 1][col - 1]
                else: # 对应字符不同，则是动态规划，是三个方向最小值 + 1（即加上本身这一步的值）
                    grid[row][col] = min(grid[row - 1][col], grid[row][col - 1], grid[row - 1][col - 1]) + 1
        #for row in grid: print(row)
        return grid[-1][-1]