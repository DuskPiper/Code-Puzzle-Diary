class Solution { // 75, 41
    int[] origin;
    Random random;

    public Solution(int[] nums) {
        origin = nums;
        random = new Random();
    }
    
    /** Resets the array to its original configuration and return it. */
    public int[] reset() {
        return origin;
    }
    
    /** Returns a random shuffling of the array. */
    public int[] shuffle() {
        // 克隆一个list然后把每一位随机swap
        int len = origin.length;
        int[] ans = origin.clone();
        for (int i = 0; i < len; i++) {
            int r = random.nextInt(len);
            int tmp = ans[i];
            ans[i] = ans[r];
            ans[r] = tmp;
        }
        return ans;
    }
}

/**
 * Your Solution object will be instantiated and called as such:
 * Solution obj = new Solution(nums);
 * int[] param_1 = obj.reset();
 * int[] param_2 = obj.shuffle();
 */