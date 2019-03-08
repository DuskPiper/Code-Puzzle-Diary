class Solution {
    public boolean canFinish(int numCourses, int[][] prerequisites) { // 80, 38
        // Build Graph
        Map<Integer, List<Integer>> neighbors = new HashMap<Integer, List<Integer>>();
        Queue<Integer> q = new LinkedList<Integer>();
        int[] inDegree = new int[numCourses]; // 入度表
        
        for (int[] pair : prerequisites) {
            inDegree[pair[0]]++;
            if (!neighbors.containsKey(pair[1]))
                neighbors.put(pair[1], new LinkedList<Integer>());
            neighbors.get(pair[1]).add(pair[0]);
        }
        
        for (int i = 0; i < numCourses; i++)
            if (inDegree[i] == 0)
                q.offer(i); // push into all nodes with 0 in-degree
        
        // Topological Sort
        int counter = 0;
        while (!q.isEmpty()) {
            int cur = q.poll();
            counter++;
            
            if (neighbors.containsKey(cur)) {
                for (Integer neighbor : neighbors.get(cur)) {
                    inDegree[neighbor]--;
                    if (inDegree[neighbor] == 0)
                        q.offer(neighbor);
                }
            }
        }
        
        return counter == numCourses; // 算法的核心：对于DAG，拓扑排序不含重复元素
    }
}