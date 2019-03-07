class MyStack { // 84, 48
    Queue<Integer> q;

    /** Initialize your data structure here. */
    public MyStack() {
        q = new LinkedList<Integer>(); 
    }
    
    /** Push element x onto stack. */
    public void push(int x) {
        q.offer(x);
        for (int i = 1; i < q.size(); i++)
            q.offer(q.poll());
    }
    
    /** Removes the element on top of the stack and returns that element. */
    public int pop() {
        return q.poll();
    }
    
    /** Get the top element. */
    public int top() {
        return q.peek();
    }
    
    /** Returns whether the stack is empty. */
    public boolean empty() {
        return q.isEmpty();
    }
}