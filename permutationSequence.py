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
'''
其实本题数据不大，n最多为9，9! = 362880，枚举应该能够通过（我没试验）。



我采用的方法是计算第k个Permutation。

假设n = 6，k = 400

先计算第一位，

第一位为6，那么它最少也是第5! * 5 + 1个排列，这是因为第一位为1/2/3/4/5时，都有5!个排列，
因此第一位为6时，至少是第5! * 5 + 1个排列（这个排列为612345）。

5! * 5 + 1 = 601 > k，所以第一位不可能是6.

一个一个地枚举，直到第一位为4时才行，这时，4xxxxx至少为第5! * 3 + 1 = 361个排列。



然后计算第二位，

与计算第一位时的区别在于，46xxxx至少为第4! * 4 + 1 = 97个排列，这是因为比6小的只有5/3/2/1了。

最后可以计算出第二位为2。
'''
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



























