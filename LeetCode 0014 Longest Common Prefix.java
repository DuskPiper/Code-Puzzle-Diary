class Solution { // 30, 83
    public String longestCommonPrefix(String[] strs) {
        if (strs == null || strs.length == 0) return "";
        String pre = "";
        String check; // check是pre的下一步，check在大多数时候比pre长一位
        // check用以存储已确定能行的prefix，check则+1长度用以测试
        for (int i = 1; i <= strs[0].length(); i ++) {
            check = strs[0].substring(0, i);
            for (String string : strs) {
                if (string.indexOf(check) != 0) return pre;
            }
            pre = check; // 测试通过，check更新（长度+1）
        }
        return pre;
    }
}