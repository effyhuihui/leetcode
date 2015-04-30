__author__ = 'effy'
'''
Given a collection of numbers that might contain duplicates, return all possible unique permutations.

For example,
[1,1,2] have the following unique permutations:
[1,1,2], [1,2,1], and [2,1,1].
'''
class Solution:
    # @param {integer[]} nums
    # @return {integer[][]}
    def permuteUnique(self, nums):
        res = []
        l = len(nums)
        nums.sort()
        def dfs(path, list):
            if l == len(path):
                res.append(path)
            else:
                prev = None
                for i in range(len(list)):
                    if list[i] != prev:
                        dfs(path+[list[i]], list[:i]+list[i+1:])
                        prev = list[i]
        dfs([],nums)
        return res
x = Solution()
print x.permuteUnique([1,1,2])