__author__ = 'effy'

class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution_secondround:
    # @param {ListNode} head
    # @param {integer} val
    # @return {ListNode}
    def removeElements(self, head, val):
        dummy = ListNode(0)
        dummy.next = head
        prev, cur = dummy,head
        while cur:
            if cur.val == val:
                prev.next = cur.next
            else:
                prev = cur
            cur = cur.next
        return dummy.next