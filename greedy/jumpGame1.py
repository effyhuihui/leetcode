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

'''
用一个变量记录最大可到达的位置, 每次在这个位置之前找。
'''
class Solution_greedy2:
    # @param A, a list of integers
    # @return a boolean
    def canJump(self, A):
        l = len(A)
        canReach = 0
        for i in range(l):
            # if i > canReach, meaning it is impossible to reach from the beginning to
            # the current i, definitely can not jump
            if i <= canReach:
                #canReach = max of( previous max reach index, current reachable index)
                canReach = max(canReach, i + A[i])
                if canReach >= l - 1:
                    return True
        return False
x = Solution_greedy2()
print x.canJump([1,0,2])