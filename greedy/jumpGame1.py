# -*- coding: utf-8 -*-
__author__ = 'effy'
'''
Given an array of non-negative integers, you are initially positioned at the first index
of the array.

Each element in the array represents your maximum jump length at that position.

Determine if you are able to reach the last index.

For example:
A = [2,3,1,1,4], return true.

A = [3,2,1,0,4], return false.
'''

class Solution:
    # @param A, a list of integers
    # @return a boolean
    def canJump(self, A):
        l = len(A)
        cur = 0
        while cur < l-1:
            if A[cur] == 0:
                return False
            elif cur+A[cur] >= l-1:
                return True
            next_max_step =0
            print cur+1, cur+A[cur]+1
            for i in range(cur+1,min(l-1,cur+A[cur]+1)):
                if A[i] >= next_max_step:
                    next_max_step = A[i]
                    cur = i
            print cur
        if cur >= l-1:
            return True
        else:
            return False

class Solution_greedy1:
    # @param A, a list of integers
    # @return a boolean
    def canJump(self, A):
        step = A[0]
        for i in range(1, len(A)):
            if step > 0:
                step -= 1
                step = max(step, A[i])
            else:
                return False
        return True


class Solution_greedy2:
    # @param A, a list of integers
    # @return a boolean
    def canJump(self, A):
        l = len(A)
        canReach = 0
        for i in xrange(l):
            if i <= canReach:
                canReach = max(canReach, i + A[i])
                if canReach >= l - 1:
                    return True
        return False
x = Solution()
print x.canJump([1,0,2])