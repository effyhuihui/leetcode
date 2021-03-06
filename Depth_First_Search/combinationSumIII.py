__author__ = 'effy'
'''
Find all possible combinations of k numbers that add up to a number n, given that only numbers from 1 to 9 can
be used and each combination should be a unique set of numbers.

Ensure that numbers within the set are sorted in ascending order.


Example 1:

Input: k = 3, n = 7

Output:

[[1,2,4]]

Example 2:

Input: k = 3, n = 9

Output:

[[1,2,6], [1,3,5], [2,3,4]]
'''
class Solution:
    # @param {integer} k
    # @param {integer} n
    # @return {integer[][]}
    def combinationSum3(self, k, n):
        res = []
        def dfs(k,n, index,path):
            if k == 0:
                if n == 0:
                    res.append(path)
            elif n<index:
                return
            else:
                for i in range(index,10):
                    if i<=n:
                        dfs(k-1, n-i,i+1,path+[i])
        dfs(k,n,1,[])
        return res

x = Solution()
print x.combinationSum3(3,9)




