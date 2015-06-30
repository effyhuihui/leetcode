__author__ = 'effy'
# -*- coding: utf-8 -*-
'''
Find the kth largest element in an unsorted array. Note that it is the kth largest element in the sorted order, not the kth distinct element.

For example,
Given [3,2,1,5,6,4] and k = 2, return 5.

Note:
You may assume k is always valid, 1 ≤ k ≤ array's length.
'''

class Solution:
    # @param {integer[]} nums
    # @param {integer} k
    # @return {integer}
    def findKthLargest(self, nums, k):
        l = len(nums)
        if l < k:
            return None
        pivot = nums[l/2]
        leftsub, rightsub = [], []
        for i in range(l):
            if i != l/2:
                if nums[i] < pivot:
                    leftsub.append(nums[i])
                else:
                    rightsub.append(nums[i])

        if len(rightsub) == k-1:
            return pivot
        elif len(rightsub) >=k:
            return self.findKthLargest(rightsub,k)
        else:
            return self.findKthLargest(leftsub,k-len(rightsub)-1)