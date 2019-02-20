# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object): # 100%, 68%
    def verticalOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        # 定义一个性质：index，左子节点的index是其根的index-1，右则+1。index相同则属同一列，同列按level排序，所以在外进行一个普通层序遍历
        if not root: return []
        queue = [root]
        columns = {} # index -> [node_values]
        indexes = {} # node -> node.index
        indexes[root] = 0
        while queue:
            level_size = len(queue)
            for _ in range(level_size):
                node = queue.pop(0)
                index = indexes[node]
                # put(index, node.val)
                if index not in columns: columns[index] = [node.val]
                else: columns[index].append(node.val)
                # push children and record their indexes
                if node.left: 
                    queue.append(node.left)
                    indexes[node.left] = index - 1
                if node.right:
                    queue.append(node.right)
                    indexes[node.right] = index + 1
        return [v for k, v in sorted(columns.items())]