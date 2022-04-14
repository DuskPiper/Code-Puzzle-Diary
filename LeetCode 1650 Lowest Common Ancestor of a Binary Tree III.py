"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution(object): # 99 55
    def lowestCommonAncestor(self, p, q):
        """
        :type node: Node
        :rtype: Node
        """
        pHistory = set([p.val])
        qHistory = set([q.val])
        while p.parent or q.parent:
            if p.parent:
                p = p.parent
                if p.val in qHistory:
                    return p
                pHistory.add(p.val)
            if q.parent:
                q = q.parent
                if q.val in pHistory:
                    return q
                qHistory.add(q.val)
        return p