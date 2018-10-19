class Solution {
    public String reverseVowels(String s) {
        int i = 0;
        int j = s.length() - 1;
        char k;
        boolean i_is_vowel = false;
        boolean j_is_vowel = false;
        StringBuilder sb = new StringBuilder(s);
        List<Character> vowels = Arrays.asList('a','e','i','o','u','A','E','I','O','U'); // 注意语法
        while (i < j) {
            i_is_vowel = vowels.contains(sb.charAt(i));
            j_is_vowel = vowels.contains(sb.charAt(j));
            if (i_is_vowel && j_is_vowel) {
                k = sb.charAt(i);
                sb.setCharAt(i, sb.charAt(j));
                sb.setCharAt(j, k);
                j--;
                i++;
            } else if (i_is_vowel) {
                j--;
            } else if (j_is_vowel) {
                i++;
            } else {
                j--;
                i++;
            }
        }
        return sb.toString();
    }
}