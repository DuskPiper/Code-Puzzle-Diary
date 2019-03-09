class Solution {
    public String mostCommonWord(String paragraph, String[] banned) { // 47, 20
        Set<String> banSet = new HashSet<String>(Arrays.asList(banned));
        Map<String, Integer> counter = new HashMap<String, Integer>();
        
        String[] words = paragraph.replaceAll("\\W+", " ").toLowerCase().split("\\s+"); // \\W+指一切标点数字，\\s+一个或多个空格
        for (String word : words)
            if (!banSet.contains(word))
                counter.put(word, 1 + counter.getOrDefault(word, 0));
        
        String ans = null;
        int freq = 0;
        for (Map.Entry<String, Integer> entry : counter.entrySet()) {
            if (entry.getValue() > freq) {
                freq = entry.getValue();
                ans = entry.getKey();
            }
        }
        return ans;
    }
}