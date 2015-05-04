__author__ = 'effy'
# -*- coding: utf-8 -*-
'''
The set [1,2,3,…,n] contains a total of n! unique permutations.

By listing and labeling all of the permutations in order,
We get the following sequence (ie, for n = 3):

"123"
"132"
"213"
"231"
"312"
"321"
Given n and k, return the kth permutation sequence.

Note: Given n will be between 1 and 9 inclusive.
'''
'''
TLE
'''
class Solution:
    # @param {integer} n
    # @param {integer} k
    # @return {string}
    def getPermutation(self, n, k):
        res = []
        def dfs(path,remain):
            if len(path) == n:
                res.append(path)
            else:
                l = len(remain)
                for i in range(l):
                    dfs(path+[remain[i]], remain[:i]+remain[i+1:])
        dfs([],[i for i in range(1,n+1)])
        return res[k-1]

x = Solution()
print x.getPermutation(3,3)

class Solution:
    def getPermutation(self, n, k):
        res = ''
        k -= 1
        fac = 1
        for i in range(1, n): fac *= i
        num = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        for i in reversed(range(n)):
            curr = num[k/fac]
            res += str(curr)
            num.remove(curr)
            if i !=0:
                k %= fac
                fac /= i
        return res
class Solution:
    # @return a string
   def getPermutation(self, n, k):
        nums = range(1, n+1)
        frac = 1
        for i in range(1, n):
            frac *= i
        res = []
        k = k - 1
        while 1:
            i, k = divmod(k, frac)
            res.append(nums[i])
            del nums[i]
            if len(nums) != 0:
                frac = frac / len(nums)
            else:
                break
        return ''.join([str(i) for i in res])



























