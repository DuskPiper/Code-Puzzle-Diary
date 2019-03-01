class Solution { // 100，16
    public int search(int[] nums, int target) {
        // Binary Search 找 pivot
        int lo = 0, hi = nums.length - 1, mid = 0, realmid;
        while (lo < hi) {
            mid = (int)(lo + hi) / 2;
            if (nums[mid] > nums[hi]) { // go right
                lo = mid + 1; // +1 是因为之前 /2 的时候可能会舍去0.5
            } else { // go left  
                hi = mid;
            }
        }
        
        int offset = lo; // 找到pivot，当offset用
        
        lo = 0;
        hi = nums.length - 1;
        while (lo <= hi) {
            mid = (int)(lo + hi) / 2;
            realmid = (mid + offset) % nums.length; // 利用offset计算真实的mid val的index
            if (nums[realmid] == target) return realmid;
            else if (nums[realmid] > target) hi = mid - 1;
            else lo = mid + 1;
        }
        return -1;
    }
}