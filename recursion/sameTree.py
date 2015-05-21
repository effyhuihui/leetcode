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
        ## continue check only when the current value is the same
        if p and q and p.val == q.val:
            ## check the left and right recursively
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        return False

class Solution_secondround:
    # @param p, a tree node
    # @param q, a tree node
    # @return a boolean
    def isSameTree(self, p, q):
        if p == None and q == None:
            return True
        if p == None or q == None:
            return False
        if p.val != q.val:
            return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right,q.right)






a,b = TreeNode(1),TreeNode(1)
a.left = b
c,d, = TreeNode(1),TreeNode(1)
c.right = d
x = Solution()
print x.isSameTree(d,b)