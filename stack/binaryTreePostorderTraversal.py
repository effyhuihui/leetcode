# -*- coding: utf-8 -
__author__ = 'effy'
'''
Given a binary tree, return the postorder traversal of its nodes' values.

For example:
Given binary tree {1,#,2,3},
   1
    \
     2
    /
   3
return [3,2,1]
左，右，中
'''
# Definition for a  binary tree node
class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

'''
这个方法会改变树的形状，因为在途中要set left right为None
'''
class Solution:
    # @param root, a tree node
    # @return a list of integers
    def postorderTraversal(self, root):
        stack = [root]
        res = []
        if not root:
            return res
        while stack:
            cur = stack[-1]
            if not cur.left and not cur.right:
                res.append(stack.pop().val)
            else:
                if cur.right:
                    stack.append(cur.right)
                    cur.right = None
                if cur.left:
                    stack.append(cur.left)
                    cur.left = None
        return res

class Solution2:
    def postorderTraversal(self, root):
        stack = []
        res = []
        def goToMostLeft(cur):
            while cur:
                stack.append(cur)
                cur = cur.left
        def goToMostRight(cur):
            while cur:
                stack.append(cur)
                cur = cur.right
        if not root:
            return res
        goToMostLeft(root)
        while stack:
            cur = stack[-1]
            if not cur.right:
                stack.pop()
                res.append(cur.val)
            goToMostRight(cur)
            cur.right = None
        return res














root = TreeNode(8)
a = TreeNode(2)
b = TreeNode(3)
c = TreeNode(4)
d = TreeNode(5)
e = TreeNode(6)
f = TreeNode(7)

root.right = b
root.left = a
a.left = c
a.right = d
b.left = e
b.right = f

x = Solution2()
print x.postorderTraversal(root)
