class Solution {
    public int maxKilledEnemies(char[][] grid) { // 97, 72
        // DP 假设没有墙，那么每个row和col的点都会分别有相同的row-killer或col-killed值
        // 因此可以避免大量重复计算，只需要计算第一行/列的值，后面照抄
        // 现在考虑有墙，则遇到墙以后，需要重新计算行/列的值，其实也相当于另起新行
        if (grid == null || grid.length == 0 || grid[0].length == 0) return 0;
        int ans = 0;
        int[] colResults = new int[grid[0].length]; // 长度为列数，存储每一列→最新←的killed值，所谓最新，是指的遇到第一行就初始化、遇到列上的墙就重新初始化
        int rowResult = 0; // 不需要array了，因为下面外层循环是行，我们不在乎过去一行的结果了，所以一个值足够存储当前最新的killed值
        
        for (int i = 0; i < grid.length; i++) {
            for (int j = 0; j < grid[0].length; j++) {
                if (grid[i][j] == 'W') continue; // 遇到墙跳过，不必更新值，也不必记录
                if (j == 0 || grid[i][j - 1] == 'W') // 新起一行，或者在行上面刚才遇到墙
                    rowResult = getRowResult(grid, i, j); // 初始化/更新行killed值
                if (i == 0 || grid[i - 1][j] == 'W')  // 在第一行，也就是每一列的第一个，或者在列上面刚才遇到墙
                    colResults[j] = getColResult(grid, i, j); // 初始化/更新当前列的最新killed值
                
                if (grid[i][j] == '0' && rowResult + colResults[j] > ans) // 只要当前位置能放炸，就试着合并行列最新killed值计算当前killed总值，更新答案
                    ans = rowResult + colResults[j];
            }
        }
        return ans;
    }
    
    public int getRowResult(char[][] grid, int i, int j) { // 初始化/更新当前位置的最新行killed值，也就是在这里放炸能炸到的这行的人数
        int counter = 0;
        while (j < grid[0].length && grid[i][j] != 'W') // 只往右数、不往左，因为默认调用的时候，左边是矩阵左边缘(初始化)或者是墙(更新)，数到墙或者矩阵右边缘为止
            if (grid[i][j++] == 'E') counter++;
        return counter;
    }
    
    public int getColResult(char[][] grid, int i, int j) { // 初始化/更新当前位置的最新列killed值，也就是在这里放炸能炸到的这列的人数
        int counter = 0;
        while (i < grid.length && grid[i][j] != 'W') // 往下数到墙或边缘
            if (grid[i++][j] == 'E') counter++;
        return counter;
    }
}