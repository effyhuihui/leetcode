# -*- coding: utf-8 -*-
__author__ = 'effy'
'''
Given a singly linked list where elements are sorted in ascending order,
convert it to a height balanced BST.
'''

class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

# Definition for singly-linked list.
class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None
'''
相比于convertSortedArrayToBST更麻烦的是如何处理linked list
这里用了两个helper method， 一个用于长度的获取，另外一个则是找到mid 点，并把linked list分成两段。
注意if elif else block里面需要分别对三种情况的当前linked list进行处理。
'''
class Solution:
    # @param head, a list node
    # @return a tree node
    def sortedListToBST(self, head):
        def listLen(head):
            count = 0
            while head:
                head = head.next
                count += 1
            return count
        def findMid(head):
            ## return one node before mid
            l = listLen(head)
            for i in range(l//2-1):
                head = head.next
            return head
        l = listLen(head)
        if l > 1:
            prev = findMid(head)
            mid = prev.next
            root = TreeNode(mid.val)
            prev.next = None
            right_head = mid.next
            root.left = self.sortedListToBST(head)
            root.right = self.sortedListToBST(right_head)
        elif l == 1:
            root = TreeNode(head.val)
        else:
            root = None
        return root




