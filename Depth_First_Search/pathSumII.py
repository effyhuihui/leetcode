__author__ = 'effy'
'''
Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals
the given sum.

For example:
Given the below binary tree and sum = 22,
              5
             / \
            4   8
           /   / \
          11  13  4
         /  \    / \
        7    2  5   1
return
[
   [5,4,11,2],
   [5,8,4,5]
]
'''
class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution:
    # @param root, a tree node
    # @param sum, an integer
    # @return a list of lists of integers
    def pathSum(self, root, sum):
        def dfs(root, currsum, path):
            if root.left==None and root.right==None:
                if currsum==sum:
                    res.append(path)
            ## it is always safer to say path+[val], becasue path may sometimes be None type
            if root.left:
                dfs(root.left, currsum+root.left.val, path+[root.left.val])
            if root.right:
                dfs(root.right, currsum+root.right.val, path+[root.right.val])
        res=[]
        if root==None: return []
        dfs(root, root.val, [root.val])
        return res


class Solution_secondround:
    # @param root, a tree node
    # @param sum, an integer
    # @return a list of lists of integers
    def pathSum(self, root, sum):
        res = []
        def dfs(root,path,remain):
            if root.left == None and root.right == None:
                if remain == root.val:
                    res.append(path+[root.val])
            if root.left:
                dfs(root.left, path+[root.val],remain-root.val)
            if root.right:
                dfs(root.right, path+[root.val], remain-root.val)
        if root == None:
            return res
        dfs(root,[],sum)
        return res


x = Solution()
print x.pathSum(None,1)






