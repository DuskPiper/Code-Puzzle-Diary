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
    public int pathSum(TreeNode root, int sum) { // 76, 8
        if (root == null)
            return 0;
        return pathSumStartAtNode(root, sum)
            + pathSum(root.left, sum)
            + pathSum(root.right, sum);
    }
    
    private int pathSumStartAtNode(TreeNode node, int sum) {
        if (node == null)
            return 0;
        return (node.val == sum ? 1 : 0) 
            + pathSumStartAtNode(node.left, sum - node.val) 
            + pathSumStartAtNode(node.right, sum - node.val);
    }
}