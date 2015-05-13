__author__ = 'effy'
# -*- coding: utf-8
'''
Given an array of n positive integers and a positive integer s, find the minimal length of a subarray of which the
sum ≥ s. If there isn't one, return 0 instead.

For example, given the array [2,3,1,2,4,3] and s = 7,
the subarray [4,3] has the minimal length under the problem constraint.

typical usage of two pointers!! 左边缩起来，右边伸出去
'''
class Solution:
    # @param {integer} s
    # @param {integer[]} nums
    # @return {integer}
    def minSubArrayLen(self, s, nums):
        if  sum(nums)<s:
            return 0
        l = len(nums)
        min_len = l
        i,j =0,0
        while i<l and j<l:
            cur_sum = sum(nums[i:j+1])
            while cur_sum>=s and i<=j:
                if j-i+1 < min_len:
                    min_len = j-i+1
                i += 1
                cur_sum = sum(nums[i:j+1])
            j+=1
        return min_len
x = Solution()
print x.minSubArrayLen(100,[])
print x.minSubArrayLen(7,[2,3,1,2,4,3])


