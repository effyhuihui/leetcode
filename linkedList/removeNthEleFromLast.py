# -*- coding= utf-8 -*-
__author__ = 'effy'
'''
Given a linked list, remove the nth node from the end of list and return its head.

For example,

   Given linked list: 1->2->3->4->5, and n = 2.

   After removing the second node from the end, the linked list becomes 1->2->3->5.
Note:
Given n will always be valid.
Try to do this in one pass.
'''

class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None


class Solution:
    # @return a ListNode
    def removeNthFromEnd(self, head, n):
        dummy = ListNode(0)
        dummy.next = head
        slow, fast = dummy, dummy
        for i in range(n+1):
            fast = fast.next
        while fast:
            slow, fast = slow.next, fast.next
        slow.next = slow.next.next
        return dummy.next


class Solution_secondround:
    # @return a ListNode
    def removeNthFromEnd(self, head, n):
        dummy = ListNode(0)
        dummy.next = head
        prevNthFromLast, last = dummy, dummy
        for i in range(n):
            last = last.next
        while last.next:
            last = last.next
            prevNthFromLast = prevNthFromLast.next
        prevNthFromLast.next = prevNthFromLast.next.next
        return dummy.next