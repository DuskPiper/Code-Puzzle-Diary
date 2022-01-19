class Solution {
    public int calculate(String s) { // 72, 37
        if (s == null || s.isEmpty()) {
            return 0;
        }
        final Stack<Integer> numStack = new Stack<>(); // 数字暂存，进栈时数字已转化为只需要+的格式，详见下面实现
        int num = 0;
        char lastSymbol = '+'; // 默认 0 + 整个算式
        
        for (int i = 0; i < s.length(); i ++) {
            final char c = s.charAt(i);
            if (Character.isDigit(c)) {
                num = num * 10 + (c - '0');
            }
            if (c == '+' || c == '-' || c == '*' || c == '/' || i == s.length() - 1) { // 当前是+-x/或者是算式结尾
                // 结算现目前的num和上次的symbol
                if (lastSymbol == '+') {
                    numStack.push(num);
                } else if (lastSymbol == '-') {
                    numStack.push(0 - num);
                } else if (lastSymbol == '*') {
                    numStack.push(numStack.pop() * num);
                } else if (lastSymbol == '/') {
                    numStack.push(numStack.pop() / num);
                }
                
                lastSymbol = c; // 记录symbol以便下次结算
                num = 0; // 重置
            }
        }
        
        int ans = 0;
        while (!numStack.isEmpty()) {
            ans += numStack.pop();
        }
        
        return ans;
    }
}
