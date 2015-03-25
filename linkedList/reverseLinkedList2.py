# -*- coding: utf-8 -*-
__author__ = 'effy'
'''
Reverse a linked list from position m to n. Do it in-place and in one-pass.

For example:
Given 1->2->3->4->5->NULL, m = 2 and n = 4,

return 1->4->3->2->5->NULL.

Note:
Given m, n satisfy the following condition:
1 ≤ m ≤ n ≤ length of list.
'''

class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution:
    # @param head, a ListNode
    # @param m, an integer
    # @param n, an integer
    # @return a ListNode
    def reverseBetween(self, head, m, n):
        dummy = ListNode(0)
        dummy.next = head
        ## find the node that is after the last node needed reverse and the one before reverse
        prev, end = dummy, dummy
        for i in range(m-1):
            prev = prev.next
        for i in range(n+1):
            end = end.next
        last = end
        current = prev.next
        ## break the linked list between prev to the next
        prev.next = None
        while current != end:
            next = current.next
            current.next = last
            last = current
            current = next
        prev.next = last
        return dummy.next



a,b,c,d,e = ListNode(1), ListNode(2),ListNode(3),ListNode(4), ListNode(5)
a.next,b.next,c.next,d.next = b,c,d,e
x = Solution()
t = x.reverseBetween(a, 1,1)
while a:
    print a.val
    a = a.next