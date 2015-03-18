# -*- coding: utf-8 -*-
__author__ = 'effy'
'''
Given a binary tree, return the zigzag level order traversal of its nodes' values. (ie, from left to right, then right to left for the next level and alternate between).

For example:
Given binary tree {3,9,20,#,#,15,7},
    3
   / \
  9  20
    /  \
   15   7
return its zigzag level order traversal as:
[
  [3],
  [9,20],
  [15,7]
]
'''
# Definition for a  binary tree node
class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of lists of integers

    def zigzagLevelOrder(self, root):
        stack = []
        res = []
        if not root:
            return stack
        stack.append(root)
        res.append([root])
        while res[-1]:
            res.append([])
            for i in res[-1]:
                while i:
                    if i.left:
                        stack.append(i.left)
                    if i.right:
                        stack.append(i.right)
            while stack:
                res[-1].append(stack.pop())
        return res

a = TreeNode(3)
b = TreeNode(9)
c = TreeNode(20)
d = TreeNode(15)
e = TreeNode(7)

a.left = b
a.right = c
b.left = d
b.right = e
x = Solution()
print x.zigzagLevelOrder(a)