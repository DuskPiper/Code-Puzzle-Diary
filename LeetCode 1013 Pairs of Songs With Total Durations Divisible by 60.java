class Solution {
    public int numPairsDivisibleBy60(int[] time) {
        Map<Integer, Integer> counter = new HashMap<Integer, Integer>();
        int ans = 0;
        for (int t : time) {
            ans += counter.getOrDefault((60 - t % 60) % 60, 0); // 外层%60是防止内层整除
            Integer key = t % 60;
            counter.put(key, 1 + counter.getOrDefault(key, 0));
        }
        return ans;
    }
}