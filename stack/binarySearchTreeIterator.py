# -*- coding: utf-8 -*-
__author__ = 'effy'
'''
Implement an iterator over a binary search tree (BST).
Your iterator will be initialized with the root node of a BST.

Calling next() will return the next smallest number in the BST.

Note: next() and hasNext() should run in average O(1) time and uses O(h) memory,
where h is the height of the tree.
'''

'''
an iterator is an object which enables to traverse a container, like a list, in certain order.
最简易的一个iterator就是range(n)。当给一个end point n时，此iterator能从小到大以1向前推进进行traverse。

这道题目里，如果只是要implement next(), hasNext()method（也就是从小到大进行traverse）而对memory没有要求，
那么其实就是在__init__里面建一个in order traversal的list，然后用一个index来一个一个移动即可。

所以这里的catch就是如果maintain一个O(h)的memory。由于要最多可maintain一个树高的stack，想到不用一次性traverse完，
但需要动态维护这个list。在init的时候只需要traverse root的left subtree。还有一点需要注意的就是因为这个memory是有大小要求，
所以list必须一边traverse一边pop，从而达到要求。
'''




# Definition for a  binary tree node
class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class BSTIterator:
    # @param root, a binary search tree's root node
    def __init__(self, root):
        self.preOrder = []
        self.refresh(root)

    def refresh(self, cur):
        while cur:
            self.preOrder.append(cur)
            cur = cur.left

    # @return a boolean, whether we have a next smallest number
    def hasNext(self):
        if self.preOrder:
            return True
        return False

    # @return an integer, the next smallest number
    def next(self):
        if self.hasNext():
            cur = self.preOrder.pop()
            v = cur.val
            self.refresh(cur.right)
            return v


class BSTIterator_secondround:
    # @param root, a binary search tree's root node
    def __init__(self, root):
        self.stack = []
        self.refresh(root)

    def refresh(self,root):
        while root:
            self.stack.append(root)
            root = root.left

    # @return a boolean, whether we have a next smallest number
    def hasNext(self):
        return self.stack != []

    # @return an integer, the next smallest number
    def next(self):
        smallest = self.stack.pop()
        self.refresh(smallest.right)
        return smallest.val

# Your BSTIterator will be called like this:
# i, v = BSTIterator(root), []
# while i.hasNext(): v.append(i.next())