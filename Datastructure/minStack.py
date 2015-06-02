# -*- coding: utf-8 -*-
__author__ = 'effy'
'''
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
getMin() -- Retrieve the minimum element in the stack.
'''

'''
正常情况下top，pop和push操作都是常量时间的，所以maintain一个minStack来获取min。
Real stack        Min stack

5  --> TOP        1
4                 1
1                 1
3                 2
2                 2
但在leetcode提交的时候会产生memory limit exceeded的错误
'''
class MinStack:
    # @param x, an integer
    # @return an integer
    def __init__(self):
        self.minStack = []
        self.stack = []

    def push(self, x):
        self.stack.append(x)
        if not self.minStack:
            self.minStack.append(x)
        else:
            self.minStack.append(min(x,self.minStack[-1]))

    # @return nothing
    def pop(self):
        if self.stack:
            self.stack.pop()
            self.minStack.pop()

    # @return an integer
    def top(self):
        if self.stack:
            return self.stack[-1]
        else:
            return
    # @return an integer
    def getMin(self):
        if self.minStack:
            return self.minStack[-1]
        else:
            return

'''
Memory optimization:

优化： Min Stack 不必每次都存入，只需要存入最小值变化的状态。
Real stack        Min stack
1  --> TOP        1
5                 1
4                 2
1
3
2
所以每次pop或者push的时候要比较一下，
1.push时 if cur< = Min Stack Top 则MinStack 也要push
2.pop时  if Real Stack top == Min Stack top  则 Min Stack 也需要pop
注意：最小值可能会多次入栈的问题。
'''
class MinStack_opt:
    # @param x, an integer
    # @return an integer
    def __init__(self):
        self.minStack = []
        self.stack = []

    def push(self, x):
        self.stack.append(x)
        ## if x==self.minStack[-1] it must go inside minStack, because
        ## if only maintain once for minimum, pop operation will have problem
        if not self.minStack or x<=self.minStack[-1]:
            self.minStack.append(x)

    # @return nothing
    def pop(self):
        if self.stack:
            cur = self.stack.pop()
            if cur == self.minStack[-1]:
                self.minStack.pop()

    # @return an integer
    def top(self):
        if self.stack:
            return self.stack[-1]
        else:
            return
    # @return an integer
    def getMin(self):
        if self.minStack:
            return self.minStack[-1]
        else:
            return


class MinStack_secondround:
    # @param x, an integer
    # @return an integer
    def __init__(self):
        self.min_stack = []
        self.stack = []
    def push(self, x):
        self.stack.append(x)
        if not self.min_stack or x <= self.min_stack[-1]:
            self.min_stack.append(x)


    # @return nothing
    def pop(self):
        cur = self.stack.pop()
        if cur == self.min_stack[-1]:
            self.min_stack.pop()


    # @return an integer
    def top(self):
        return self.stack[-1]


    # @return an integer
    def getMin(self):
        return self.min_stack[-1]