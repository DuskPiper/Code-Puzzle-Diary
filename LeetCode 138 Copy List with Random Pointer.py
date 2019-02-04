# Definition for singly-linked list with a random pointer.
# class RandomListNode(object):
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None

class Solution(object): # 96% Time, 69% RAM
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        if not head: return None
        dic = {} # <RandomListNode, RandonListNode>
        ptr = head # iterator
        while ptr:
            dic[ptr] = RandomListNode(ptr.label) # 复制Node
            ptr = ptr.next
        ptr = head
        while ptr:
            ptr2 = dic.get(ptr)
            ptr2.next = dic.get(ptr.next) # 复制Next指针
            ptr2.random = dic.get(ptr.random) # 复制Random指针
            ptr = ptr.next
        return dic[head]
            