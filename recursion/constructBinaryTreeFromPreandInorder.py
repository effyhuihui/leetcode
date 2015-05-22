__author__ = 'effy'
'''
Given preorder and inorder traversal of a tree, construct the binary tree.


'''
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