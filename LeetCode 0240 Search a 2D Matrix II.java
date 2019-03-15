class Solution {
    public boolean searchMatrix(int[][] matrix, int target) { // 100, 50
        if (matrix == null || matrix.length == 0 || matrix[0].length == 0)
            return false;
        // 从左下角或右上角开始binary search
        int r = matrix.length;
        int c = matrix[0].length;
        int x = r - 1;
        int y = 0;
        while (x >= 0 && y < c) {
            int cur = matrix[x][y];
            if (cur == target)
                return true;
            else if (cur > target)
                x--;
            else
                y++;
        }
        return false;
    }
}