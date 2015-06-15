__author__ = 'effy'
'''
Given a sorted array, remove the duplicates in place such that each element appear only once and return the new length.

Do not allocate extra space for another array, you must do this in place with constant memory.

For example,
Given input array nums = [1,1,2],

Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively.
It doesn't matter what you leave beyond the new length.
'''
class Solution_secondround:
    # @param {integer[]} nums
    # @return {integer}
    def removeDuplicates(self, nums):
        l = len(nums)
        start = 0
        duplicates = 0
        for i in range(l):
            if i > start and nums[i] == nums[start]:
                duplicates += 1
            else:
                nums[i-duplicates] = nums[i]
                start = i
        return l-duplicates


class Solution_3rd:
    # @param {integer[]} nums
    # @return {integer}
    def removeDuplicates(self, nums):
        prev = None
        l = len(nums)
        duplicate_count = 0
        for i in range(l):
            if nums[i] != prev:
                prev = nums[i]
                nums[i-duplicate_count] = nums[i]
            else:
                duplicate_count += 1
        return l-duplicate_count