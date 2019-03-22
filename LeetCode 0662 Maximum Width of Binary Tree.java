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
    public int widthOfBinaryTree(TreeNode root) { // 99, 33
        return dfs(root, 0, 0, new ArrayList<Integer>(), new ArrayList<Integer>());
    }
    
    private int dfs(TreeNode node, int curLevel, int index, ArrayList<Integer> leftmostAtLevel, ArrayList<Integer> rightmostAtLevel) {
        if (node == null)
            return 0;
        if (curLevel == leftmostAtLevel.size()) { // 新一层，新建
            leftmostAtLevel.add(index); // dfs到新一层一定是最左边的，这个值不动了
            rightmostAtLevel.add(index); // dfs最后才记录到实际的(最右的)值，所以之后一定每次都更新
        } else  { // not new to a level, index must be > rightmostAtLevel[curLevel]
            rightmostAtLevel.set(curLevel, index); // 更新最右 
        }
        int curDiff = rightmostAtLevel.get(curLevel) - leftmostAtLevel.get(curLevel) + 1; // 本层目前为止的距离，实际上要最后一次访问本层(访问最右node时)才是最大答案
        int leftDiff = dfs(node.left, curLevel + 1, index * 2 + 1, leftmostAtLevel, rightmostAtLevel); // dfs left
        int rightDiff = dfs(node.right, curLevel + 1, index * 2 + 2, leftmostAtLevel, rightmostAtLevel); //dfs right
        return Math.max(curDiff, Math.max(leftDiff, rightDiff));
    }
}