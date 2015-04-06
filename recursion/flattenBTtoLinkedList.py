# -*- coding: utf-8 -*-
__author__ = 'effy'
'''
Given a binary tree, flatten it to a linked list in-place.

For example,
Given

         1
        / \
       2   5
      / \   \
     3   4   6
The flattened tree should look like:
   1
    \
     2
      \
       3
        \
         4
          \
           5
            \
             6
思路是这样的：
每次拿到一个current root， 分成左子树和右子树，1. 找到左子树的right most node 2. 把右子树挪到左子树的right most
node的右边  3.把新的左子树放到current root的右边，4. 再把current的左子树变成None

这样的话每一步做完，当前的current root就不再有左子树恩恩
上面的例子可以变成这样：
Step 1: current = 1
         1
        / \
       2   5
      / \   \
     3   4   6


         1
        /
       2
      / \
     3   4
          \
           5
             \
              6

     1
      \
       2
      / \
     3   4
          \
           5
             \
              6

Step 2: current  = 2
     1
      \
       2
      / \
     3   4
          \
           5
             \
              6
     1
      \
       2
      /
     3
      \
       4
        \
         5
          \
           6

     1
      \
       2
        \
         3
          \
           4
            \
             5
              \
               6
检验接下来每个current root， 直到所有的current root都没有左子树停止
'''
class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution:
    # @param root, a tree node
    # @return nothing, do it in place
    def flatten(self, root):
        def goToRightMost(root):
            while root.right:
                root = root.right
            return root
        if root != None:
            left = root.left
            if left:
            ## find the right most node in the current left sub tree
                rightmost = goToRightMost(left)
                ## move current right sub tree to right most node in current left sub tree
                rightmost.right = root.right
                ## move current left sub tree to the current.right
                root.right = left
                ## remember to assign left to be none to avoid infinite loop
                root.left = None
            ## and then continue, current root = current.right
            self.flatten(root.right)


