class Solution {
    public int mySqrt(int x) { // 99.9, 61
        if (x == 1) // prevent /by0
            return 1;
        int lo = 0;
        int hi = x;
        while (lo < hi) {
            int mid = lo + (hi - lo) / 2; // 防溢出
            if (mid <= x / mid && mid + 1 > x / (mid + 1)) // 用x/mid而不是mid*mid，防int溢出
                return mid;
            else if (mid > x / mid)
                hi = mid;
            else if (mid < x / mid)
                lo = mid;
        }
        return x;
    }
}