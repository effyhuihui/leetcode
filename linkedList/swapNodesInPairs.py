__author__ = 'effy'
'''
Given a linked list, swap every two adjacent nodes and return its head.

For example,
Given 1->2->3->4, you should return the list as 2->1->4->3.

Your algorithm should use only constant space.
You may not modify the values in the list, only nodes itself can be changed.
'''

class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution:
    # @param a ListNode
    # @return a ListNode
    def swapPairs(self, head):
        if not head or not head.next:
            return head
        left = head
        right = head.next
        dummy = ListNode(0)
        dummy.next = head
        pre_pair = dummy
        while left and right:
            ## swap
            pre_pair.next = right
            left.next = right.next
            right.next =left
            ## advance to next pair
            pre_pair = left
            left = left.next
            if left:
                right = left.next
            else:
                break
        return dummy.next


class Solution_secondround:
    # @param a ListNode
    # @return a ListNode
    def swapPairs(self, head):
        if head == None:
            return head
        dummy = ListNode(0)
        dummy.next = head
        prev_last = dummy
        left,right = head,head.next
        while right:
            next = right.next
            prev_last.next = right
            right.next = left
            left.next = next
            prev_last = left
            left = next
            if next == None:
                break
            else:
                right = next.next
        return dummy.next



class Solution_3rd:
    # @param a ListNode
    # @return a ListNode
    def swapPairs(self, head):
        dummyleft, dummyright = ListNode(0), ListNode(0)
        dummyleft.next, dummyright.next = dummyright,head
        if not head or not head.next:
            return head
        prev,left,right = dummyright, dummyleft, dummyright
        while right.next and right.next.next:
            left = left.next.next
            right = right.next.next
            prev.next = right
            afterright = right.next
            right.next =left
            left.next = afterright
            left = prev.next
            right = left.next
            prev = right
        return dummyright.next