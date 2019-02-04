class Solution { // 51%
    public int findUnsortedSubarray(int[] nums) {
        int[] origin = nums.clone();
        Arrays.sort(nums);
        int i = 0, j = nums.length - 1;
        for (; i < nums.length; i ++) {
            if (nums[i] != origin[i]) break;
        }
        for (; j >=0; j --) {
            if (nums[j] != origin[j]) break;
        }
        return Math.max(0, j - i + 1);
    }
}