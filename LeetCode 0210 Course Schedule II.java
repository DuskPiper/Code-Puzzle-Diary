class Solution {
    public int[] findOrder(int numCourses, int[][] prerequisites) { // 48, 20
        if (numCourses == 0) return new int[0];
        // make it a graph
        Map<Integer, HashSet<Integer>> nextCourses = new HashMap<Integer, HashSet<Integer>>(); // {课程：(课程的后续课程)}
        Map<Integer, HashSet<Integer>> preCourses = new HashMap<Integer, HashSet<Integer>>(); // {课程：(课程的前序课程(wishlist))}
        for (int[] prerequisite : prerequisites) {
            if (nextCourses.get(prerequisite[1]) == null) nextCourses.put(prerequisite[1], new HashSet<Integer>());
            nextCourses.get(prerequisite[1]).add(prerequisite[0]);
            if (preCourses.get(prerequisite[0]) == null) preCourses.put(prerequisite[0], new HashSet<Integer>());
            preCourses.get(prerequisite[0]).add(prerequisite[1]);
        }
        
        // BFS
        Queue<Integer> queue = new LinkedList<Integer>();
        for (int i = 0; i < numCourses; i++) // 过滤：将不需要前序课程的课程入队列，这些课程可以不在意顺序直接修
            if (!preCourses.containsKey(i)) 
                queue.offer(i);
        int[] ans = new int[numCourses];
        int counter = 0; // 用来填充答案的助手
        while (!queue.isEmpty()) { // bfs
            Integer curCourse = queue.poll();
            // Now take course
            ans[counter++] = curCourse;
            for (Integer nextCourse : nextCourses.getOrDefault(curCourse, new HashSet<Integer>())) { // 处理当前课程的后续课程，而非直接丢进队列
                preCourses.get(nextCourse).remove(curCourse); // 当前后续课程 的 前序课程(wishlist)中除去当前课程
                if (preCourses.get(nextCourse).size() == 0) // 如果前序课程(wishlist)为空了，就入队列；如果不为空就不管，总有一天会变空的
                    queue.offer(nextCourse);
            }
        }
        return counter == numCourses ? ans : new int[0];
    }
}