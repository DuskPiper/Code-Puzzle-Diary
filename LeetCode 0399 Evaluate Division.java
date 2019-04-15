class Solution {
    public double[] calcEquation(String[][] equations, double[] values, String[][] queries) { // 97, 86
        /*build graph*/
        Map<String, List<String>> neighbors = new HashMap<>();
        Map<String, Double> weights = new HashMap<>(); // String Key <= Strings[0] + Strings[1]
        for (int i = 0; i < equations.length; i++) {
            if (!neighbors.containsKey(equations[i][0])) // graph a -> b
                neighbors.put(equations[i][0], new LinkedList<String>());
            neighbors.get(equations[i][0]).add(equations[i][1]);
            weights.put(equations[i][0] + equations[i][1], values[i]);
            
            if (!neighbors.containsKey(equations[i][1])) // graph b -> a
                neighbors.put(equations[i][1], new LinkedList<String>());
            neighbors.get(equations[i][1]).add(equations[i][0]);
            weights.put(equations[i][1] + equations[i][0], 1.0 / values[i]);
        }
        
        /*graph traverse*/
        double[] ans = new double[queries.length];
        for (int i = 0; i < queries.length; i++) {
            String[] query = queries[i];
            if (!neighbors.containsKey(query[0])) { // vertice not registered
                ans[i] = -1.0;
                continue;
            }
            ans[i] = dfs(queries[i][0], queries[i][1], neighbors, weights, new HashSet<String>()); // dfs
        }
        
        return ans;
    }
    
    private double dfs(String cur, String tar, Map<String, List<String>> neighbors, Map<String, Double> weights, Set<String> visited) {
        if (cur.equals(tar)) 
            return 1.0; // found ans
        visited.add(cur);
        for (String neighbor : neighbors.getOrDefault(cur, new LinkedList<String>())) {
            if (!visited.contains(neighbor)) {
                //System.out.print(cur + "->" + neighbor + ": ");
                double curAns = dfs(neighbor, tar, neighbors, weights, visited);
                if (curAns >= 0) 
                    return curAns * weights.get(cur + neighbor); // found ans in sub-recursion   
            }
        }
        return -1.0; // not found ans in any sub-recursion
    }
}