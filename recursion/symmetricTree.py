__author__ = 'effy'
'''
Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

For example, this binary tree is symmetric:

    1
   / \
  2   2
 / \ / \
3  4 4  3
But the following is not:
    1
   / \
  2   2
   \   \
   3    3
Note:
Bonus points if you could solve it both recursively and iteratively.
'''

class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution_recursive:
    # @param root, a tree node
    # @return a boolean
    def isSymmetric(self, root):
        if not root:
            return True
        ## compare left's left child with right's right child, and left'right with right's left
        def mirrorTree(root1, root2):
            if root1 == None and root2 == None:
                return True
            if root1 and root2 and root1.val == root2.val:
                return mirrorTree(root1.left, root2.right) and mirrorTree(root1.right, root2.left)
            return False
        return mirrorTree(root.left, root.right)


class Solution_iterative:
    # @param root, a tree node
    # @return a boolean
    def isSymmetric(self, root):
        if not root:
            return True
        sub_left,sub_right = [root.left], [root.right]
        while sub_left and sub_right:
            l, r = sub_left.pop(), sub_right.pop()
            if l == None and r == None:
                return True
            if l and r and l.val == r.val:
                ## sequence matters!!!!!
                sub_left.append(l.left)
                sub_left.append(l.right)
                sub_right.append(r.right)
                sub_right.append(r.left)
            else:
                print 'in'
                return False
        if sub_left or sub_right:
            return False
        return True


class Solution_secondround:
    # @param root, a tree node
    # @return a boolean
    def isSymmetric(self, root):
        if root == None or (root.left == None and root.right == None):
            return True
        def isMirror(rootleft, rootright):
            if rootleft == None and rootright == None:
                return True
            if rootleft == None or rootright == None:
                return False
            if rootleft.val != rootright.val:
                return False
            return isMirror(rootleft.right, rootright.left) and isMirror(rootleft.left, rootright.right)

        return isMirror(root.left,root.right)




root,a,b,c,d,e = TreeNode(2),TreeNode(3),TreeNode(3),TreeNode(4),TreeNode(5),TreeNode(5)
root.left,root.right, a.left,a.right,b.right = a,b,c,d,e
x = Solution_iterative()
print x.isSymmetric(root)

















