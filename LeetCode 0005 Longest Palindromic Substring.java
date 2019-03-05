class Solution {
    // Solution: Brute Force, O(n^2) worst
    public String longestPalindrome(String s) { // 99.5, 46
        if (s == null || s.length() == 0) return "";
        // Try Brute Force
        int len = s.length();
        String ans = "";
        for (int i = 0; i < len; i++) {
            // odd-lengthed palindrom
            ans = extendPalindrome(s, i, i, ans);
            
            // even-lengthed palindrom
            if (i < len - 1 && s.charAt(i) == s.charAt(i + 1))
                ans = extendPalindrome(s, i, i + 1, ans);
        }
        return ans;
    }
    
    private String extendPalindrome(String s, int start, int end, String oldAnswer) {
        while (start > 0 && end < s.length() - 1 && s.charAt(start - 1) == s.charAt(end + 1)) {
            start--;
            end++;
        }
        return end - start + 1 > oldAnswer.length() ? s.substring(start, end + 1) : oldAnswer;
    } 
}