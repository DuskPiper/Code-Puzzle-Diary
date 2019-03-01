/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
class Solution { // 100, 8
    // 中序遍历的结果是BST元素的自然排序，因此中序遍历k次即可
    public int kthSmallest(TreeNode root, int k) {
        // Inorder traversal with counter
        Stack<TreeNode> stack = new Stack<TreeNode>();
        int counter = 0;
        TreeNode ptr = root;
        while (!stack.isEmpty() || ptr != null) {
            while (ptr != null) {
                stack.push(ptr);
                ptr = ptr.left;
            }
            ptr = stack.pop();
            if (++ counter == k) return ptr.val;
            ptr = ptr.right;
        }
        return -1;
    }
}