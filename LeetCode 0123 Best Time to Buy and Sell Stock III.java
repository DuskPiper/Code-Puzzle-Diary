class Solution {
    public int maxProfit(int[] prices) { // 100, 96
        // 这题挺难的，参考LeetCode 121 122
        int buyPrice1 = Integer.MAX_VALUE; // 第一次买入花的钱，此时相应地账户余额 -buyprice1
        int earnPrice1 = 0; // 第一次卖出后赚到的钱
        int buyPrice2 = Integer.MAX_VALUE; // 第二次买入花的钱
        int earnPrice2 = 0; // 第二次卖出后赚到的钱
        for (int price : prices) {
            buyPrice1 = Math.min(buyPrice1, price);
            earnPrice1 = Math.max(earnPrice1, price - buyPrice1);
            buyPrice2 = Math.min(buyPrice2, price - earnPrice1); // 关键在这里，第二次买入的时候花掉第一次的收入“earnPrice1”，这样就把两次交易联系起来了
            earnPrice2 = Math.max(earnPrice2, price - buyPrice2);
        }
        return earnPrice2;
    }
}