# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object): # 99% Time, 60% RAM
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root: return []
        stack = [root] # 流水线，所有数据都要后进前出一遍
        ans = []
        reverser = -1 # 用来确定该行是否reverse的，1则不reverse，-1则reverse
        while stack: # 单次loop对应树的一层
            reverser = -reverser # 每层都改编一次reverser，达到zigzag效果
            curLayer = [] # 本层的答案
            for i in range(len(stack)): # 单次loop对应本层的单个数据，因为是BFS，顺序是本层左->右
                node = stack.pop(0) # for循环会把该层所有元素从前面pop完
                if node.left: stack.append(node.left) 
                if node.right: stack.append(node.right) # 先左后右丢下一层的node进stack尾部
                curLayer.append(node.val) # 记录答案进层答案
            ans.append(curLayer[::reverser]) # 根据reverse信息记录本层答案
        return ans