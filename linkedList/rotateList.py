# -*- coding: utf-8 -*-
__author__ = 'effy'
'''
Given a list, rotate the list to the right by k places, where k is non-negative.

For example:
Given 1->2->3->4->5->NULL and k = 2,
return 4->5->1->2->3->NULL.

Given 1->2->3->4->5->NULL and k = 3,
return 3->4->5->1->2-> NULL

Given 1->2->3->4->5->NULL and k = 4,
return 2->3->4->5->1->NULL

k=5 remain the same
Thoughts:

其实就是把整个list一起往右移动k个，所以最后的len(list)-k-1个nodes就只好放到最前面了
所以只要找到最后一个可以移动的node(new last node)，原先的最后一个node(old last
node)，以及要变到head的最后几个node的第一个(new head)， 然后把new last.next = None

old last.next = head
再返回new head就好了
'''
class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution:
    # @param head, a ListNode
    # @param k, an integer
    # @return a ListNode
    def rotateRight(self, head, k):
        if head == None or head.next == None or k == 0:
            return head
        ## temp will be the node of the new end node
        cur, temp, oldEnd = head, head, head
        l = 0
        while cur:
            oldEnd = cur
            cur = cur.next
            l += 1
        steps = k%l
        if steps:
            for i in range(l-steps-1):
                ##if k > length of the list, redirect to head and continue
                temp = temp.next
            newEnd = temp
            newHead = newEnd.next
            newEnd.next = None
            oldEnd.next = head
            return newHead
        else:
            return head
a,b,c,d,e = ListNode(1), ListNode(2), ListNode(3), ListNode(4), ListNode(5)
a.next, = b,
x = Solution()

t = x.rotateRight(a,3)
while t:
    print t.val
    t = t.next