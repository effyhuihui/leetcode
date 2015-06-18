__author__ = 'effy'
'''
You are given two linked lists representing two non-negative numbers.
The digits are stored in reverse order and each of their nodes contain a single digit.
Add the two numbers and return it as a linked list.

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
'''

class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution:
    # @return a ListNode
    def addTwoNumbers(self, l1, l2):
        if l1 == None: return l2
        if l2 == None: return l1
        flag = 0
        dummy = ListNode(0)
        p = dummy
        while l1 and l2:
            p.next = ListNode((l1.val+l2.val+flag) % 10)
            flag = (l1.val+l2.val+flag) // 10
            l1 = l1.next
            l2 = l2.next
            p = p.next
        if l2:
            while l2:
                p.next = ListNode((l2.val+flag) % 10)
                flag = (l2.val+flag) / 10
                l2 = l2.next; p = p.next
        if l1:
            while l1:
                p.next = ListNode((l1.val+flag) % 10)
                flag = (l1.val+flag) / 10
                l1 = l1.next; p = p.next
        if flag == 1: p.next = ListNode(1)
        return dummy.next



class Solution:
    # @param {ListNode} l1
    # @param {ListNode} l2
    # @return {ListNode}
    def addTwoNumbers(self, l1, l2):
        dummy = ListNode(0)
        addOne = 0
        cur1,cur2 = l1, l2
        curnew = dummy
        while cur1 and cur2:
            total = cur2.val+cur1.val+addOne
            addOne = total/10
            curnew.next = ListNode(total%10)
            curnew = curnew.next
            cur1 = cur1.next
            cur2 = cur2.next
        cur_remain = None
        if cur1:
            cur_remain = cur1
        if cur2:
            cur_remain = cur2
        while cur_remain:
            total = cur_remain.val+addOne
            curnew.next = ListNode(total%10)
            addOne = total//10
            curnew = curnew.next
            cur_remain=cur_remain.next
        if addOne:
            curnew.next = ListNode(1)
        return dummy.next