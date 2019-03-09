/*
// Definition for a Node.
class Node {
    public int val;
    public List<Node> neighbors;

    public Node() {}

    public Node(int _val,List<Node> _neighbors) {
        val = _val;
        neighbors = _neighbors;
    }
};
*/
class Solution {
    public Node cloneGraph(Node node) { // 93, 100
        if (node == null)
            return null;
        Node root = new Node(node.val, new ArrayList<Node>());
        Map<Integer, Node> map = new HashMap<Integer, Node>(); // val -> new Nodes
        Queue<Node> q = new LinkedList<Node>(); // BFS
        
        q.offer(node);
        map.put(root.val, root);
        while (!q.isEmpty()) {
            Node n = q.poll();
            for (Node neighbor : n.neighbors) {
                if (!map.containsKey(neighbor.val)) {
                    map.put(neighbor.val, new Node(neighbor.val, new ArrayList<Node>())); // create a new copy among neighbors
                    q.offer(neighbor);
                }
                map.get(n.val).neighbors.add(map.get(neighbor.val)); // add copied neighbor (from map) into current node's copy's neighbor list
            } 
        }
        return root;
    }
}