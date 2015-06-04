__author__ = 'effy'
'''
Given two integers n and k, return all possible combinations of k numbers out of
1 ... n.

For example,
If n = 4 and k = 2, a solution is:

[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]
'''
class Solution:
    # @return a list of lists of integers
    def combine(self, n, k):
        def dfs(path,index):
            if len(path) == k:
                res.append(path)
            for i in range(index, n+1):
                dfs(path+[i], i+1)
        res = []
        dfs([],1)
        return res


class Solution_secondround:
    # @param {integer} n
    # @param {integer} k
    # @return {integer[][]}
    def combine(self, n, k):
        res = []
        def dfs(index,path):
            if len(path) == k:
                res.append(path)
            else:
                for i in range(index,n+1):
                    dfs(i+1, path+[i])
        dfs(1, [])
        return res


x = Solution()
print x.combine(4,2)
