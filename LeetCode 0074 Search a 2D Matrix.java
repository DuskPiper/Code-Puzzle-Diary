class Solution {
    public boolean searchMatrix(int[][] matrix, int target) { // 100, 18
        if (matrix == null || matrix.length == 0 || matrix[0].length == 0)
            return false;
        int r = matrix.length;
        int c = matrix[0].length;
        int lo = 0;
        int hi = r * c - 1;
        while (lo < hi) {
            int mid = lo + (hi - lo) / 2;
            int midVal = matrix[mid / c][mid % c];
            if (midVal > target)
                hi = mid;
            else if (midVal < target)
                lo = mid + 1;
            else
                return true;
        }
        return matrix[lo / c][lo % c] == target;
    }
}