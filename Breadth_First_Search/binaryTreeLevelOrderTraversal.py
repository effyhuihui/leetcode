__author__ = 'effy'
'''
Given a binary tree, return the level order traversal of its nodes' values.
(ie, from left to right, level by level).

For example:
Given binary tree {3,9,20,#,#,15,7},
    3
   / \
  9  20
    /  \
   15   7
return its level order traversal as:
[
  [3],
  [9,20],
  [15,7]
]
'''
from collections import deque
class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution_bfs:
    # @param root, a tree node
    # @return a list of lists of integers
    def levelOrder(self, root):
        queue = deque()
        res = []
        if root == None:
            return queue
        queue.append = [root]
        while queue:
            current = queue.popleft()
            temp_queue = deque()
            temp_res = []
            while current:
                cur = current.popleft()
                temp_res.append(cur.val)
                if cur.left:
                    temp_queue.append(cur.left)
                if cur.right:
                    temp_queue.append(cur.right)
            if temp_queue:
                queue.append(temp_queue)
            if temp_res:
                res.append(temp_res)
        return res
'''
ues preorder dfs to accomplish bfs
'''
class Solution_dfs:
    # @param root, a tree node
    # @return a list of lists of integers
    def levelOrder(self, root):
        def preorder(root,level,res):
            if root:
                if len(res) < level+1:
                    res.append([])
                res[level].append(root.val)
                preorder(root.left, level+1, res)
                preorder(root.right, level+1, res)
        res = []
        preorder(root,0,res)
        return res





























