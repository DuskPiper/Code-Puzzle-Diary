class Solution {
    public int calculate(String s) { // 90, 72
        if (s == null || s.isEmpty()) {
            return 0;
        }
        
        int ans = 0;
        int num = 0;
        int symbol = 1; // +:1  -:-1
        final Stack<Integer> ansStack = new Stack<>();
        final Stack<Integer> symStack = new Stack<>();
        
        for (int i = 0; i < s.length(); i ++) {
            final char c = s.charAt(i);
            if (Character.isDigit(c)) {
                num = num * 10 + (c - '0');
            } else if (c == '+') {
                ans += symbol * num; // 结算上次的结果
                symbol = 1; // 为下次结算预设置值
                num = 0; // 为下次结算预设置值
            } else if (c == '-') {
                ans += symbol * num; // 结算
                symbol = -1; // 为下次结算预设置值
                num = 0; // 为下次结算预设置值
            } else if (c == '(') {
                ansStack.push(ans); // 存储括号前的ans
                symStack.push(symbol); // 存储括号前的sym
                // num = 0; // 不用复位，括号前一定是0
                symbol = 1; // 复位，为括号内的运算作准备
                ans = 0; // 复位
            } else if (c == ')') {
                ans += symbol * num; // 结算，括号内的最后一次结算
                ans = ansStack.pop() + symStack.pop() * ans; // 取得括号前的ans/sym，和括号内的结果做结算
                num = 0; // 复位
                // symbol = 1; // 不需要，括号后面要么结束运算，要么是symbol
            }
        }
        ans += symbol * num; // 最后一个数字，不一定有，没有的话就是0
        return ans;
    }
}
