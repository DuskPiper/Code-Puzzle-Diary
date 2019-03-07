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
    public List<List<Integer>> verticalOrder(TreeNode root) { // 94, 78
        if (root == null)
            return new LinkedList<List<Integer>>();
        
        Queue<TreeNode> q = new LinkedList<TreeNode>(); // 层序遍历需要的queue
        List<List<Integer>> ans = new LinkedList<List<Integer>>(); // 运算结果
        Map<TreeNode, Integer> nodeOffsets = new HashMap<TreeNode, Integer>(); // Node对应的offset值
        Map<Integer, List<Integer>> offsetVal = new HashMap<Integer, List<Integer>>(); // offset值对应的所有node值，按entry转换成答案
        int minKey = 0;
        
        nodeOffsets.put(root, 0);
        q.offer(root);
        while (!q.isEmpty()) {
            TreeNode node = q.poll();
            int nodeOffset = nodeOffsets.get(node);
            
            if (!offsetVal.containsKey(nodeOffset))
                offsetVal.put(nodeOffset, new LinkedList<Integer>());
            offsetVal.get(nodeOffset).add(node.val);
            
            if (node.left != null) {
                q.offer(node.left);
                nodeOffsets.put(node.left, nodeOffset - 1);
                if (nodeOffset - 1 < minKey)
                    minKey = nodeOffset - 1;
            }
            if (node.right != null) {
                q.offer(node.right);
                nodeOffsets.put(node.right, nodeOffset + 1);
            }
        }
        
        while (offsetVal.containsKey(minKey)) {
            ans.add(offsetVal.get(minKey));
            minKey++;
        }
        
        return ans;
    }
}