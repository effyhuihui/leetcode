__author__ = 'effy'
'''
Given a set of distinct integers, nums, return all possible subsets.

Note:
Elements in a subset must be in non-descending order.
The solution set must not contain duplicate subsets.
For example,
If nums = [1,2,3], a solution is:

[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]
'''
class Solution:
    # @param {integer[]} nums
    # @return {integer[][]}
    def subsets(self, nums):
        nums.sort()
        res = []
        def dfs(path,remain):
            res.append(path)
            l = len(remain)
            for i in range(l):
                dfs(path+[remain[i]], remain[i+1:])
        dfs([],nums)
        return res


class Solution_secondround:
    # @param {integer[]} nums
    # @return {integer[][]}
    def subsets(self, nums):
        res = []
        l = len(nums)
        nums.sort()
        def dfs(index,path):
            res.append(path)
            for i in range(index,l):
                dfs(i+1,path+[nums[i]])
        dfs(0,[])
        return res

x = Solution()
print x.subsets([1,2,3])






























