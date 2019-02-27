class LRUCache { // 5%
    private HashMap<Integer, Integer> s;
    private LinkedList<Integer> l;
    private int cap;

    public LRUCache(int capacity) {
        this.s = new HashMap<Integer, Integer>(); // 存放数据键值对
        this.l = new LinkedList<Integer>(); // 存放数据键最近调用次序
        this.cap = capacity; // 额定容量
    }
    
    public int get(int key) {
        int ans = this.s.getOrDefault(key, -1); // 获取结果，没有则-1
        if (ans >= 0) { // 如果访问键存在，则更新最近调用
            this.l.removeFirstOccurrence(key); // 删除原本的
            this.l.addFirst(key); // 创建最新的在最前面
        }
        return ans;
    }
    
    public void put(int key, int value) {
        this.s.put(key, value); // 存放或者更新结果
        this.l.removeFirstOccurrence(key); // 更新最近调用
        this.l.addFirst(key);
        if (this.l.size() > this.cap) { // 检查是否溢出，是则删除l最后一项(LRU)
            this.s.remove(this.l.pollLast());
        }
    }
}