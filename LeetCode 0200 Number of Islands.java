class Solution {
    public int numIslands(char[][] grid) { // 99.9, 65
        if (grid == null || grid.length == 0 || grid[0].length == 0)
            return 0;
        int r = grid.length;
        int c = grid[0].length;
        int count = 0;
        for (int i = 0; i < r; i++) {
            for (int j = 0; j < c; j++) {
                if (grid[i][j] == '1') {
                    mark(grid, i, j);
                    count++;
                }
            }
        }
        return count;
    }
    
    private void mark(char[][]grid, int i, int j) {
        if (i < 0 || j < 0 || i >= grid.length || j >= grid[0].length)
            return;
        if (grid[i][j] != '1')
            return;
        grid[i][j] = '2';
        mark(grid, i + 1, j);
        mark(grid, i - 1, j);
        mark(grid, i, j + 1);
        mark(grid, i, j - 1);
    }
}