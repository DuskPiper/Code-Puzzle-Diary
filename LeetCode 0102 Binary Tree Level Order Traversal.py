# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object): # 84%, 75%
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root: return []
        queue, ans = [root], []
        while queue:
            cur_layer = []
            level_size = len(queue)
            for _ in range(level_size):
                node = queue.pop(0)
                cur_layer.append(node.val)
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
            ans.append(cur_layer)
        return ans