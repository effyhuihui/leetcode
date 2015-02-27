# -*- coding: utf-8 -*-
__author__ = 'effy'
'''
Given a binary tree, return the inorder traversal of its nodes' values.

For example:
Given binary tree {1,#,2,3},
   1
    \
     2
    /
   3
return [1,3,2].
左，中，右
Note: Recursive solution is trivial, could you do it iteratively?

'''
# Definition for a  binary tree node
class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None
'''
这个方法改变了树的形状
'''
class Solution:
    # @param root, a tree node
    # @return a list of integers
    def inorderTraversal(self, root):
        stack = []
        inOrder = []
        if not root:
            return inOrder
        stack.append(root)
        while stack:
            cur = stack[-1]
            if cur.left:
                stack.append(cur.left)
                cur.left = None
            else:
                inOrder.append(stack.pop().val)
                if cur.right:
                    stack.append(cur.right)
        return inOrder

'''
这个方法不改变树的形状 -- 思路和binarySearchTreeIterator类似
'''
class Solution2:
    def inorderTraversal(self,root):
        stack = []
        inOrder = []

        def goToCurrentMostLeft(node):
            cur = node
            while cur:
                stack.append(cur)
                cur = cur.left

        goToCurrentMostLeft(root)
        while stack:
            cur = stack.pop()
            inOrder.append(cur.val)
            goToCurrentMostLeft(cur.right)
        return inOrder




a = TreeNode(1)
b = TreeNode(2)
c = TreeNode(3)
a.right = b
b.left = c
#x = Solution()
#print x.inorderTraversal(a)