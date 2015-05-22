__author__ = 'effy'
# -*- coding: utf-8 -*-
__author__ = 'effy'
'''
Given a binary tree

    struct TreeLinkNode {
      TreeLinkNode *left;
      TreeLinkNode *right;
      TreeLinkNode *next;
    }
Populate each next pointer to point to its next right node. If there is no next right node, the next pointer
should be set to NULL.

Initially, all next pointers are set to NULL.

Note:

You may only use constant extra space.
You may assume that it is a perfect binary tree (ie, all leaves are at the same level, and every parent has two children).
For example,
Given the following perfect binary tree,
         1
       /  \
      2    3
     / \  / \
    4  5  6  7
After calling your function, the tree should look like:
         1 -> NULL
       /  \
      2 -> 3 -> NULL
     /      \
    4------->7 -> NULL
'''
class TreeLinkNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None
         self.next = None

class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        if root == None:
            return root
        parent = [root]
        children = []
        while parent or children:
            ## if parent is not None
            ## pop each node and add into children stack
            ## first right and then left
            while parent:
                cur = parent.pop()
                ## only difference from populate next right pointer 1
                if cur.right:
                    children.append(cur.right)
                if cur.left:
                    children.append(cur.left)
            ## inside children are nodes in the same level from right to left
            ## pop each node and pointing to its left neighbor in children stack
            ## note that the last popped node will bethe right most node in the same
            ## level, so its next will always be None
            ## And add that not-None node back to parent stack to go one level down
            while children:
                cur = children.pop()
                if cur:
                    if children:
                        cur.next = children[-1]
                    else:
                        cur.next = None
                    parent.append(cur)


from collections import deque
class Solution_secondround:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        if root == None:
            return
        parent = deque()
        parent.append(root)
        children = deque()
        while parent or children:
            while parent:
                cur= parent.popleft()
                if cur.left:
                    children.append(cur.left)
                if cur.right:
                    children.append(cur.right)
            while children:
                cur = children.popleft()
                if children:
                    cur.next= children[0]
                parent.append(cur)





a,b,c,d,e,f,g = TreeLinkNode(1),TreeLinkNode(2),TreeLinkNode(3),TreeLinkNode(4),TreeLinkNode(5),TreeLinkNode(6),TreeLinkNode(7)
a.left, a.right,b.left,b.right,c.left,c.right=b,c,d,e,f,g
x = Solution()
s = [x.connect(a)]
while s:
    cur = s.pop()
    print cur.val,cur.next
    if cur.left:
        s.append(cur.left)
    if cur.right:
        s.append(cur.right)



