class Solution { // 7%
    public int countSubstrings(String s) {
        int counter = 0;
        int j; // substring radius
        int len = s.length();
        for (int i = 0; i < len; i ++) { // i is midpoint
            j = 0;
            // Now check odd-lengthed substring
            while (i - j >= 0 && i + j < len) {
                if (isPalindrom(s.substring(i - j, i + j + 1))) {
                    counter ++;
                    j ++;
                } else {
                    break;
                }
            }
            // Now check even-lengthed substring
            j = 0;
            while (i - j >= 0 && i + j + 1 < len) {
                if (isPalindrom(s.substring(i - j, i + j + 2))) {
                    counter ++;
                    j ++;
                } else {
                    break;
                }
            }
        }
        return counter;
    }
    
    private boolean isPalindrom(String s) { // check if a string is palindrom
        if (s.length() == 1) return true;
        StringBuilder sb = new StringBuilder(s);
        return sb.reverse().toString().equals(s);
    }
}