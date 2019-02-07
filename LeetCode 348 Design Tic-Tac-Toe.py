class TicTacToe(object): # 85% Time, 66% RAM

    def __init__(self, n):
        """
        Initialize your data structure here.
        :type n: int
        """
        self.rows = [0] * n # 所有行分别的元素和
        self.cols = [0] * n # 所有列分别的元素和
        self.diag = 0 # 对角线元素和
        self.adia = 0 # 反对角线元素和
        self.n = n

    def move(self, row, col, player):
        """
        Player {player} makes a move at ({row}, {col}).
        @param row The row of the board.
        @param col The column of the board.
        @param player The player, can be either 1 or 2.
        @return The current winning condition, can be either:
                0: No one wins.
                1: Player 1 wins.
                2: Player 2 wins.
        :type row: int
        :type col: int
        :type player: int
        :rtype: int
        """
        # 插入值
        p = player * 2 - 3 # offset, p1 -> -1, p2 -> 1
        self.rows[row] += p # 更新行和
        self.cols[col] += p # 更新列和
        if col == row: self.diag += p # 更新对角线和
        if col + row + 1 == self.n: self.adia += p # 更新反对角线和
        
        if self.n in [self.rows[row], self.cols[col], self.diag, self.adia]: return 2 # 任意和达到n，则该项全是“1”，返回2
        if -self.n in [self.rows[row], self.cols[col], self.diag, self.adia]: return 1 # 任意和达到n则全是“-1”，返回1
        return 0
        
# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)