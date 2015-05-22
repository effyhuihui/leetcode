# -*- coding: utf-8 -*-
__author__ = 'effy'
# Definition for a  binary tree node
'''
Given a binary tree, return the preorder traversal of its nodes' values.

For example:
Given binary tree {1,#,2,3},
   1
    \
     2
    /
   3
return [1,2,3].
中，左，右
Note: Recursive solution is trivial, could you do it iteratively?
'''
class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None
'''
thoughts:
1. init a stack, and a value list
2 push root in if not None else return []
3.the main body is a while loop
4 if the stack is not empty:
    pop the cur node from stack
    add its value to value list
    add right child to stack if exist (ADD RIGHT CHILD FIRST)
    add left child to stack if exits(ADD LEFT CHILD SECOND)
5. finally return value list
'''

class Solution:
    # @param root, a tree node
    # @return a list of integers
    def preorderTraversal(self, root):
        res = []
        stack = []
        if not root:
            return res
        stack.append(root)
        while stack:
            cur = stack.pop()
            res.append(cur.val)
            if cur.right:
                stack.append(cur.right)
            if cur.left:
                stack.append(cur.left)
        return res


class Solution:
    # @param root, a tree node
    # @return a list of integers
    def preorderTraversal(self, root):
        res = []
        if root == None:
            return []
        res+= [root.val]
        res += self.preorderTraversal(root.left)
        res+= self.preorderTraversal(root.right)
        return res



root = TreeNode(1)
a = TreeNode(2)
b = TreeNode(3)
root.left, root.right = a, b
c = TreeNode(4)
d = TreeNode(5)
a.right=c
b.left = d

x = Solution()
print x.preorderTraversal(root)

