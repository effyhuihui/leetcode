__author__ = 'effy'
'''
Given inorder and postorder traversal of a tree, construct the binary tree.
'''

class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution:
    # @param {integer[]} inorder
    # @param {integer[]} postorder
    # @return {TreeNode}
    def buildTree(self, inorder, postorder):
        if len(inorder) == 0:
            return None
        rootval = postorder[-1]
        root = TreeNode(rootval)
        root_index = inorder.index(rootval)
        root.left = self.buildTree(inorder[:root_index],postorder[:root_index])
        root.right = self.buildTree(inorder[root_index+1:], postorder[root_index:len(postorder)-1])
        return root