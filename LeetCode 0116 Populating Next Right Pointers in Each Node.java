/*
// Definition for a Node.
class Node {
    public int val;
    public Node left;
    public Node right;
    public Node next;

    public Node() {}

    public Node(int _val,Node _left,Node _right,Node _next) {
        val = _val;
        left = _left;
        right = _right;
        next = _next;
    }
};
*/
class Solution {
    public Node connect(Node root) { // 47, 72
        if (root == null) return root;
        List<Node> curLevel = new ArrayList<Node>();
        List<Node> nextLevel = new ArrayList<Node>();
        curLevel.add(root);
        
        while (curLevel.size() > 0) {
            for (int i = 0; i < curLevel.size(); i++) {
                Node cur = curLevel.get(i);
                if (i < curLevel.size() - 1)
                    cur.next = curLevel.get(i + 1);
                if (cur.left != null)
                    nextLevel.add(cur.left);
                if (cur.right != null)
                    nextLevel.add(cur.right);
            }
            curLevel = new ArrayList<Node>(nextLevel);
            nextLevel.clear();
        }
        return root; 
    }
}