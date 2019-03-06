class Solution {
    public int fourSumCount(int[] A, int[] B, int[] C, int[] D) { // 99, 56
        int target = 0;
        // 简化成2sum，因为不需要找出具体的组合
        Map<Integer, Integer> counter = new HashMap<Integer, Integer>();
        int ans = 0;
        for (int a : A) {
            for (int b : B) {
                counter.put(a + b, counter.getOrDefault(a + b, 0) + 1);
            }
        }
        for (int c : C) {
            for (int d : D) {
                ans += counter.getOrDefault(target - c - d, 0);
            }
        }
        return ans;
    }
}