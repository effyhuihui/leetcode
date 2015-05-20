__author__ = 'effy'
# -*- coding: utf-8 -*-
'''
Given a sorted array and a target value, return the index if the target is found. If not, return the index where
it would be if it were inserted in order.

You may assume no duplicates in the array.

Here are few examples.
[1,3,5,6], 5 → 2
[1,3,5,6], 2 → 1
[1,3,5,6], 7 → 4
[1,3,5,6], 0 → 0
'''

class Solution:
    # @param A, a list of integers
    # @param target, an integer to be inserted
    # @return integer
    def searchInsert(self, A, target):
        n = len(A)
        if n == 1:
            if target > A[0]: return 1
            else: return 0
        start = 0
        end = n-1
        mid = (start+end)/2
        while start < end:
            if A[mid] == target:
                return mid
            elif A[mid] > target:
                end = max(0,mid-1)
            else:
                start = min(n-1,mid+1)
            mid = (start+end)/2
        if A[mid] >= target:
            return mid
        else :
            return mid+1


class Solution_secondround:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer}
    def searchInsert(self, nums, target):
        start, end = 0, len(nums)-1
        while start<=end:
            mid = (start+end)/2
            if nums[mid] == target:
                return mid
            if nums[mid] < target:
                start = mid +1
            else:
                end = mid -1
        if nums[mid]>target:
            return mid
        else:
            return mid+1

a = Solution()
print a.searchInsert([1,3],3)