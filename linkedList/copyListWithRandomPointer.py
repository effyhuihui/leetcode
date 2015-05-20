__author__ = 'effy'
'''
A linked list is given such that each node contains an additional random pointer which
could point to any node in the list or null.

Return a deep copy of the list.

http://www.cnblogs.com/zuoyuan/p/3745126.html
'''
class RandomListNode:
     def __init__(self, x):
         self.label = x
         self.next = None
         self.random = None

class Solution:
    # @param head, a RandomListNode
    # @return a RandomListNode
    def copyRandomList(self, head):
        if not head:
            return head
        current = head
        ## copy node and insert to  the right of original node
        while current:
            new = RandomListNode(current.label)
            next = current.next
            current.next = new
            new.next = next
            current = next
        ## copy random pointer
        current = head
        while current:
            if current.random:
                current.next.random = current.random.next
            current = current.next.next
        ## extract the new list out of the original list
        new_head = head.next
        current = head
        while current:
            new_current = current.next
            ## change back the original list
            current.next = current.next.next
            if new_current.next:
                new_current.next = new_current.next.next
            ## advance one node ahead
            current = current.next
        return new_head



class Solution_secondround:
    # @param head, a RandomListNode
    # @return a RandomListNode
    def copyRandomList(self, head):
        if head == None:
            return None
        copy = {}
        cur = head
        while cur:
            copy[cur] = RandomListNode(cur.label)
            cur = cur.next
        cur = head
        while cur:
            new = copy[cur]
            if cur.next:
                new.next = copy[cur.next]
            if cur.random:
                new.random = copy[cur.random]
            cur = cur.next
        return copy[head]