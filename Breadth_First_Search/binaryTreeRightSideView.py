__author__ = 'effy'
'''
Given a binary tree, imagine yourself standing on the right side of it,
return the values of the nodes you can see ordered from top to bottom.

For example:
Given the following binary tree,
   1            <---
 /   \
2     3         <---
 \     \
  5     4       <---
You should return [1, 3, 4].

    1
   /
  2
You should return [1,2]
'''

'''
similar to level order traversal , append the right most node in each level
'''
class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of integers
    def rightSideView(self, root):
        res = []
        if root == None:
            return res
        queue = [root]
        while queue:
            ## use a stack to mimic queue...>___< not super efficient
            cur = queue[-1]
            res.append(cur.val)
            ## pop all nodes that from the last level
            l = len(queue)
            for i in range(l):
                cur = queue.pop(0)
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
            ## now inside queue should only have next level node
        return res


from collections import deque
class Solution_secondround:
    # @param root, a tree node
    # @return a list of integers
    def rightSideView(self, root):
        res = []
        if root == None:
            return res
        queue = deque()
        queue.append(root)
        while queue:
            res.append(queue[-1].val)
            l = len(queue)
            for i in range(l):
                cur = queue.popleft()
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
        return res



