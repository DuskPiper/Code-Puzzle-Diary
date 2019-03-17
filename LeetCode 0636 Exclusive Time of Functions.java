class Solution {
    public int[] exclusiveTime(int n, List<String> logs) { // 94 53
        Stack<Integer> stack = new Stack<Integer>();
        int[] ans = new int[n];
        
        int lastTime = 0;
        for (String log : logs) {
            String[] status = log.split(":");
            int id = Integer.parseInt(status[0]);
            int time = Integer.parseInt(status[2]);
            if (status[1].equals("start")) { // start a recursion
                if (!stack.isEmpty())
                    ans[stack.peek()] += time - lastTime;
                stack.push(id);
                lastTime = time;
            } else { // end a recursion
                ans[stack.pop()] += time - lastTime + 1;
                lastTime = time + 1;
            }
        }
        return ans;
    }
}