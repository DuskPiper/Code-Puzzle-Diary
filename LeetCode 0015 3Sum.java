class Solution {
    public List<List<Integer>> threeSum(int[] nums) { // 99.7, 88
        List<List<Integer>> ans = new LinkedList<List<Integer>>();
        if (nums.length < 3)
            return ans;
        Arrays.sort(nums);
        for (int i = 0; i < nums.length - 2; i++) {
            int lo = i + 1, hi = nums.length - 1, target = 0 - nums[i], sum;
            if (i > 0 && nums[i] == nums[i - 1]) // corner case
                continue;
            while (lo < hi) {
                sum = nums[lo] + nums[hi];
                if (sum == target) { // found pair
                    ans.add(Arrays.asList(nums[i], nums[lo], nums[hi]));
                    while (lo < hi && nums[lo + 1] == nums[lo])
                        lo++;
                    while (lo < hi && nums[hi - 1] == nums[hi])
                        hi--;
                    lo++;
                    hi--;
                } else if (sum < target) {
                    lo++;
                } else {
                    hi--;
                }
            }
        }
        return ans;
    }
}