__author__ = 'effy'
'''
Given a binary tree, find the maximum path sum.

The path may start and end at any node in the tree.

For example:
Given the below binary tree,

       1
      / \
     2   3
Return 6.
'''
class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution:
    # @param root, a tree node
    # @return an integer
    def maxsum(self, root):
        if root == None: return 0
        sum = root.val
        lmax = 0; rmax = 0
        if root.left:
            lmax = self.maxsum(root.left)
            if lmax > 0:
                sum += lmax
        if root.right:
            rmax = self.maxsum(root.right)
            if rmax > 0:
                sum += rmax
        if sum > Solution.max: Solution.max = sum
        return max(root.val, max(root.val + lmax, root.val + rmax))

    def maxPathSum(self, root):
        Solution.max = -10000000
        if root == None: return 0
        self.maxsum(root)
        return Solution.max

