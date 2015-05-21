__author__ = 'effy'
# -*- coding: utf-8 -*-
'''
Given a binary tree, determine if it is a valid binary search tree (BST).

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
'''
'''
解题思路：看到二叉树我们首先想到需要进行递归来解决问题。这道题递归的比较巧妙。让我们来看下面一棵树：

　　　　　　　　　　　　　　　　　    4

　　　　　　　　　　　　　　　　　/      \
　　　　　　　　　　　　　　　　 2　　     6

　　　　　　　　　　　　　　　 /    \   /   \

　　　　　　　　　　　　　　  1      5 3    7

对于一颗子树，root.left这棵树的所有节点值都小于root，
root.right这棵树的所有节点值都大于root。然后依次递归下去就可以了。
例如：如果这棵树是二叉查找树，那么左子树的节点值一定处于（负无穷，4）这个范围内，
右子树的节点值一定处于（4，正无穷）这个范围内。
对于一颗子树  6    他的左子树范围应该也在 （负无穷，4）之间，而在以3为root的tree中，左子树应为 负无穷到3.。
          /  \
         3    7

'''
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a boolean
    def isValidBST(self, root):
        def validSubTree(root, min,max):
            if root == None:
                return True
            if root.val >= max or root.val <= min:
                return False
            ## if current val is valid, then check the left sub tree with updated value range, same to right
            return validSubTree(root.left, min, root.val) and validSubTree(root.right,root.val, max)
        lower_bound = -float('inf')
        upper_bound = float('inf')
        return validSubTree(root, lower_bound, upper_bound)

class Solution_second_round:
    # @param root, a tree node
    # @return a boolean
    def isValidBST(self, root):
        def validSubBST(root,smallest,biggest):
            if root == None:
                return True
            if root.val <= smallest or root.val >= biggest:
                return False
            ## go to sub tree, the bound will change accordingly!!!!
            ## go to left node, the biggest val(upper bound) changes to current root val,
            ## go to the right node, the smallest val(lower bound) changes to current root val
            return validSubBST(root.left,smallest, root.val) \
                   and validSubBST(root.right, root.val,biggest)
        return validSubBST(root,-float('inf'),float('inf'))