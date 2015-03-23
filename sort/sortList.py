__author__ = 'effy'
'''
Sort a linked list in O(n log n) time using constant space complexity.

One take away from the problem is that: if you want to use fast runner technique for linked list
slow and fast should start differently!!!
'''
class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def sortList(self, head):
        ## by excluding the special cases. slow and fast should start differently
        if  head == None or head.next == None:
            return head
        slow, fast = head, head.next.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        mid = slow.next
        slow.next = None

        pre = self.sortList(head)
        post = self.sortList(mid)

        dummy_head = ListNode(0)
        cur = dummy_head
        while pre and post:
            if pre.val<=post.val:
                cur.next = pre
                pre = pre.next
            else:
                cur.next = post
                post = post.next
            cur = cur.next
        if pre:
            cur.next = pre
        if post:
            cur.next = post
        return dummy_head.next


a = ListNode(10)
b = ListNode(8)
c = ListNode(6)
d = ListNode(4)
e = ListNode(2)
f = ListNode(1)
a.next = b
b.next = c
c.next = d
d.next = e
e.next = f
x = Solution()
t = x.sortList(a)
while t:
    print t.val
    t = t.next