class Solution {
    public int uniquePaths(int m, int n) { // 100, 24
        // DP
        int[][] grid = new int[n][m];
        for (int r = 0; r < n; r++)
            for (int c = 0; c < m; c++)
                grid[r][c] = (r == 0 || c == 0) ? 1 : grid[r - 1][c] + grid[r][c - 1];
        return grid[n - 1][m - 1];
    }
}