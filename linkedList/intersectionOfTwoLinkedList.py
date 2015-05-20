# -*- coding: utf-8 -*-
__author__ = 'effy'
'''
For example, the following two linked lists:

A:          a1 → a2
                   ↘
                     c1 → c2 → c3
                   ↗
B:     b1 → b2 → b3
begin to intersect at node c1.


Notes:

If the two linked lists have no intersection at all, return null.
The linked lists must retain their original structure after the function returns.
You may assume there are no cycles anywhere in the entire linked structure.
Your code should preferably run in O(n) time and use only O(1) memory.


'''
'''
use a HASH TABLE and store all node in list A, and then look up each node in list B
can be done, but memory limit exceeded
time: O(M+N) memory: O(M) dict
'''
class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution:
    # @param two ListNodes
    # @return the intersected ListNode
    def getIntersectionNode(self, headA, headB):
        lookup = {}
        endA = headA
        while endA:
            lookup[endA] = True
            endA = endA.next
        endB = headB
        while endB:
            if lookup.get(endB, False):
                return endB
            endB = endB.next
        return None


'''
use two Array as storage time: O(M+N), mem O(m)+O(n) list
pass
'''
class Solution2:
    # @param two ListNodes
    # @return the intersected ListNode
    def getIntersectionNode(self, headA, headB):
        listA = []
        listB = []
        if headA == None or headB == None:# 判断输入表是否为空
            return None
        endA, endB = headA, headB
        while endA:#链表赋值到list中，方便从后面比较
            listA.append(endA)
            endA = endA.next
        while endB:
            listB.append(endB)
            endB = endB.next

        if endA != endB:
            return None

        intersect = endA
        while listA and listB:
            endA = listA.pop()
            endB = listB.pop()
            if endA != endB:
                return intersect
            else:
                intersect = endA
        return intersect

'''
Two pointer solution (O(n+m) running time, O(1) memory):

Maintain two pointers pA and pB initialized at the head of A and B, respectively.
Then let them both traverse through the lists, one node at a time.
When pA reaches the end of a list, then redirect it to the head of B (yes, B, that's right.);
similarly when pB reaches the end of a list, redirect it the head of A.
If at any point pA meets pB, then pA/pB is the intersection node.

To see why the above trick would work, consider the following two lists:
A = {1,3,5,7,9,11} and B = {2,4,9,11}, which are intersected at node '9'.
Since B.length (=4) < A.length (=6), pB would reach the end of the merged list first,
because pB traverses exactly 2 nodes less than pA does. By redirecting pB to head A, and pA to head B,
we now ask pB to travel exactly 2 more nodes than pA would. So in the second iteration, they are guaranteed
to reach the intersection node at the same time.

If two lists have intersection, then their last nodes must be the same one.
So when pA/pB reaches the end of a list, record the last element of A/B respectively.
If the two last elements are not the same one, then the two lists have no intersections.
'''
class Solution3:
    def getIntersectionNode(self, headA, headB):
        curA, curB = headA, headB
        endA, endB = None,None
        if not headA or not headB:
            return None
        while curA != curB:
            if curA.next:
                curA = curA.next
            else:
                endA = curA
                curA = headB
            if curB.next:
                curB = curB.next
            else:
                endB = curB
                curB = headA
            if endA and endB and endA != endB:
                return None
        return curA




headA = ListNode(1)
headB = ListNode(2)
headA.next = headB
x = Solution()
new =x.getIntersectionNode(headA, headB)
print new.val



class Solution_secondround:
    def getIntersectionNode(self, headA, headB):
        if headA == None or headB == None:
            return None
        endB = headB
        while endB.next:
            endB = endB.next
        ## link endB to headA
        endB.next = headA
        slow, fast = headB, headB.next
        hasIntersect = False
        while fast:
            if slow == fast:
                hasIntersect = True
                break
            slow = slow.next
            fast = fast.next
            if fast:
                fast = fast.next
        if not hasIntersect:
            endB.next = None
            return None
        else:
            fast = fast.next
            start = headB
            while fast!= start:
                fast = fast.next
                start = start.next
            endB.next = None
            return start






















