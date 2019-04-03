class Solution {
    public int countBattleships(char[][] board) { // 99.5, 5
        if (board == null || board.length == 0 || board[0].length == 0)
            return 0;
        int counter = 0;
        int row = board.length;
        int col = board[0].length;
        for (int i = 0; i < row; i++) {
            for (int j = 0; j < col; j++) {
                if (board[i][j] == 'X' && (i == row - 1 || board[i + 1][j] == '.') && (j == col - 1 || board[i][j + 1] == '.'))
                    counter ++;
            }
        }
        return counter;
    }
}