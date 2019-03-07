class TicTacToe { // 99, 9
    int n;
    int[] rows;
    int[] cols;
    int diag;
    int adiag;

    /** Initialize your data structure here. */
    public TicTacToe(int n) {
        this.n = n;
        this.rows = new int[n];
        this.cols = new int[n];
        this.diag = 0;
        this.adiag = 0;
        Arrays.fill(rows, 0);
        Arrays.fill(cols, 0);
    }
    
    /** Player {player} makes a move at ({row}, {col}).
        @param row The row of the board.
        @param col The column of the board.
        @param player The player, can be either 1 or 2.
        @return The current winning condition, can be either:
                0: No one wins.
                1: Player 1 wins.
                2: Player 2 wins. */
    public int move(int row, int col, int player) {
        int step = player == 2 ? 1 : -1;
        this.rows[row] += step;
        this.cols[col] += step;
        if (row == col)
            this.diag += step;
        if (row + col == n - 1)
            this.adiag += step;
        
        if (this.rows[row] == n || this.cols[col] == n || this.diag == n || this.adiag == n)
            return 2;
        if (this.rows[row] == -n || this.cols[col] == -n || this.diag == -n || this.adiag == -n)
            return 1;
        return 0;
    }
}

/**
 * Your TicTacToe object will be instantiated and called as such:
 * TicTacToe obj = new TicTacToe(n);
 * int param_1 = obj.move(row,col,player);
 */