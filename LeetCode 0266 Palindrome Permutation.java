class Solution {
    public boolean canPermutePalindrome(String s) { // 100, 5
        final Map<Character, Integer> counter = new HashMap<>();
        for (int i = 0; i < s.length(); i ++) {
            final Character c = s.charAt(i);
            counter.put(c, counter.getOrDefault(c, 0) + 1);    
        }
        int oddCounter = 0;
        for (final Integer count : counter.values()) {
            oddCounter += count % 2;
            if (oddCounter > 1) {
                return false;
            }
        }
        return true;
    }
}
