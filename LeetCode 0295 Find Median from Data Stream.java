class MedianFinder { // 100, 100
    PriorityQueue<Integer> low;
    PriorityQueue<Integer> high;

    /** initialize your data structure here. */
    public MedianFinder() {
        low = new PriorityQueue<Integer>((n1, n2) -> n2 - n1); // <=中位数的数
        high = new PriorityQueue<Integer>(); // >=中位数的数
    }
    
    public void addNum(int num) {
        if (low.isEmpty() || num <= low.peek()) low.offer(num);
        else high.offer(num);
        if (low.size() - high.size() > 1) high.offer(low.poll()); // 平衡大小，保证两边数量相等
        if (high.size() - low.size() > 1) low.offer(high.poll());
    }
    
    public double findMedian() {
        if (low.size() + high.size() == 0) return 0.0; // 全空
        else if ((low.size() + high.size()) % 2 == 0) return (double)((low.peek() + high.peek()) / 2.0); // 偶数项（则两queue大小相等
        else return (double)(low.size() > high.size() ? low.peek() : high.peek()); // 奇数项（则大的那一个queue的peek是中位数
    }
}