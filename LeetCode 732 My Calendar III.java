class MyCalendarThree { // 4%
    // 该题中我们并不在乎book开始和结束的配对关系，只关心有效节点的book增减状况
    TreeMap<Integer, Integer> books; // 存储所有book，格式为<时间点，book增加量>

    public MyCalendarThree() {
        this.books = new TreeMap<Integer, Integer>();
    }
    
    public int book(int start, int end) {
        int k = 0; // 当前节点book数目
        int maxK = 0; // 最大book数目
        this.books.put(start, this.books.getOrDefault(start, 0) + 1); // 开始节点的book增加数目 +1
        this.books.put(end, this.books.getOrDefault(end, 0) - 1); // 结束节点的book增加数目 -1
        Set<Integer> keys = this.books.navigableKeySet();
        for (Integer actionTime : keys) { // 按时间顺序遍历时间节点
            k += this.books.get(actionTime); // 计算当前节点book值
            if (k > maxK) maxK = k; // 更新最大值
        }
        return maxK;
    }
}

/**
 * Your MyCalendarThree object will be instantiated and called as such:
 * MyCalendarThree obj = new MyCalendarThree();
 * int param_1 = obj.book(start,end);
 */