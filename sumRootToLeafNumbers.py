__author__ = 'effy'
'''
Given a binary tree containing digits from 0-9 only, each root-to-leaf path could represent a number.

An example is the root-to-leaf path 1->2->3 which represents the number 123.

Find the total sum of all root-to-leaf numbers.

For example,

    1
   / \
  2   3
The root-to-leaf path 1->2 represents the number 12.
The root-to-leaf path 1->3 represents the number 13.

Return the sum = 12 + 13 = 25.
'''

class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution:
    # @param root, a tree node
    # @return an integer
    def sumNumbers(self, root):
        res = []
        if root == None:
            return 0
        def numbers(cur,num_so_far):
            if cur.left == None and cur.right == None:
                res.append(num_so_far*10+cur.val)
            if cur.left:
                numbers(cur.left, num_so_far*10+cur.val)
            if cur.right:
                numbers(cur.right, num_so_far*10+cur.val)
        numbers(root,0)
        print res
        return sum(res)
root, a, b = TreeNode(1),TreeNode(2),TreeNode(3)
root.left, root.right = a, b
x = Solution()
print x.sumNumbers(root)

