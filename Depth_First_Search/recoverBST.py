__author__ = 'effy'
'''
Two elements of a binary search tree (BST) are swapped by mistake.

Recover the tree without changing its structure.

Note:
A solution using O(n) space is pretty straight forward.
Could you devise a constant space solution?
'''
class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None


## inorder traversal takes O(N) but sort takes O(NlogN)
## not super efficient
class Solution:
    # @param root, a tree node
    # @return nothing, modify the binary tree in-place instead.
    def recoverTree(self, root):
        nodes, value = self.inorder(root)
        value.sort()
        for i in range(len(nodes)):
            nodes[i].val = value[i]

    def inorder(self,root):
        stack = []
        nodes, value = [], []
        def goToMostleft(cur):
            while cur:
                stack.append(cur)
                cur = cur.left
        goToMostleft(root)
        while stack:
            cur = stack.pop()
            nodes.append(cur)
            value.append(cur.val)
            goToMostleft(cur.right)
        return nodes, value
