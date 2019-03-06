class Solution {
    public int[] dailyTemperatures(int[] T) { // 78, 48
        int[] ans = new int[T.length];
        Arrays.fill(ans, 0);
        Stack<Integer> stack = new Stack<Integer>(); // stack存储以往未确定答案的index，之后扫描往前挨个pop
        for (int i = 0; i < T.length; i++) {
            while (!stack.isEmpty() && T[stack.peek()] < T[i]) {
                int j = stack.pop();
                ans[j] = i - j;
            }
            stack.push(i); // 所有当前值显然都是不知道答案的，丢进stack等待解决
        }
        return ans;
    }
}