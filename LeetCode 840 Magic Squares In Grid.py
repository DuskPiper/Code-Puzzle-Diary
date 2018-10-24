class Solution:
    def numMagicSquaresInside(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        ans = 0
        x = len(grid[0])
        y = len(grid)
        for i in range(x - 2):
            for j in range(y - 2):
                ans += int(self.isMagic(i, j, grid))#是True就+1
        return ans
                
    def isMagic(self, i, j, grid):
        if not grid[i+1][j+1] == 5:return False #提升速度的法宝：如果中间不为5，则一定错误
        for m in range(i,i+3):#检查数据合法性：是不是0-9
            for n in range(j,j+3):
                if grid[m][n] > 9 or grid[m][n] < 0:
                    return False
        s = sum([grid[i][j], grid[i][j+1], grid[i][j+2]])#这就是所谓相等的那个和
        for k in range(1,3,1):#检查行
            if not sum([grid[i + k][j], grid[i + k][j + 1], grid[i + k][j + 2]]) == s:
                return False
        for k in range(3):#检查列
            if not sum([grid[i][j+k], grid[i+1][j+k], grid[i+2][j+k]]) == s:
                return False
        if not sum([grid[i+k][j+k] for k in range(3)]) == s:#检查对角线
            return False
        if not sum([grid[i+2-k][j+2-k] for k in range(3)]) == s:#检查对角线
            return False
        return True