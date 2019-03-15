class Solution {
    public int searchInsert(int[] nums, int target) { // 100, 6
        if (nums == null || nums.length == 0)
            return 0;
        int lo = 0, hi = nums.length - 1;
        if (target < nums[0])
            return 0;
        if (target > nums[hi])
            return nums.length;
        while (lo <= hi) {
            int mid = (lo + hi) / 2;
            if (nums[mid] > target)
                hi = mid - 1;
            else if (nums[mid] < target)
                lo = mid + 1;
            else
                return mid;
        }
        return lo;
    }
}