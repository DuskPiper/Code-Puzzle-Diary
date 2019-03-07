class Solution {
    public int myAtoi(String str) { // 97, 18
        // 1. Corner case
        if (str == null || str.equals(""))
            return 0;
        
        // 2. Remove(skip) " "
        int i = 0;
        while (i < str.length() && str.charAt(i) == ' ')
            i++;
        
        // 3. Read +/-
        int symbol = 1;
        if (i < str.length() && (str.charAt(i) == '+' || str.charAt(i) == '-')) {
            symbol = str.charAt(i) == '+' ? 1 : -1;
            i++;
        }
        
        // 4. Construct value
        int ans = 0;
        int downGradedMaxInt = Integer.MAX_VALUE / 10;
        int downGradedMaxIntRemain = Integer.MAX_VALUE % 10;
        while (i < str.length()) {
            // Get next digit, return if NaN
            int diff = str.charAt(i) - '0';
            if (diff > 9 || diff < 0)
                break;
            
            // Check overflow, return if overflow
            if (ans > downGradedMaxInt || ans == downGradedMaxInt && diff > downGradedMaxIntRemain) // overflow
                return symbol == 1 ? Integer.MAX_VALUE : Integer.MIN_VALUE;
            
            // Append new digit
            ans = ans * 10 + diff;
            i++;
        }
        return ans * symbol;
    }
}