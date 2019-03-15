public class Solution {
    public String reverseWords(String s) { // 57, 21
        StringBuffer ans = new StringBuffer();
        StringBuffer sb = new StringBuffer();
        for (int i = s.length() - 1; i >= 0; i--) {
            char c = s.charAt(i);
            if (c == ' ') {
                if (sb.length() == 0)
                    continue;
                else {
                    ans.append(sb.reverse().toString());
                    ans.append(" ");
                    sb.delete(0, sb.length());
                }
            } else {
                sb.append(c);
            }
        }
        if (sb.length() > 0) {
            ans.append(sb.reverse().toString());
            ans.append(" ");
        }
        if (ans.length() == 0)
            return "";
        return ans.substring(0, ans.length() - 1).toString();
    }
}