class Solution {
    public int rob(int[] nums) { // 100, 7
        /*in-place*/
        return robHelper(nums, 0, nums.length);
    }
    
    private int robHelper(int[] nums, int i, int j) {
        if (i >= j)
            return 0;
        if (j - i == 1)
            return nums[i];
        if (j - i == 2)
            return Math.max(nums[i], nums[i + 1]);
        int mid = (i + j) / 2;
        return Math.max(
            robHelper(nums, i, mid - 1) + robHelper(nums, mid + 2, j) + nums[mid], // rob mid
            robHelper(nums, i, mid) + robHelper(nums, mid + 1, j) // don't rob mid
        );
    }
}