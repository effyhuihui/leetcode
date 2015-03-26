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
    def reorderList_my_own(self, head):
        '''
        :param head: 1,2,3,4,5
        :into 1,3,5
               4,2
        :return 1,4,3,2,5
        '''
        if not head or not head.next:
            return head
        slow, fast = head, head.next
        last = None
        while slow and fast:
            slow.next = fast.next
            slow = slow.next
            fast.next = last
            last = fast
            if slow:
                fast = slow.next
        cur_old, cur_new = head, last
        while cur_new and cur_old:
            tmp = cur_old.next
            cur_old.next = cur_new
            next_cur_new = cur_new.next
            cur_new.next = tmp
            cur_old = tmp
            cur_new = next_cur_new
        return  head

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

x = Solution()
a,b,c,d,e = ListNode(1), ListNode(2), ListNode(3), ListNode(4), ListNode(5)
#a.next, b.next, c.next = b,c,d
y = x.reorderList(a)

while y:
    print y.val
    y = y.next

print "new"


