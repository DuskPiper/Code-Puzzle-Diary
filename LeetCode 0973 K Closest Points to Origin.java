class Solution {
    // O(N logN), 45, 88
    // 排序并返回子序列
    public int[][] kClosest(int[][] points, int K) { // 45, 88
        Arrays.sort(points, (p1, p2) -> p1[0] * p1[0] + p1[1] * p1[1] - p2[0] * p2[0] - p2[1] * p2[1]);
        return Arrays.copyOfRange(points, 0, K);
    }
    
    // 用priority queue也是一种办法，O(N logK), 但是费内存且实际效果不太好
    
    
    
    
    // O(N), 100, 12
    // 结合快排、二分，每次找pivot保证其左右的相对大小一致，再比较pivot和K并以此递归，直到pivot = K为止
    public int[][] kClosest(int[][] points, int K) { 
        int len =  points.length, l = 0, r = len - 1;
        while (l <= r) {
            int mid = helper(points, l, r);
            if (mid == K) break;
            if (mid < K) {
                l = mid + 1;
            } else {
                r = mid - 1;
            }
        }
        return Arrays.copyOfRange(points, 0, K);
    }

    private int helper(int[][] A, int l, int r) {
        int[] pivot = A[l];
        while (l < r) {
            while (l < r && compare(A[r], pivot) >= 0) r--;
            A[l] = A[r];
            while (l < r && compare(A[l], pivot) <= 0) l++;
            A[r] = A[l];
        }
        A[l] = pivot;
        return l;
    }

    private int compare(int[] p1, int[] p2) {
        return p1[0] * p1[0] + p1[1] * p1[1] - p2[0] * p2[0] - p2[1] * p2[1];
    }
}