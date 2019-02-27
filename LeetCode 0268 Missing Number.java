class Solution { // 100%, 90%
    public int missingNumber(int[] nums) {
        if (nums == null || nums.length == 0) return 0;
        int theoreticalSum = nums.length * (nums.length + 1) / 2; // 1-n所有数字的和, n * (n + 1) / 2
        int actualSum = 0; // 实际上所有数字的和
        for (int num : nums) {
            actualSum += num;
        }
        return theoreticalSum - actualSum;
    }
}