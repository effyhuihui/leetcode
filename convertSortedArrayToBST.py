__author__ = 'effy'
'''
Given an array where elements are sorted in ascending order, convert it to a height balanced BST.
'''
class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution:
    # @param num, a list of integers
    # @return a tree node
    def sortedArrayToBST(self, num):
        ## handle special cases
        if not num:
            return None
        l = len(num)
        if l == 1:
            return TreeNode(num[0])
        ## root is the middle element
        root = TreeNode(num[l//2])
        ## assign left and right respectively :)
        root.left = self.sortedArrayToBST(num[:l//2])
        root.right = self.sortedArrayToBST(num[l//2+1:])
        return root

a = [1,2,3,4,5,6,7]
x = Solution()
nodes = x.sortedArrayToBST(a)
print nodes.val
print nodes.left.val, nodes.right.val

