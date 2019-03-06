class Solution {
    public int maxProfit(int[] prices) { // 99, 98
        // 贪婪，根据下一次价格，在所有转折点买进卖出，赚到所有上升区间的钱
        if (prices == null || prices.length == 0)
            return 0;
        int ans = 0;
        boolean bought = false;
        int buyPrice = 0;
        for (int i = 0; i < prices.length - 1; i++) {
            if (prices[i] < prices[i + 1] && !bought) {
                bought = true;
                buyPrice = prices[i];
            } else if (prices[i] > prices[i + 1] && bought) {
                bought = false;
                ans += prices[i] - buyPrice;
            }
        }
        if (bought) // 最后一份price，这时候无论如何都要卖了
            ans += (prices[prices.length - 1] - buyPrice);
        return ans;
    }
}