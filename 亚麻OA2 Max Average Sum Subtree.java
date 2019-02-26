import java.util.*;

public class Solution {
    class Result { // 用来封装答案，便于在树的层级之间传值
        CategoryNode node;
        int sum;
        int size;

        public Result(CategoryNode node, int sum, int size) {
            this.node = node;
            this.size = size;
            this.sum = sum;
        }
    }

    private Result ans = null; // in-class global

    // METHOD SIGNATURE BEGINS
    public CategoryNode getMostPopularNode(CategoryNode rootCategory) {
        if (rootCategory == null) return null;
        Result rootResult = helper(rootCategory); // Result of root
        return this.ans.node; // Best result of all
    }
    // METHOD SIGNATURE ENDS

    public Result helper(CategoryNode root) {
        if (root == null) return new Result(null, 0 ,0); // Bottom of recursion

        int subNodesSum = 0;
        int subNodesSize = 0;
        for (CategoryNode subNode : root.subCategoryNode) { // Collect results from all children
            Result subNodeResult = helper(subNode); // Recursion into all children, BFS
            subNodesSize += subNodeResult.size;
            subNodesSum += subNodeResult.sum;
        }

        Result curResult = new Result(root, subNodesSum + root.value, subNodesSize + 1); // Result for this node
        if (this.ans == null || this.ans.sum * this.ans.size > curResult.sum * curResult.size) {
            if (curResult.size > 1) { // Leaves shall be excluded
                this.ans = curResult;
            }
        }
        return curResult;
    }
}