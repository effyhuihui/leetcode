# -*- coding: utf-8 -*-
__author__ = 'effy'
'''
Given a singly linked list L: L0→L1→…→Ln-1→Ln,
reorder it to: L0→Ln→L1→Ln-1→L2→Ln-2→…

You must do this in-place without altering the nodes' values.

For example,
Given {1,2,3,4}, reorder it to {1,4,2,3}.
'''

class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution:
    # @param head, a ListNode
    # @return nothing
    def reorderList(self, head):
        if not head or not head.next:
            return
        slow ,fast = head, head.next
        while fast:
            fast = fast.next
            if fast:
                fast = fast.next
                slow = slow.next
            else:
                break
        ## slow is not the break point of the two sub lists
        sub_head = slow.next
        ## break the two lists
        slow.next = None
        ##reverse second sub list
        last = None
        cur = sub_head
        while cur:
            tmp = cur.next
            cur.next = last
            last = cur
            cur = tmp

        curA, curB = head, last
        while curA and curB:
            next_cur_B = curB.next
            curB.next = curA.next
            curA.next = curB
            curA = curB.next
            curB = next_cur_B



class Solution_secondround:
    # @param head, a ListNode
    # @return nothing
    def reorderList(self, head):
        if head == None or head.next == None:
            return
        def reverse(head):
            last = None
            cur = head
            while cur:
                next = cur.next
                cur.next = last
                last = cur
                cur = next
            return last
        slow, fast = head, head.next
        while fast.next:
            slow = slow.next
            fast = fast.next
            if fast.next:
                fast = fast.next
        ## now slow is the end ot first part,
        second_head = slow.next
        slow.next = None
        reversed_second_head = reverse(second_head)
        cur1, cur2 = head, reversed_second_head
        while cur2 and cur1:
            next_cur2 = cur2.next
            next_cur1 = cur1.next
            cur1.next = cur2
            cur2.next = next_cur1
            cur1 = next_cur1
            cur2 = next_cur2






x = Solution()
a,b,c,d,e = ListNode(1), ListNode(2), ListNode(3), ListNode(4), ListNode(5)
#a.next, b.next, c.next = b,c,d
y = x.reorderList(a)

while y:
    print y.val
    y = y.next

print "new"


