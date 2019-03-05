class Solution {
    public int maxTurbulenceSize(int[] A) { // 99, 29
        // DP 既然条件中有两种情况，那解答就按两种算
        // 利用Turbulence Size End At I来动态增长或清零，来实现DP
        if (A == null || A.length == 0)
            return 0;
        int ans = 1;
        int turSizeEndAtI = 1;
        // case 1, odd -> Ak > Ak+1 ; even -> Ak < Ak+1
        for (int i = 1; i < A.length; i++) {
            if (i % 2 == 0) // even i
                turSizeEndAtI = A[i] < A[i - 1] ? turSizeEndAtI + 1 : 1;
            else // odd i
                turSizeEndAtI = A[i] > A[i - 1] ? turSizeEndAtI + 1 : 1;
            
            if (turSizeEndAtI > ans)
                ans = turSizeEndAtI;
        }
        
        turSizeEndAtI = 1;
        // case 2, odd -> Ak < Ak+1 ; even -> Ak > Ak+1
        for (int i = 1; i < A.length; i++) {
            if (i % 2 == 0) // even i
                turSizeEndAtI = A[i] > A[i - 1] ? turSizeEndAtI + 1 : 1;
            else // odd i
                turSizeEndAtI = A[i] < A[i - 1] ? turSizeEndAtI + 1 : 1;
            
            if (turSizeEndAtI > ans)
                ans = turSizeEndAtI;
        }
        
        return ans;
    }
}