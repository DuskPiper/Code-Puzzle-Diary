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
    public TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) { // 100, 14
        while ((root.val - p.val) * (root.val - q.val) > 0) { // while 2 nodes are on same side
            if (root.val < p.val)
                root = root.right;
            else
                root = root.left;
        } // breaks if two nodes are on difference sides or if one of nodes is cur root
        return root;
    }
}