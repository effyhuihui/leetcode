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



'''
every time if see rotate, use pivot or circular list
rotate a LINKED LIST by kth:
1. link the head and end of current linked list to make it a circle
2. new head will be the (l-k)th element from the current list
3. break the circle return new head
'''
class Solution_secondround:
    # @param head, a ListNode
    # @param k, an integer
    # @return a ListNode

    def rotateRight(self, head, k):
        if head is None or k == 0:
            return head
        last_node = head
        l = 1
        while last_node.next:
            l += 1
            last_node = last_node.next
        steps = l- k%l
        if steps != 0:
            ### make linked list a circle
            last_node.next = head
            prev_new_head = head
            for i in range(steps-1):
                prev_new_head = prev_new_head.next
            new_head = prev_new_head.next
            prev_new_head.next = None
            return new_head
        else:
            return head


class Solution_3rd:
    # @param head, a ListNode
    # @param k, an integer
    # @return a ListNode

    def rotateRight(self, head, k):
        if not head or k ==0:
            return head
        l = 0
        cur = head
        while cur:
            l += 1
            cur = cur.next
        newk = k%l
        if newk == 0:
            return head
        slow,fast = head,head
        for i in range(newk):
            fast = fast.next
        while fast.next:
            slow = slow.next
            fast = fast.next
        newhead = slow.next
        slow.next = None
        fast.next = head
        return newhead
a,b,c,d,e = ListNode(1), ListNode(2), ListNode(3), ListNode(4), ListNode(5)
a.next, = b,
x = Solution()

t = x.rotateRight(a,3)
while t:
    print t.val
    t = t.next