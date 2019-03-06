class Solution {
    public int maxProfit(int[] prices) { // 100, 92
        if (prices == null || prices.length < 1)
            return 0;
        int leastSoFar = prices[0];
        int ans = 0;
        for (int p : prices) {
            ans = Math.max(p - leastSoFar, ans);
            leastSoFar = Math.min(leastSoFar, p);
        }
        return ans;
    }
}