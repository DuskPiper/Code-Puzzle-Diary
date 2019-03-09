class Solution {
    public List<List<String>> groupAnagrams(String[] strs) { // 87, 70
        List<List<String>> ans = new ArrayList<List<String>>();
        Map<Integer, List<String>> map = new HashMap<Integer, List<String>>(); // anagram feature value -> list of anagrams
        
        for (String s : strs) {
            int feature = feature(s);
            if (!map.containsKey(feature))
                map.put(feature, new LinkedList<String>());
            map.get(feature).add(s);
        }
        
        for (Map.Entry<Integer, List<String>> entry : map.entrySet())
            ans.add(entry.getValue());
        
        return ans;
    }
    
    private int feature(String s) { // find feature value for anagram
        char[] ca = s.toCharArray();
        Arrays.sort(ca); // important
        return Arrays.hashCode(ca); // another approach: String.valueOf(ca)
    }
}