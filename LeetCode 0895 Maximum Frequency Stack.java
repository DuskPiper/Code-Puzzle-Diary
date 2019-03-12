class FreqStack { // 80, 75
    Map<Integer, Integer> counter;
    Map<Integer, Stack<Integer>> freqStacks;
    int maxFreq;

    public FreqStack() {
        counter = new HashMap<Integer, Integer>(); // element -> its frequency
        freqStacks = new HashMap<Integer, Stack<Integer>>(); // frequency -> stack of elements at this freq or above
        maxFreq = 0;
    }
    
    public void push(int x) {
        int curFreq = 1 + counter.getOrDefault(x, 0);
        counter.put(x, curFreq);
        maxFreq = curFreq > maxFreq ? curFreq : maxFreq;
        if (!freqStacks.containsKey(curFreq)) 
            freqStacks.put(curFreq, new Stack<Integer>());
        freqStacks.get(curFreq).push(x);
    }
    
    public int pop() {
        int ans = freqStacks.get(maxFreq).pop();
        counter.put(ans, counter.get(ans) - 1);
        if (freqStacks.get(maxFreq).size() == 0)
            maxFreq -= 1;
        return ans;
    }
}

/**
 * Your FreqStack object will be instantiated and called as such:
 * FreqStack obj = new FreqStack();
 * obj.push(x);
 * int param_2 = obj.pop();
 */