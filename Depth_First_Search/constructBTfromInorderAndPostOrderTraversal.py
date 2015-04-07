__author__ = 'effy'
'''
Given inorder and postorder traversal of a tree, construct the binary tree.
you may assume duplicates does not exist
'''
class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None
'''
post order traversal always end with the root node.
1. get the last from post array, construct root
2. find same value in inorder array
3. split inorder into left and right
4. recursion
'''
class Solution:
    # @param postorder, a list of integers
    # @param inorder, a list of integers
    # @return a tree node
    def buildTree(self, postorder, inorder):
        l = len(postorder)
        if l == 0:
            return
        root = TreeNode(postorder[-1])
        if l == 1:
            return root
        mid = inorder.index(postorder[-1])
        root.left = self.buildTree(postorder[mid:l-1], inorder[:mid])
        root.right = self.buildTree(postorder[:mid], inorder[mid+1:])
        return root