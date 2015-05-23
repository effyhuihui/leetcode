__author__ = 'effy'
# -*- coding: utf-8 -*-
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
    def __init__(self):
        self.max = -10000000
    '''
    maxsum(root) returns root直的左枝，root直的右枝的最大值 注意，“直” 表示如果是左支，那么每一个child都是
    parent的left child，右支同理
    '''
    def maxsum(self, root):
        if root == None:
            return 0
        skew_sum = root.val
        lmax = self.maxsum(root.left)
        rmax = self.maxsum(root.right)
        if lmax > 0:
            skew_sum += lmax
        if rmax > 0:
            skew_sum += rmax
        if skew_sum > self.max:
            self.max = skew_sum
        return max(root.val, max(root.val + lmax, root.val + rmax))

    def maxPathSum(self, root):
        if root == None:
            return 0
        self.maxsum(root)
        return self.max

class Solution_secondround:
    # @param root, a tree node
    # @return an integer
    def __init__(self):
        self.max_sum = -10000000
    def maxPathSum(self, root):
        def maxSkewSum(cur_node):
            if cur_node == None:
                return 0
            lmax = maxSkewSum(cur_node.left)
            rmax = maxSkewSum(cur_node.right)
            ## skew_sum represent the sum that from left to cur_node and to cur_node right :)
            skew_sum = cur_node.val
            if lmax >0:
                skew_sum += lmax
            if rmax >0:
                skew_sum += rmax
            if skew_sum > self.max_sum:
                self.max_sum = skew_sum
            ##the path is either go with the left side, or right side, or just one node (if left and right sum are both
            ## less than zero )
            return max(cur_node.val,cur_node.val+lmax, cur_node.val+rmax)
        if root == None:
            return 0
        maxSkewSum(root)
        return self.max_sum