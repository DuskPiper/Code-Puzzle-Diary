class Solution {
    public boolean isAnagram(String s, String t) { // 89, 70
        int[] counter = new int[26];
        for (char c : s.toCharArray())
            counter[c - 'a']++;
        for (char c : t.toCharArray())
            counter[c - 'a']--;
        for (int count : counter)
            if (count != 0)
                return false;
        return true;
    }
}