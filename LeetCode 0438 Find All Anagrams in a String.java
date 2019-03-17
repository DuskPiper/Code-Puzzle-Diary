class Solution {
    public List<Integer> findAnagrams(String s, String p) { // 17, 76
        List<Integer> ans = new LinkedList<Integer>();
        int pFeature = feature(p);
        int i = 0, j = p.length();
        while (j <= s.length()) {
            if (feature(s.substring(i, j)) == pFeature) {
                ans.add(i);
                while (j < s.length() && s.charAt(j) == s.charAt(i)) {
                    ans.add(++i);
                    j++;
                }   
            }
            i++; j++;
        }
        return ans;
    }
    
    private int feature(String s) {
        char[] sChar = s.toCharArray();
        Arrays.sort(sChar);
        return Arrays.hashCode(sChar);
    }
}