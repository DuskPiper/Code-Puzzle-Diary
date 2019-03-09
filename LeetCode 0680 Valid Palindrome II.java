class Solution {
    public boolean validPalindrome(String s) { // 92, 55
        int l = -1, r = s.length();
        while (++l < --r) 
            if (s.charAt(l) != s.charAt(r))  // 仅此一次换位(删字)
                return isPalindromic(s, l, r+1) || isPalindromic(s, l-1, r);
        return true;
    }

    public boolean isPalindromic(String s, int l, int r) {
        while (++l < --r) 
            if (s.charAt(l) != s.charAt(r)) return false;
        return true;
    }   
}