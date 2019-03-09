class Solution {
    public boolean isPalindrome(String s) { // 90, 80
        // s = s.replaceAll("\\W+", "").replaceAll(" ", "").toLowerCase();
        
        int lo = 0, hi = s.length() - 1;
        while (lo <= hi) {
            if (lo < s.length() && !Character.isLetterOrDigit(s.charAt(lo)))
                {lo++;continue;}
            if (hi >= 0 && !Character.isLetterOrDigit(s.charAt(hi)))
                {hi--;continue;}
            
            if (Character.toLowerCase(s.charAt(lo)) != Character.toLowerCase(s.charAt(hi)))
                return false;
            lo++;
            hi--;
        }
        return true;
    }
}