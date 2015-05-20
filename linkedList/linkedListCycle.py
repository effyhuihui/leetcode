__author__ = 'effy'
'''
Given a linked list, determine if it has a cycle in it.

Follow up:
Can you solve it without using extra space?

Thought:
Very typical and classic two pointers problem
'''

class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution:
    # @param head, a ListNode
    # @return a boolean
    def hasCycle(self, head):
        if not head or not head.next:
            return False
        slow = head
        fast = head.next
        while fast:
            if fast == slow:
                return True
            else:
                slow = slow.next
                fast = fast.next
                if fast:
                    fast = fast.next
        return False



class Solution_secondround:
    # @param head, a ListNode
    # @return a boolean
    def hasCycle(self, head):
        if head == None:
            return False
        slow, fast = head, head.next
        while fast:
            if slow == fast:
                return True
            slow = slow.next
            fast = fast.next
            if fast:
                fast = fast.next
        return False