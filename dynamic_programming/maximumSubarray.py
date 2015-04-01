# -*- coding: utf-8 -*-
__author__ = 'effy'
'''
Find the contiguous subarray within an array (containing at least one number)
which has the largest sum.

For example, given the array [−2,1,−3,4,−1,2,1,−5,4],
the contiguous subarray [4,−1,2,1] has the largest sum = 6.
'''
class Solution:
    # @param A, a list of integers
    # @return an integer
    def maxSubArray(self, A):
        max = -float("inf")
        current_sum = 0
        for i in range(len(A)):
            if current_sum < 0:
                current_sum = 0
            current_sum += A[i]
            if current_sum > max:
                max = current_sum
        return max
x = Solution()
print x.maxSubArray([-2])