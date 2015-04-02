__author__ = 'effy'
'''
Given a binary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
'''
# Definition for a  binary tree node
class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution_DFS:
    # @param root, a tree node
    # @return an integer
    def maxDepth(self, root):
        max_depth = 0
        if not root:
            return 0
        nodes = [(root,1)]
        ## DFS use a stack
        while nodes:
            cur = nodes.pop()
            ## if cur is the leaf, compare and assign new max_depth
            if not cur[0].left and not cur[0].right:
                max_depth = max(cur[1], max_depth)
            ## if it is not leaf, push a new tuple into nodes with
            ## 1 more length advance
            else:
                if cur[0].right:
                    nodes.append((cur[0].right,cur[1]+1))
                if cur[0].left:
                    nodes.append((cur[0].left,cur[1]+1))
        return max_depth

class Solution_recursion:
    # @param root, a tree node
    # @return an integer
    def maxDepth(self,root):
        if not root:
            return 0
        return  max(self.maxDepth(root.left)+1, self.maxDepth(root.right)+1)

a,b,c,d,e = TreeNode(1), TreeNode(1),TreeNode(1),TreeNode(1), TreeNode(1)
a.left,a.right = b,c
b.left = d
d.right = e

r = TreeNode(1)
x = Solution_recursion()
print x.maxDepth(a)

