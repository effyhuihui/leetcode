__author__ = 'effy'
'''
Merge two sorted linked lists and return it as a new list. The new list should be made by
splicing together the nodes of the first two lists.
'''
class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution:
    # @param two ListNodes
    # @return a ListNode
    def mergeTwoLists(self, l1, l2):
        cur1 = l1
        cur2 = l2
        dummy = ListNode(0)
        cur = dummy
        while cur1 and cur2:
            if cur1.val <= cur2.val:
                cur.next = cur1
                cur1 = cur1.next
            else:
                cur.next = cur2
                cur2 = cur2.next
            cur = cur.next
        if cur1:
            cur.next = cur1
        if cur2:
            cur.next = cur2
        return dummy.next

