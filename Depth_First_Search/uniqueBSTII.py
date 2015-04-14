__author__ = 'effy'
# -*- coding: utf8 -*-
'''
Given n, generate all structurally unique BST's (binary search trees) that store
values 1...n.

For example,
Given n = 3, your program should return all 5 unique BST's shown below.

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3
'''
class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None
'''
想要得到所有的res 用dfs
'''
class Solution:
    # @return a list of tree node
    def generateTrees(self, n):
        ## dfs returns a list of BST that have values ranging from start to end
        def dfs(start, end):
            if start > end:
                return [None]
            res = []
            for rootval in range(start,end+1):
                ## get a list of possible left sub trees given a root value
                leftSubTree = dfs(start,rootval-1)
                ## get a list of possible right sub trees given a root value
                rightSubTree = dfs(rootval+1, end)
                ## to get all combinations of left,right sub trees given a root value
                for i in leftSubTree:
                    for j in rightSubTree:
                        root = TreeNode(rootval)
                        root.left, root.right = i,j
                        res.append(root)
            return res
        return dfs(1,n)

