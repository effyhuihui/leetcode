__author__ = 'effy'
'''
Given a collection of integers that might contain duplicates, nums, return all possible subsets.

Note:
Elements in a subset must be in non-descending order.
The solution set must not contain duplicate subsets.
For example,
If nums = [1,2,2], a solution is:

[
  [2],
  [1],
  [1,2,2],
  [2,2],
  [1,2],
  []
]
'''
class Solution:
    # @param {integer[]} nums
    # @return {integer[][]}
    def subsetsWithDup(self, nums):
        nums.sort()
        res = []
        def dfs(path,remain):
            res.append(path)
            prev = None
            l = len(remain)
            for i in range(l):
                if remain[i] != prev:
                    dfs(path+[remain[i]], remain[i+1:])
                    prev = remain[i]
        dfs([],nums)
        return res


class Solution_secondround:
    # @param {integer[]} nums
    # @return {integer[][]}
    def subsetsWithDup(self, nums):
        nums.sort()
        res = []
        l = len(nums)
        def dfs(index,path):
            res.append(path)
            prev = None
            for i in range(index,l):
                cur = nums[i]
                if cur != prev:
                    dfs(i+1, path+[cur])
                    prev = cur
        dfs(0,[])
        return res


x = Solution()
print x.subsetsWithDup([1,2,2])

























