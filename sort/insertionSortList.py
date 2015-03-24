# -*- coding= utf-8 -*-
__author__ = 'effy'
'''
Sort a linked list using insertion sort.
'''
class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None

'''
my way
'''
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
            if before_cur.val > cur.val:
                pre = dummy
                post = pre.next
                while post.val < cur.val:
                    post = post.next
                    pre = pre.next
                before_cur.next = cur.next
                cur.next = post
                pre.next = cur
                cur = before_cur.next
            else:
                before_cur = cur
                cur = cur.next
        return dummy.next


'''
will pass http://www.cnblogs.com/zuoyuan/p/3700105.html
'''
class Solution2:
# @param head, a ListNode
# @return a ListNode
    def insertionSortList(self, head):
        if not head:
            return head
        dummy = ListNode(0)                         #为链表加一个头节点
        dummy.next = head
        curr = head
        while curr.next:
            if curr.next.val < curr.val:            #如果链表是升序的，那么curr指针一直往后移动
                pre = dummy                         #直到一个节点的值小于前面节点的值
                while pre.next.val < curr.next.val: #然后寻找插入的位置
                    pre = pre.next
                tmp = curr.next                     #上面的示意图就是以下这段代码
                curr.next = tmp.next
                tmp.next = pre.next
                pre.next = tmp
            else:
                curr = curr.next
        return dummy.next

a = ListNode(1)
b = ListNode(2)
c = ListNode(3)
d = ListNode(4)
e = ListNode(5)
a.next = b
b.next = c
c.next = d
d.next = e
x = Solution()
t = x.insertionSortList(a)
while t:
    print t.val
    t = t.next

