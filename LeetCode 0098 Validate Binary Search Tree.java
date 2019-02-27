/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
class Solution { // 100% Time, 42% RAM
    public boolean isValidBST(TreeNode root) {
        if (root == null) return true;
        return isValidRoot(root, Long.MAX_VALUE, Long.MIN_VALUE); // 用long避免corner case
    }
    
    private boolean isValidRoot(TreeNode node, long max, long min) { // helper
        if (node.val >= max || node.val <= min) return false; // 很重要，检查上下限，上下限会在调用递归时做调整
        if (node.left == null && node.right == null) return true; // 是叶子
        boolean leftValid = true, rightValid = true; // 用来记录两边子树是否validBST，函数结尾返回leftValid && rightValid
        if (node.left != null) { // 左子树
            if (node.left.val >= node.val) {
                return false;
            } else {
                leftValid = isValidRoot(node.left, node.val, min); // 递归看左子树是否valid，此处更新max值为当前node值，因为这是左子树必须小于的最小值
            }
        }
        if (node.right != null) { // 右子树
            if (node.right.val <= node.val) {
                return false;
            } else {
                rightValid = isValidRoot(node.right, max, node.val); // 递归右子树，同上
            }
        }
        return leftValid && rightValid; // 左右子树均valid则返回true
    }
}