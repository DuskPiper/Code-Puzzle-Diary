/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
class Solution {
    // Iteration 
    public boolean isSameTree(TreeNode p, TreeNode q) { // 100, 14
        if (p == null && q == null)
            return true;
        else if (p == null || q == null)
            return false;
        Queue<TreeNode> q1 = new LinkedList<TreeNode>();
        Queue<TreeNode> q2 = new LinkedList<TreeNode>();
        q1.offer(p);
        q2.offer(q);
        
        while (!q1.isEmpty() || !q2.isEmpty()) {
            TreeNode nodep = q1.poll();
            TreeNode nodeq = q2.poll();
            if (!compareNode(nodep, nodeq))
                return false;
            if (nodep.left != null) {
                q1.offer(nodep.left);
                q2.offer(nodeq.left);
            }
            if (nodep.right != null) {
                q1.offer(nodep.right);
                q2.offer(nodeq.right);
            }
        }
        return true;
    }
    
    public boolean compareNode(TreeNode a, TreeNode b) {
        if (a == null && b == null)
            return true;
        else if (a == null || b == null)
            return false;
        if (a.val != b.val)
            return false;
        if ((a.left != null) != (b.left != null))
            return false;
        if ((a.right != null) != (b.right != null))
            return false;
        return true;
    }
    
    //recursion
    public boolean isSameTree(TreeNode p, TreeNode q) { // 100, 19
        if (p == null && q == null)
            return true;
        if (p == null || q == null)
            return false;
        if (p.val != q.val)
            return false;
        if (!isSameTree(p.left, q.left) || !isSameTree(p.right, q.right))
            return false;
        return true;
    }
}