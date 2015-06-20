'''
Given a sorted linked list, delete all duplicates such that each element appear only once.

For example,
Given 1->1->2, return 1->2.
Given 1->1->2->3->3, return 1->2->3.
'''

class LinkedList:
    def __init__(self, val):
        self.val = val
        self.next = None

class Solution:
    def deleteDuplicates(self, head):
        '''
        Given a sorted linked list, delete all duplicates such that each element appear only once.

        For example,
        Given 1->1->2, return 1->2.
        Given 1->1->2->3->3, return 1->2->3.
        '''
        if not head:
            return head
        prev = head
        cur = head.next
        while cur:
            if prev.val == cur.val:
                prev.next = cur.next
            else:
                prev = cur
            cur = prev.next
        return head



class Solution_3rd:
    # @param head, a ListNode
    # @return a ListNode
    def deleteDuplicates(self, head):
        dummy = ListNode(-100000)
        prev  = dummy
        dummy.next = head
        cur = head
        while cur:
            if cur.val != prev.val:
                prev.next = cur
                prev = cur
            cur =  cur.next
        prev.next = cur
        return dummy.next


a = LinkedList(1)
b = LinkedList(2)
a.next = b
x = Solution()
head = x.deleteDuplicates(a)
print head.val