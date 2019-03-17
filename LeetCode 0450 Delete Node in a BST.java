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
    public TreeNode deleteNode(TreeNode root, int key) { // 98, 46
        if (root == null)
            return root;
        if (key < root.val)
            root.left = deleteNode(root.left, key);
        else if (key > root.val)
            root.right = deleteNode(root.right, key);
        else { // found node
            if (root.left == null)
                return root.right;
            if (root.right == null)
                return root.left;
            // target node has both left and right subtree
            TreeNode min = root.right;
            while (min.left != null)
                min = min.left;
            root.val = min.val;
            root.right = deleteNode(root.right, min.val);  
        }
        return root;
    }
}