class Solution {
    public boolean wordBreak(String s, List<String> wordDict) { // 73, 38
        // DP, wordBreakAtIndex[i] 
        boolean[] wordBreakAtIndex = new boolean[s.length() + 1];
        HashSet<String> dict = new HashSet<String>(wordDict);
        wordBreakAtIndex[0] = true;
        for (int end = 0; end <= s.length(); end++) {
            for (int start = 0; start < end; start++) {
                if (wordBreakAtIndex[start] == true && dict.contains(s.substring(start, end))) {
                    wordBreakAtIndex[end] = true;
                    break;
                }
            }
        }
        return wordBreakAtIndex[s.length()];
    }
}