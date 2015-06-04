__author__ = 'effy'
# -*- coding: utf-8 -*-
'''
Given a collection of candidate numbers (C) and a target number (T), find all unique combinations in C
where the candidate numbers sums to T.

Each number in C may only be used once in the combination.

Note:
All numbers (including target) will be positive integers.
Elements in a combination (a1, a2, … , ak) must be in non-descending order. (ie, a1 ≤ a2 ≤ … ≤ ak).
The solution set must not contain duplicate combinations.
For example, given candidate set 10,1,2,7,6,1,5 and target 8,
A solution set is:
[1, 7]
[1, 2, 5]
[2, 6]
[1, 1, 6]
'''
'''
below is very similar to combination sum I, however, it will result in duplication
'''
class Solution_wrong:
    # @param {integer[]} candidates
    # @param {integer} target
    # @return {integer[][]}
    def combinationSum2(self, candidates, target):
        res = []
        l = len(candidates)
        candidates.sort()
        def dfs(path,index,remain):
            if remain == 0:
                res.append(path)
            else:
                for i in range(index,l):
                    val = candidates[i]
                    if val <= remain:
                        dfs(path+[val], i+1, remain-val)
        dfs([],0,target)
        return res

x = Solution_wrong()
print x.combinationSum2([10,1,2,7,6,1,5], 8)

'''
注意在dfs的else block里面加了一个判断，在每同一个level的dfs recall前，检查一下这次加入path的元素是不是和上一次加入过的相同，
要是相同的话就跳过，这样就防止了重复
'''
class Solution:
    # @param {integer[]} candidates
    # @param {integer} target
    # @return {integer[][]}
    def combinationSum2(self, candidates, target):
        res = []
        l = len(candidates)
        candidates.sort()
        def dfs(path,index,remain):
            if remain == 0:
                res.append(path)
            else:
                prev = None
                for i in range(index,l):
                    val = candidates[i]
                    if val <= remain and val != prev:
                        dfs(path+[val], i+1, remain-val)
                        prev = val

        dfs([],0,target)
        return res



class Solution_secondround:
    # @param {integer[]} candidates
    # @param {integer} target
    # @return {integer[][]}
    def combinationSum2(self, candidates, target):
        candidates.sort()
        l = len(candidates)
        res = []
        def dfs(index,remain,path):
            if remain == 0:
                res.append(path)
            else:
                prev = None
                for i in range(index,l):
                    val = candidates[i]
                    if val != prev and val<=remain:
                        dfs(i+1, remain-val, path+[val])
                        prev = val
        dfs(0,target,[])

x = Solution()
print x.combinationSum2([10,1,2,7,6,1,5], 8)