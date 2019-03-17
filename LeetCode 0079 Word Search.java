class Solution {
    public boolean exist(char[][] board, String word) { // 99.9, 40
        if (board == null || board.length == 0 || board[0].length == 0)
            return false;
        if (word == null || word.length() == 0)
            return true;
        for (int i = 0; i < board.length; i++) {
            for (int j = 0; j < board[0].length; j++) {
                if (board[i][j] == word.charAt(0) && dfs(board, i, j, word, 0))
                    return true;
            }
        }
        return false;
    }
    
    private boolean dfs(char[][] board, int r, int c, String word, int depth) {
        if (depth == word.length()) // search exceeds length, search completed
            return true; 
        if (r < 0 || c < 0 || r >= board.length || c >= board[0].length) // index out of range
            return false;
        if (word.charAt(depth) != board[r][c]) // cur step is incorrect
            return false;
        // Now cur step is correct
        char cur = board[r][c];
        board[r][c] = '#';
        boolean ans = dfs(board, r + 1, c, word, depth + 1)
            || dfs(board, r - 1, c, word, depth + 1)
            || dfs(board, r, c + 1, word, depth + 1)
            || dfs(board, r, c - 1, word, depth + 1);
        board[r][c] = cur;
        return ans;
    }
}