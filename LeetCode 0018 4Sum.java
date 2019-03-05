class Solution {
    public List<List<Integer>> fourSum(int[] nums, int target) { // 75, 32
        if (nums == null || nums.length < 4)
            return new ArrayList<List<Integer>>();
        Arrays.sort(nums);
        return nSumInSorted(4, nums, target, 0);
    }
    
    private List<List<Integer>> nSumInSorted(int n, int[] nums, int target, int start) { // 制造一个n-sum，以后就不怕了
        // note that nums shall be already sorted
        List<List<Integer>> ans = new LinkedList<List<Integer>>();
        if (n < 2)
            return ans;
        else if (n == 2) {
            // do 2-sum
            int lo = start, hi = nums.length - 1, sum;
            while (lo < hi) {
                sum = nums[lo] + nums[hi];
                if (sum == target) {
                    ans.add(Arrays.asList(nums[lo], nums[hi]));
                    while (lo < hi && nums[lo] == nums[lo + 1])
                        lo++;
                    while (hi > lo && nums[hi] == nums[hi - 1])
                        hi--;
                    lo++; hi--;
                } else if (sum < target) {
                    lo++;
                } else {
                    hi--;
                }
            }
        } else { // n > 2
            // recurse until n = 2
            for (int i = start; i <= nums.length - n; i++) {
                if (i > start && nums[i] == nums[i - 1])
                    continue;
                List<List<Integer>> lowerAns = nSumInSorted(n - 1, nums, target - nums[i], i + 1);
                for (List<Integer> list : lowerAns) {
                    List<Integer> tmpList = new LinkedList<Integer>(list);
                    tmpList.add(0, nums[i]);
                    ans.add(tmpList);
                }
            }
        }
        return ans;
    }
}