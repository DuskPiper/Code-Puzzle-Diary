# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object): # 88%, 81%
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        # 就是把普通的level traversal的答案倒着输出而已
        if not root: return []
        queue, ans = [root], []
        while queue:
            cur_level = []
            level_size = len(queue)
            for _ in range(level_size):
                node = queue.pop(0)
                cur_level.append(node.val)
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
            ans.append(cur_level)
        return ans[::-1]