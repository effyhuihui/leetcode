__author__ = 'effy'
'''
Given a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list.

For example,
Given 1->2->3->3->4->4->5, return 1->2->5.
Given 1->1->1->2->3, return 2->3.
'''
class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def deleteDuplicates(self, head):
        if not head:
            return head
        dummy = ListNode(0)
        dummy.next = head
        last_distinct = dummy
        current = head.next
        prev = head
        while current:
            if current.val == prev.val:
                while current and current.val == prev.val:
                    current = current.next
                last_distinct.next = current
                prev = current
                if current:
                    current = current.next
            else:
                last_distinct = prev
                prev = current
                current = current.next
        return dummy.next


class Solution_3rd:
    # @param head, a ListNode
    # @return a ListNode
    def deleteDuplicates(self, head):
        dummy = ListNode(-1000)
        dummy.next = head
        prev_non_dup = dummy
        prev = head
        while prev:
            isDup = False
            cur = prev.next
            while cur and  cur.val == prev.val:
                isDup = True
                cur = cur.next
            if not isDup:
                prev_non_dup.next = prev
                prev_non_dup = prev
                prev = cur
            else:
                prev = cur
        prev_non_dup.next = prev
        return dummy.next


a,b,c,d,e,f,g = ListNode(1), ListNode(1),ListNode(2),ListNode(2), ListNode(4),ListNode(4),ListNode(5)
a.next, = b,
x = Solution()
t = x.deleteDuplicates(a)
while t:
    print t.val
    t = t.next

