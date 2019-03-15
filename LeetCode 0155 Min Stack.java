class MinStack { // 99, 67 
    Stack<Integer> stack;
    int min;

    /** initialize your data structure here. */
    public MinStack() {
        stack = new Stack<Integer>();
        min = Integer.MAX_VALUE;;
    }
    
    public void push(int x) {
        if (x <= min) { // 需要更新min
            stack.push(min); // 特殊操作，再次把老min进栈一次，因此老min在新min下面(当然重复的老min在更下面、它本身该在的位置)
            min = x;
        }
        stack.push(x); // 无论如何也记录新值
    }
    
    public void pop() {
        if (stack.pop() == min) // 这里已经完成常规pop了
            min = stack.pop(); // 检测到是pop了最小值，因为之前约定的结构，下一位不是常规值而是老min值，所以再pop一次
    }
    
    public int top() {
        return stack.peek();
    }
    
    public int getMin() {
        return min;
    }
}

/**
 * Your MinStack object will be instantiated and called as such:
 * MinStack obj = new MinStack();
 * obj.push(x);
 * obj.pop();
 * int param_3 = obj.top();
 * int param_4 = obj.getMin();
 */