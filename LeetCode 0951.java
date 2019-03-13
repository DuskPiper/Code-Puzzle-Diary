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
    public boolean flipEquiv(TreeNode root1, TreeNode root2) { // 100, 21
        // recursion
        if (root1 == null || root2 == null) // if any leaf's child
            return root1 == root2; // true only if both null
        if (root1.val != root2.val)
            return false;
        return (flipEquiv(root1.left, root2.left) && flipEquiv(root1.right, root2.right))  // not flip this time
            || (flipEquiv(root1.left, root2.right) && flipEquiv(root1.right, root2.left)); // flip this time
    }
}