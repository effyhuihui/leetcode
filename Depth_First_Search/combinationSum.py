__author__ = 'effy'
# -*= coding: utf-8 -*-
'''
Given a set of candidate numbers (C) and a target number (T), find all unique combinations in C where the candidate
numbers sums to T.

The same repeated number may be chosen from C unlimited number of times.

Note:
All numbers (including target) will be positive integers.
Elements in a combination (a1, a2, … , ak) must be in non-descending order. (ie, a1 ≤ a2 ≤ … ≤ ak).
The solution set must not contain duplicate combinations.
For example, given candidate set 2,3,6,7 and target 7,
A solution set is:
[7]
[2, 2, 3]
'''
class Solution:
    # @param {integer[]} candidates
    # @param {integer} target
    # @return {integer[][]}
    def combinationSum(self, candidates, target):
        l = len(candidates)
        res = []
        def dfs(path,index,remain):
            if remain == 0:
                res.append(path)
            else:
                for i in range(index,l):
                    val = candidates[i]
                    if val<=remain:
                        dfs(path+[val],i,remain-val)
        candidates.sort()
        dfs([],0,target)
        return res


class Solution_secondround:
    # @param {integer[]} candidates
    # @param {integer} target
    # @return {integer[][]}
    def combinationSum(self, candidates, target):
        candidates.sort()
        l = len(candidates)
        res = []
        def dfs(index,remain,path):
            if remain == 0:
                res.append(path)
            else:
                for i in range(index,l):
                    val = candidates[i]
                    if  val<=remain:
                        dfs(i, remain-val, path+[val])
        dfs(0,target,[])
        return res