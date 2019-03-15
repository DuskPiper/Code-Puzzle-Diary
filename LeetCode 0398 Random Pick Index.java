class Solution { // 68, 73
    Random random;
    Map<Integer, List<Integer>> map;

    public Solution(int[] nums) {
        random = new Random();
        map = new HashMap<Integer, List<Integer>>();
        for (int i = 0; i < nums.length; i++) {
            if (!map.containsKey(nums[i]))
                map.put(nums[i], new ArrayList<Integer>());
            map.get(nums[i]).add(i);
        }
    }
    
    public int pick(int target) {
        List<Integer> list = map.get(target);
        return list.get(random.nextInt(list.size()));
    }
}

/**
 * Your Solution object will be instantiated and called as such:
 * Solution obj = new Solution(nums);
 * int param_1 = obj.pick(target);
 */