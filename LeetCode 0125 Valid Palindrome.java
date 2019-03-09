class Solution {
    public boolean isPalindrome(String s) { // 27, 82
        s = s.replaceAll("\\W+", "").replaceAll(" ", "").toLowerCase();
        int lo = 0, hi = s.length() - 1;
        while (lo < hi) {
            if (s.charAt(lo) != s.charAt(hi))
                return false;
            lo++;
            hi--;
        }
        return true;
    }
}