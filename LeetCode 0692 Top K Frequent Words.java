class Solution {
    // 54, 67
    // 用HashMap作计数器，再把结果按entry过PriorityQueue
    public List<String> topKFrequent(String[] words, int k) {
        Map<String, Integer> counter = new HashMap<String, Integer>();
        for (String word : words) { // 计数
            counter.put(word, counter.getOrDefault(word, 0) + 1);
        }
        
        PriorityQueue<Map.Entry<String, Integer>> pq = new PriorityQueue<Map.Entry<String, Integer>>(
            (a,b) -> a.getValue() == b.getValue() ? b.getKey().compareTo(a.getKey()) : a.getValue() - b.getValue() // 频数高则先，相等则String小在先
        );
        for (Map.Entry<String, Integer> entry : counter.entrySet()) { // 统计Value最高的k个
            pq.offer(entry);
            if (pq.size() > k) pq.poll();
        }
        
        List<String> res = new LinkedList<String>(); // 转成结果
        while (!pq.isEmpty()) {
            System.out.println(pq.peek().getValue());
            res.add(0, pq.poll().getKey()); // 注意add 0，因为pq先出小的
        }
        return res;
    }
}