# -*- coding: utf-8 -*-
__author__ = 'effy'
'''
Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the
shortest path from the root node down to the nearest leaf node.
'''
class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution_iterative:
    # @param root, a tree node
    # @return an integer
    def minDepth(self, root):
        min_depth = float("inf")
        if root == None:
            return 0
        nodes = [(root,1)]
        while nodes:
            cur = nodes.pop()
            if cur[0].left == None and cur[0].right == None:
                min_depth = min(cur[1],min_depth)
            else:
                if cur[0].left: nodes.append(cur[0].left, cur[1]+1)
                if cur[0].right: nodes.append(cur[0].right, cur[1]+1)
        return min_depth
'''
和求树的max depth有所不同
分几种情况考虑：1，树为空，则为0。
2，根节点如果只存在左子树或者只存在右子树，则返回值应为左子树或者右子树的（最小深度+1）。
3，如果根节点的左子树和右子树都存在，则返回值为（左右子树的最小深度的较小值+1）。
'''
class Solution_recursive:
    # @param root, a tree node
    # @return an integer
    def minDepth(self, root):
        if root == None:
            return 0
        if root.left == None and root.right != None:
            return self.minDepth( root.right ) + 1
        if root.left != None and root.right == None:
            return self.minDepth( root.left ) + 1
        return min( self.minDepth( root.left ), self.minDepth( root.right ) ) + 1

