__author__ = 'effy'
'''
Given preorder and inorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.
'''

class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None
'''
preorder starts with the root node, same with post/in construct
'''
class Solution:
    # @param preorder, a list of integers
    # @param inorder, a list of integers
    # @return a tree node
    def buildTree(self, preorder, inorder):
        l = len(preorder)
        if l == 0:
            return
        root = TreeNode(preorder[0])
        if l == 1:
            return root
        mid = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1:mid+1], inorder[:mid])
        root.right = self.buildTree(preorder[mid+1:], inorder[mid+1:])
        return root

class Solution_secondround:
    # @param {integer[]} preorder
    # @param {integer[]} inorder
    # @return {TreeNode}
    def buildTree(self, preorder, inorder):
        if len(preorder) == 0:
            return None
        rootval = preorder[0]
        root = TreeNode(rootval)
        if len(preorder) == 1:
            return root
        root_index = inorder.index(rootval)
        root.left = self.buildTree(preorder[1:root_index+1], inorder[:root_index])
        root.right = self.buildTree(preorder[root_index+1:], inorder[root_index+1:])
        return root