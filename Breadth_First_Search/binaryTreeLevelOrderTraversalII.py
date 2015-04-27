__author__ = 'effy'
'''
Given a binary tree, return the bottom-up level order traversal of its nodes' values.
(ie, from left to right, level by level from leaf to root).

For example:
Given binary tree {3,9,20,#,#,15,7},
    3
   / \
  9  20
    /  \
   15   7
return its bottom-up level order traversal as:
[
  [15,7],
  [9,20],
  [3]
]
'''

class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of lists of integers
    def levelOrderBottom(self, root):
        def preorder(root, level,res):
            if root:
                if len(res)<level+1:
                    res.append([])
                res[level].append(root.val)
                preorder(root.left,level+1, res)
                preorder(root.right, level+1, res)
        res = []
        preorder(root,0, res)
        final = []
        for i in reversed(res):
            final.append(i)
        return final
a = TreeNode(1)
x = Solution()
print x.levelOrderBottom(a)