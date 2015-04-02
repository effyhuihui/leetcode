__author__ = 'effy'
'''
Given two binary trees, write a function to check if they are equal or not.

Two binary trees are considered equal if they are structurally identical and the nodes have the same value.
'''
class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution:
    # @param p, a tree node
    # @param q, a tree node
    # @return a boolean
    def isSameTree(self, p, q):
        ## both are None
        if not p and not q:
            return True
        if p != None and q != None:
            return (p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right))
        else:
            return False
a,b = TreeNode(1),TreeNode(1)
a.left = b
c,d, = TreeNode(1),TreeNode(1)
c.right = d
x = Solution()
print x.isSameTree(d,b)