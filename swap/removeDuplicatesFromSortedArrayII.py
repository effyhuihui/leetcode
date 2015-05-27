__author__ = 'effy'
'''
Follow up for "Remove Duplicates":
What if duplicates are allowed at most twice?

For example,
Given sorted array nums = [1,1,1,2,2,3],

Your function should return length = 5, with the first five elements of nums being 1, 1, 2, 2 and 3.
It doesn't matter what you leave beyond the new length.
'''

class Solution_secondround:
    # @param {integer[]} nums
    # @return {integer}
    def removeDuplicates(self, nums):
        l = len(nums)
        prev = 0
        total_duplicates = 0
        local_duplicates = 0
        for i in range(l):
            if i > prev and nums[prev] == nums[i]:
                local_duplicates += 1
                if local_duplicates >=2:
                    total_duplicates += 1
                else:
                    nums[i-total_duplicates] = nums[i]
            else:
                local_duplicates = 0
                prev = i
                nums[i-total_duplicates] = nums[i]
        return l-total_duplicates