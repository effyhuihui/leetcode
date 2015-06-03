__author__ = 'effy'
'''
Given an array of integers and an integer k, find out whether there there are two distinct indices i and j in the array
such that nums[i] = nums[j] and the difference between i and j is at most k.
'''
class Solution:
    # @param {integer[]} nums
    # @param {integer} k
    # @return {boolean}
    def containsNearbyDuplicate(self, nums, k):
        num_dict = {}
        l = len(nums)
        if l <=1:
            return False
        for i in range(l):
            if nums[i] in num_dict and i-num_dict[nums[i]] <=k:
                return True
            num_dict[nums[i]] = i
        return False
