__author__ = 'effy'
# -*- coding: utf-8 -*-
'''
Find the contiguous subarray within an array (containing at least one number) which has the largest product.

For example, given the array [2,3,-2,4],
the contiguous subarray [2,3] has the largest product = 6.
因为input全部是integer，所以要是全部是正数的话只要一直乘到底就好，可是这里有一个可能为负数的情况，
而两个负数负负得正又变成更大的正数，所以要maintain两个var 一个是posMax 一个是negMax，in case min max会互相转换。
注意这里其实是一个dp的问题，dp[i]表示从0到第i个index的subarray里，最大的maximal，这里用的negMax和posMax都是辅助变量，
分别表示“到index为i为止并且连续乘上nums[i]”的最大负数和最大正数。
'''

class Solution:
    # @param A, a list of integers
    # @return an integer
    def maxProduct(self, A):
        if len(A) == 1:
            return
        posMax, negMax, maximal = 0, 0, 0
        for a in A:
            if a < 0:
                posMax, negMax = negMax, posMax
            ## see?? below, the definiteion of posMax and negMax ensures that either one has current
            ## a as part of it 所以肯定是连续的
            posMax = max(a, posMax*a)
            negMax = min(a, negMax*a)
            maximal = max(maximal, posMax)
        return maximal

class Solution_secondround:
    # @param {integer[]} nums
    # @return {integer}
    def maxProduct(self, nums):
        if len(nums) == 0:
            return
        if len(nums) == 1:
            return nums[0]
        negMax, posMax,maxProd = 0,0,0
        for i in nums:
            if i<0:
                negMax,posMax = posMax,negMax
            negMax = min(i, negMax*i)
            posMax = max(i, posMax*i)
            maxProd = max(maxProd,posMax)
        return maxProd



class Solution_3rd:
    # @param {integer[]} nums
    # @return {integer}
    def maxProduct(self, nums):
        if len(nums) == 0:
            return
        if len(nums) == 1:
            return nums[0]
        negMax, posMax = 0, 0
        global_max = 0
        for i in nums:
            if i < 0:
                negMax, posMax = posMax, negMax
            negMax = min(negMax*i, i)
            posMax = max(posMax*i, i)
            global_max = max(global_max, posMax)
        return global_max

x = Solution()
print x.maxProduct([-4,-3,-2])




















