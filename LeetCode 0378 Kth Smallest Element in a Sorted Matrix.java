class Solution {
    public int kthSmallest(int[][] matrix, int k) { // 100, 40
        /*quick selection / binary search*/
        int lo = matrix[0][0];
        int hi = matrix[matrix.length - 1][matrix[0].length - 1];
        while (lo < hi) {
            int mid = (hi - lo) / 2 + lo;
            int lesserThanMid = countLesserEqualThanTarget(matrix, mid);
            if (lesserThanMid < k)
                lo = mid + 1;
            else
                hi = mid;
        }
        return lo;
    }
    
    private int countLesserEqualThanTarget(int[][] matrix, int target) { // count #elements <= target
        int count = 0;
        int j = matrix[0].length - 1;
        for (int i = 0; i < matrix.length; i++) {
            while (j >= 0 && matrix[i][j] > target)
                j--;
            count += (j + 1);
        }
        return count;
    }
}