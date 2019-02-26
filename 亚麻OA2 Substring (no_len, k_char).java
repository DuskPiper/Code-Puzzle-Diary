import java.util.*;

public class KCharNoLength {
	// Find substrings with k distinct char, no length limit
	List<String> KCharSubstring(String input, int k) {
		List<String> results = new ArrayList<String>();
		if (input == null || input.length() == 0 || k == 0 || k > input.length()) return result;

		int resultCount = 0;
		int len = input.length;
		int[] count = new int[26];

		for (int left = 0; left < len; left ++) { // Check all substring starting at l
			int distinctNum = 0;
			Arrays.fill(count, 0);
			int right = left;

			for (; right < n; right ++) { // Check specific substring starting at l and ending at r
				char c = input.charAt(right);
				if (count[c - 'a'] == 0) distinctNum ++; // First occur
				count[c - 'a'] ++; // Save occurrence

				if (distinctNum == k) { // k reached
					String result = input.substring(left, right + 1);
					if (!results.contains(result)) results.add(result); // 去重添加
				} else if (distinctNum > k) { // k exceeded, stop inner loop, look for next l
					break;
				}
			}
		}
		return results;
	}
}