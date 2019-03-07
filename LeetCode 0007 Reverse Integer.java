class Solution {
    public int reverse(int x) { // 99.99, 28
        int result = 0;
        int newResult;
        while (x != 0) {
            int tail = x % 10;
            newResult = result * 10 + tail;
            if ((newResult - tail) / 10 != result) // Java会自动处理溢出，比如正溢出变负，这样的话，得到的(溢出错误后的)结果无法回溯
                return 0; // 检测到无法回溯就说明溢出了
            result = newResult;
            x = x / 10;
        }
        return result;
    }
}