class Solution { // 100, 13
    public boolean isValid(String s) {
        Stack<Character> stack = new Stack<Character>();
        for (char c : s.toCharArray()) {
            if (c == '(') stack.push(')');
            else if (c == '[') stack.push(']');
            else if (c == '{') stack.push('}');
            else {
                if (stack.isEmpty() || stack.pop() != c) // 多了后括号，或，后括号存在内层未闭合[(])
                    return false;
            }
        }
        return stack.isEmpty();
    }
} 