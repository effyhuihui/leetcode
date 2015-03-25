__author__ = 'effy'
'''
Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.

If the number of nodes is not a multiple of k then left-out nodes in the end should remain as it is.

You may not alter the values in the nodes, only nodes itself may be changed.

Only constant memory is allowed.

For example,
Given this linked list: 1->2->3->4->5

For k = 2, you should return: 2->1->4->3->5

For k = 3, you should return: 3->2->1->4->5
'''
class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution:
    # @param head, a ListNode
    # @param k, an integer
    # @return a ListNode
    def reverse(self, start, end):
        '''
        :param start: the start nodes to be reversed
        :param end:  the end nodes that DOES NOT need to be reversed
        :return: return the reversed list head
        '''
        current = start
        last = end
        while current != end:
            next = current.next
            current.next = last
            last = current
            current = next
        ## last will be the reversed list head
        return last

    def reverseKGroup(self, head, k):
        dummy = ListNode(0)
        dummy.next = head
        prev_list = dummy
        start= head
        while start:
            bottom = start
            ##bottom is the last node to be reversed.
            for i in range(k-1):
                bottom = bottom.next
                if not bottom:
                    return dummy.next
            ## advance end one node after, it is ok that in this reversion, end is None
            end = bottom.next
            ## if there is a sub list to be reversed, break the prev list first, before reverse
            prev_list.next = None
            newhead = self.reverse(start,end)
            ## link back the reversed list to the whole list
            prev_list.next = newhead
            ## reassign prev_list to be the last node of the reversed list, which is "start"
            prev_list = start
            ## reassign "start" to be "end"
            start = end
        return dummy.next

a,b,c,d,e = ListNode(1), ListNode(2),ListNode(3),ListNode(4), ListNode(5)
a.next,b.next,c.next,d.next = b,c,d,e
x = Solution()
t = x.reverseKGroup(a,3)
while t:
    print t.val
    t = t.next















