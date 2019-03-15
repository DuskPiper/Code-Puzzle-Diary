class Solution {
    public int maximalRectangle(char[][] matrix) { // 72, 91
        if (matrix == null || matrix.length == 0 || matrix[0].length == 0)
            return 0;
        int r = matrix.length;
        int c = matrix[0].length;
        int[][] maxHeight = new int[r][c]; // 当前元素往上全是1的最高高度
        int ans = 0;
        
        for (int i = 0; i < r; i++) {
            for (int j = 0; j < c; j++) {
                if (matrix[i][j] == '0') // 如果当前元素是0，高度一定是0
                    continue;
                // 如果当前元素是1
                maxHeight[i][j] = i == 0 ? 1 : maxHeight[i - 1][j] + 1; // 最高高度是上面元素的高度+1，上面没元素就是1
            }
        }
        
        for (int i = 0; i < r; i++) {
            for (int j = 0; j < c; j++) {
                if (matrix[i][j] == '0')
                    continue;
                // 以当前高度往左右扫描，尽量扫远一点，左右最远之间的距离构成了一个当前高度为高、左右距离为底边的矩形
                int leftmostIndexAtHeight = j, rightmostIndexAtHeight = j;
                while (leftmostIndexAtHeight > 0 && maxHeight[i][leftmostIndexAtHeight - 1] >= maxHeight[i][j])
                    leftmostIndexAtHeight--;
                while (rightmostIndexAtHeight < c - 1 && maxHeight[i][rightmostIndexAtHeight + 1] >= maxHeight[i][j])
                    rightmostIndexAtHeight++;
                ans = Math.max(ans, (rightmostIndexAtHeight - leftmostIndexAtHeight + 1) * maxHeight[i][j]);
            }
        }
        return ans;
    }
}