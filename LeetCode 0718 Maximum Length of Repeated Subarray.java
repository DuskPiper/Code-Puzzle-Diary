class Solution { // 67, 46
    public int findLength(int[] A, int[] B) {
        // 动态规划
        if(A == null || B == null) return 0;
        int m = A.length;
        int n = B.length;
        int ans = 0;
        // dp[i][j] 是对于分别结束在i，j的A，B的子串的最长相同子序列的长度
        int[][] dp = new int[m + 1][n + 1];
        for(int i = 0; i <= m; i ++){
            for(int j = 0; j <= n; j ++){
                if(i == 0 || j == 0){ // 对于任意结束在0的子序列，序列长度为0，dp值自然也是0
                    dp[i][j] = 0;
                } else if (A[i - 1] == B[j - 1]) { // 对于结束在i，j的两个序列，如果各自末尾新值也相等，则共同增长长度
                    dp[i][j] = 1 + dp[i - 1][j - 1];
                    ans = ans > dp[i][j] ? ans : dp[i][j]; // 增长后测算记录最长值
                }
            }
        }
        return ans;
    }
}