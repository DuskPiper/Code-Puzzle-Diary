import java.util.*;

public class KLengthLess {
    // Find substring with length=k, and includes k-1 distinct char

    public List<String> KSubstring(String input, int k) {
        Map<Character, Integer> occurrence = new HashMap<Character, Integer>();
        List<String> result = new ArrayList<String>();
        for (int left = 0; left + k <= input.length(); left ++) { // Check each substring whose len=k
            String str = input.substring(left, left + k);
            boolean isRepeated = false;

            for (char c : str.toCharArray()) { // Check char
                if occurrence.containsKey(c) { // Char c appearred already
                    if (!isRepeated) occurrence.put(c, occurrence.get(c) + 1); // First repeat
                    else break; // Not first repeat, meaning this substring is not target
                    isRepeated = true; // Set flag. KEY is that: we don't want this flag to be set true twice
                } else {
                    occurrence.put(c, 1);
                }
            }

            if (isRepeated && !result.contains(str)) result.add(str); // Flag = true, repeat happens and only happens once, target found, 去重添加
            occurrence.clear();
        }
        return result;
    }
}