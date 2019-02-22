class Solution(object): # 100%，5%
    def validTicTacToe(self, board):
        """
        :type board: List[str]
        :rtype: bool
        """
        ''' 
        reach this board position 大概有以下需求
        1. 不可能超出一个获胜行列，除非他们share一个棋子 
           其实“同阵营两个不相交行/列获胜”的情况被棋子数量限制包括了，所以不必额外单独检查
           唯一需要检查的是两方不能同时获胜
        2. 后手O获胜的情况下，棋子数量差别只能是0(X=O)
        3. 前手X获胜的情况下，棋子数量差别只能是1(X>O)
        4. 无论怎样，X总数一定比O总数多1或者0个
        '''
        b = board[0] + board[1] + board[2]
        X_num, O_num = b.count('X'), b.count('O') # X O 棋子总数
        X_win_count, O_win_count = 0, 0 # X O 胜利总数
        for st in (b[0::3], b[1::3], b[2::3], # 列
                   b[0:3], b[3:6], b[6:], # 行
                   b[0::4], b[2:8:2]): # 对角线
            if st == 'XXX': X_win_count += 1
            elif st == 'OOO': O_win_count += 1
        
        if X_win_count and O_win_count: return False  # 1. 两方不能同时获胜
        elif X_win_count: return X_num - O_num == 1 # 3.
        elif O_win_count: return X_num == O_num # 2.
        else: return X_num - O_num in (0, 1) # 4.