__author__ = 'effy'
'''
Given a collection of numbers, return all possible permutations.

For example,
[1,2,3] have the following permutations:
[1,2,3], [1,3,2], [2,1,3], [2,3,1], [3,1,2], and [3,2,1].
'''
class Solution:
    # @param {integer[]} nums
    # @return {integer[][]}
    def permute(self, nums):
        res = []
        def dfs(num,path):
            l = len(num)
            if l == 0:
                res.append(path)
            else:
                for i in range(l):
                    dfs(num[:i]+num[i+1:], path+[num[i]])
        dfs(nums,[])
        return res


class Solution_secondround:
    # @param {integer[]} nums
    # @return {integer[][]}
    def permute(self, nums):
        res = []
        def dfs(path, cadidates):
            if not cadidates:
                res.append(path)
            else:
                for i in range(len(cadidates)):
                    dfs(path+[cadidates[i]], cadidates[:i]+cadidates[i+1:])
        dfs([], nums)
        return res

x = Solution()
print x.permute([1,2,3])