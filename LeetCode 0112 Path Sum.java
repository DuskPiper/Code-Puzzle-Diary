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
    public boolean hasPathSum(TreeNode root, int sum) { // 100, 11
        if (root == null)
            return false;
        return (root.val == sum && root.left == null && root.right == null) // at leaf
            || hasPathSum(root.left, sum - root.val) // trace left
            || hasPathSum(root.right, sum - root.val); // trace right
    }
}