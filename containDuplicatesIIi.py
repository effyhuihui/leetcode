__author__ = 'effy'
'''
Given an array of integers, find out whether there are two distinct indices i and j in the array such that the
difference between nums[i] and nums[j] is at most t and the difference between i and j is at most k.
'''
class Solution:
    # @param {integer[]} nums
    # @param {integer} k
    # @param {integer} t
    # @return {boolean}
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        if k <= 0 or t < 0:
            return False
        numsDict = {}
        for i in range(len(nums)):
            bucket = nums[i]/(t+1)
            for key in [bucket-1, bucket, bucket+1]:
                if key in numsDict and abs(numsDict[key] - nums[i]) <= t:
                    return True
            numsDict[bucket] = nums[i]
            if i+1 > k:
                del numsDict[nums[i-k]/(t+1)]
        return False