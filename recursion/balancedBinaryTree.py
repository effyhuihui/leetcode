__author__ = 'effy'
'''
Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as a binary
tree in which the depth of the two subtrees of every node never differ by more than 1.
'''

class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None
## purely recursion
class Solution:
    # @param root, a tree node
    # @return a boolean
    def height(self,root):
        if root == None:
            return 0
        return 1+max(self.height(root.left), self.height(root.right))

    def isBalanced(self, root):
        if root == None:
            return True
        left_height, right_height = self.height(root.left), self.height(root.right)
        return abs(left_height-right_height) <= 1 and self.isBalanced(root.left) and self.isBalanced(root.right)

## preserve the height for each node along the way
class Solution_memorization:
    def __init__(self):
        self.heights = {}

    def height(self,root):
        if root == None:
            return 0
        return 1+max(self.height(root.left), self.height(root.right))

    def isBalanced(self, root):
        if root == None:
            return True
        if root.left  not in self.heights:
            self.heights[root.left] = self.height(root.left)
        if root.right not in self.heights:
            self.heights[root.right] = self.height(root.right)
        left_height, right_height = self.heights[root.left], self.heights[root.right]
        return abs(left_height-right_height) <= 1 and self.isBalanced(root.left) and self.isBalanced(root.right)


class Solution_secondround:
    def __init__(self):
        self.heights = {None:0}
    def height(self,root):
        if root in self.heights:
            return self.heights[root]
        h = max(self.height(root.left), self.height(root.right)) +1
        self.heights[root] = h
        return h
    def isBalanced(self, root):
        if root == None:
            return True
        leftroot = root.left
        rightroot = root.right
        return abs(self.height(leftroot)-self.height(rightroot))<=1 and self.isBalanced(leftroot) and self.isBalanced(rightroot)


