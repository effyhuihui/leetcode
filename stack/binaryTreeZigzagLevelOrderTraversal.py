# -*- coding: utf-8 -*-
__author__ = 'effy'
'''
Given a binary tree, return the zigzag level order traversal of its nodes' values. (ie, from left to right, then right to left for the next level and alternate between).

For example:
Given binary tree {3,9,20,#,#,15,7},
    3
   / \
  9  20
    /  \
   15   7
return its zigzag level order traversal as:
[
  [3],
  [20,9],
  [15,7]
]

注意哦，在奇数level上得节点要翻转过来存入数组，level 1 不是9，20，而是20，9
'''
# Definition for a  binary tree node
class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None
'''
Below is the solution using stack
'''
class Solution:
    # @param root, a tree node
    # @return a list of lists of integers
    def zigzagLevelOrder(self, root):
        s1 = []
        s2 = []
        result = []
        level = 0
        if not root:
            return result
        s1.append(root)
        ## if level is odd
        while s1 or s2:
            result.append([])
            if level%2:
                while s2:
                    cur = s2.pop()
                    result[-1].append(cur.val)
                    if cur.right:
                        s1.append(cur.right)
                    if cur.left:
                        s1.append(cur.left)
            else:
                while s1:
                    cur = s1.pop()
                    result[-1].append(cur.val)
                    if cur.left:
                        s2.append(cur.left)
                    if cur.right:
                        s2.append(cur.right)
            level += 1
        return result


class Solution_secondround:
    # @param root, a tree node
    # @return a list of lists of integers
    def zigzagLevelOrder(self, root):
        res = []
        level = 0
        if root == None:
            return res
        stack =[root]
        while stack:
            res.append([])
            l = len(stack)
            temp_stack = []
            for i in range(l):
                cur = stack.pop()
                res[-1].append(cur.val)
                if level%2:
                    if cur.right:
                        temp_stack.append(cur.right)
                    if cur.left:
                        temp_stack.append(cur.left)
                else:
                    if cur.left:
                        temp_stack.append(cur.left)
                    if cur.right:
                        temp_stack.append(cur.right)
            stack += temp_stack
            level += 1
        return res




a = TreeNode(3)
b = TreeNode(9)
c = TreeNode(20)
d = TreeNode(15)
e = TreeNode(7)

a.left = b
a.right = c
b.left = d
b.right = e
x = Solution()
print x.zigzagLevelOrder(a)