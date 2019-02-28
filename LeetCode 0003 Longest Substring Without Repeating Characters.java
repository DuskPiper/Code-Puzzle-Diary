class Solution { // 85, 9
    // 动态规划算法  启发自LeetCode 53 Maximum Subarray
    public int lengthOfLongestSubstring(String s) {
        if (s == null) return 0;
        Map<Character, Integer> lastAppear = new HashMap<Character, Integer>(); // 字符上次出现的地方
        int start = 0; // 子串开始的地方
        int ans = 0; 
        for (int i = 0; i < s.length(); i ++) { // i是子串结束的地方
            char c = s.charAt(i); // 新子串字符（上一个循环结尾的合法子串下一位字符
            if (lastAppear.containsKey(c) && lastAppear.get(c) >= start) { // 新字符有重复，其加入会让子串不合法
                start = lastAppear.get(c) + 1; // 截取子串后面部分，保证新子串合法性，不过子串一定不会变长、且大概率变短
            } else {
                ans = ans >= (i - start + 1) ? ans : i - start + 1; // 新字符在老子串中无重复，子串增补一位，len+1，记录答案
            }
            lastAppear.put(c, i); // 记录本字符上次出现地址
        }
        return ans;
    }
}