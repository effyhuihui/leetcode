__author__ = 'effy'
'''
Sort a linked list using insertion sort.
'''
class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def insertionSortList(self, head):
        dummy = ListNode(0)
        dummy.next = head
        if head == None or head.next == None:
            return head
        cur = head.next
        before_cur = head
        while cur:
            pre = dummy
            post = pre.next
            while post != cur:
                if post.val <= cur.val:
                    post = post.next
                    pre = pre.next
                else:
                    break
            if post == cur:
                cur = cur.next
                before_cur = before_cur.next
            else:
                before_cur.next = cur.next
                cur.next = post
                pre.next = cur
                cur = before_cur.next
        return dummy.next
a = ListNode(5)
b = ListNode(4)
c = ListNode(3)
d = ListNode(2)
e = ListNode(1)
a.next = b
b.next = c
c.next = d
d.next = e
x = Solution()
t = x.insertionSortList(a)
while t:
    print t.val
    t = t.next

