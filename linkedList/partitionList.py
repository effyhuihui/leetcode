# -*- coding: utf-8 -*-
__author__ = 'effy'
'''
Given a linked list and a value x, partition it such that all nodes less than x come before nodes greater
than or equal to x.

You should preserve the original relative order of the nodes in each of the two partitions.
Assume that there is only one node with partition value
For example,
    Given 1->4->3->2->5->2 and x = 3,
    return 1->2->2->4->3->5.


解题思路：解决链表问题时，最好加一个头结点，问题会比较好解决。对这道题来说，创建两个头结点head1和head2，
head1这条链表是小于x值的节点的链表，head2链表是大于等于x值的节点的链表，然后将head2链表链接到head链表的尾部即可。
'''
class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution:
    # @param head, a ListNode
    # @param x, an integer
    # @return a ListNode
    def partition(self, head, x):
        small_head = ListNode(0)
        equal_or_larger_head = ListNode(0)
        cur_small,cur_equal_or_larger= small_head,equal_or_larger_head,
        if not head:
            return head
        cur = head
        while cur:
            if cur.val < x:
                cur_small.next = cur
                cur_small = cur
                cur = cur.next
                ## have to set to None!! otherwise the small list and larger list will be infinite
                cur_small.next = None
            else:
                cur_equal_or_larger.next = cur
                cur_equal_or_larger = cur
                cur = cur.next
                cur_equal_or_larger.next = None
        cur_small.next = equal_or_larger_head.next
        return small_head.next


a = ListNode(2)
b = ListNode(1)
a.next = b
x = Solution()
r = x.partition(a,1)
