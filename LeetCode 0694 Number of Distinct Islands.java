class Solution {
    public int numDistinctIslands(int[][] grid) { // 73, 44
        Set<String> islandFeatures = new HashSet<String>();
        for (int r = 0; r < grid.length; r++) {
            for (int c = 0; c < grid[0].length; c++) {
                if (grid[r][c] == 1) {
                    StringBuilder feature = new StringBuilder(); // use feature string to represent shape of island, each char of string means a traverse step
                    dfs(grid, r, c, feature, '0');
                    islandFeatures.add(feature.toString());
                }
            }
        }
        return islandFeatures.size();
    }
    
    private void dfs(int[][] grid, int r, int c, StringBuilder feature, char curStep) {
        if (r < 0 || c < 0 || r >= grid.length || c >= grid[0].length || grid[r][c] != 1) {// invalid index or is water or is visited
            feature.append('r'); // meaning return step
            return;
        }
        feature.append(curStep);
        grid[r][c] = 2; // "2" means visited
        
        // Now do next move
        dfs(grid, r, c + 1, feature, 'r');
        dfs(grid, r, c - 1, feature, 'l');
        dfs(grid, r - 1, c, feature, 'u');
        dfs(grid, r + 1, c, feature, 'd');
        feature.append('r'); // meaning return step
    }
}