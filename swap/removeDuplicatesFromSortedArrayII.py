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

class Solution_3rd:
    # @param {integer[]} nums
    # @return {integer}
    def removeDuplicates(self, nums):
        prev = None
        l = len(nums)
        total_duplicates_count = 0
        local_occur = 1
        for i in range(l):
            if prev != nums[i]:
                local_occur = 1
                prev = nums[i]
            else:
                local_occur += 1
                if local_occur > 2:
                    total_duplicates_count += 1
            nums[i-total_duplicates_count] = nums[i]
        return l-total_duplicates_count
x = Solution_3rd()
print x.removeDuplicates([1,1,1,2,2,3,3,3,4,5,5,6,7,7,7])

