class Solution {
    public List<String> generateParenthesis(int n) { // 16, 99
        // DP,g(n)和g(n-1)的关系是，g(n)在g(n-1)的所有可能答案中的任意位置插入一对括号
        List<String> ans = new ArrayList<String>();
        if (n == 0) return ans;
        if (n == 1) {
            ans.add("()");
            return ans;
        }
        
        Set<String> ansSet = new HashSet<String>(); // 用set去重
        for (String s : generateParenthesis(n - 1)) {
            for (int i = 0; i < s.length(); i ++)
                ansSet.add(s.substring(0, i) + "()" + s.substring(i, s.length()));
        }
        ans.addAll(ansSet);
        return ans;
    }
}