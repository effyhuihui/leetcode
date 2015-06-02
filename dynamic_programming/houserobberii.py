__author__ = 'effy'
'''
Note: This is an extension of House Robber.

After robbing those houses on that street, the thief has found himself a new place for his thievery so that he will not
get too much attention. This time, all houses at this place are arranged in a circle.
That means the first house is the neighbor of the last one. Meanwhile, the security system for these houses remain the same as for those in the previous street.

Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of
money you can rob tonight without alerting the police.
'''
'''
use simple rob as helper method,
break the circle:
1. do not choose 0th house, start simplerob() form 1st house
2. choose 0th house,start simplerob() from the 2rd house

'''
class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def rob(self, nums):
        l = len(nums)
        if l == 0:
            return 0
        if l == 1:
            return nums[0]
        def simplerob(nums):
            l = len(nums)
            if l == 0:
                return 0
            max_profit = nums[0]
            prev_one, prev_two = max_profit,0
            for i in range(1,l):
                current_total = max(prev_two+nums[i], prev_one)
                max_profit = max(max_profit, current_total)
                prev_two= prev_one
                prev_one = current_total
            return max_profit
        return max(simplerob(nums[1:]), nums[0]+simplerob(nums[2:-1]))


