__author__ = 'effy'
'''
Given a linked list, return the node where the cycle begins. If there is no cycle, return null.

Follow up:
Can you solve it without using extra space?
'''

class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution:
    # @param head, a ListNode
    # @return a list node
    def detectCycle(self, head):
        if not head or not head.next:
            return None
        slow = head
        fast = head.next
        dummy = ListNode(0)
        dummy.next = head
        while fast:
            if slow == fast:
                ## if there is a loop, slow will always loop inside
                start = dummy
                while start != slow:
                    start = start.next
                    slow = slow.next
                return slow
            else:
                slow = slow.next
                fast = fast.next
                if fast:
                    fast = fast.next
                else:
                    return None
        return None