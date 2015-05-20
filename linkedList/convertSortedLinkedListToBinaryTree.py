__author__ = 'effy'



class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None

class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None


class Solution_secondround:
    # @param head, a list node
    # @return a tree node
    def sortedListToBST(self, head):
        if head == None:
            return None
        if head.next == None:
            return TreeNode(head.val)
        dummy = ListNode(0)
        dummy.next = head
        slow, fast = dummy, head.next
        while fast.next:
            slow = slow.next
            fast = fast.next
            if fast.next:
                fast = fast.next
        mid = slow.next
        right = mid.next
        mid.next = None
        slow.next = None
        root = TreeNode(mid.val)
        ## because of the way slow and fast node are iterated, head might be the same node as mid
        ## so just to avoid duplicate, but fast can never be head.... haha
        if mid != head:
            root.left = self.sortedListToBST(head)
        root.right = self.sortedListToBST(right)
        return root