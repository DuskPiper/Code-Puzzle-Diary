class Solution { // 99.9% Time, 11% RAM
    public void reverseString(char[] s) {
        char tmp;
        int i = 0, j = s.length - 1;
        while (i < j) {
            tmp = s[i];
            s[i] = s[j];
            s[j] = tmp;
            i ++;
            j --;
        }
    }
}