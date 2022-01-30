# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def getDirections(self, root, startValue, destValue): # 68%, 43%
        """
        :type root: Optional[TreeNode]
        :type startValue: int
        :type destValue: int
        :rtype: str
        """
        def findPathToRoot(root, target): # return a string of steps from root to target
            if not root: # parent is leaf
                return None
            if root.val == target: # found target
                return ""
            
            leftPath = findPathToRoot(root.left, target) # found target in left subtree
            if not leftPath == None:
                return "L" + leftPath
            rightPath = findPathToRoot(root.right, target) # found target in right subtree
            if not rightPath == None:
                return "R" + rightPath
            
            return None
        
        pathRootToStart = findPathToRoot(root, startValue)
        pathRootToDest = findPathToRoot(root, destValue)
        
        while(pathRootToStart and pathRootToDest and pathRootToStart[0] == pathRootToDest[0]):
            pathRootToStart = pathRootToStart[1:]
            pathRootToDest = pathRootToDest[1:]
            
        return "U" * len(pathRootToStart) + pathRootToDest