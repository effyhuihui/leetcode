__author__ = 'effy'
# -*- coding: utf-8
'''
Now instead of outputting all the combinations,return how many
distinct solution does it have
虽然这里说只要找到有几组unique的解就好，但是不能用dp，为什么呢？因为dp[i]不仅仅
与dp[i-1]有关，还与i-1具体的解有关
'''
class Solution:
    # @param {integer} n
    # @return {integer}
    def totalNQueens(self, n):
        res = []
        def check(k,j,path):
            for i in range(k):
                if path[i] == j or abs(k-i) == abs(path[i]-j):
                    return False
            return True
        def dfs(path):
            l = len(path)
            if l == n:
                res.append(path)
            else:
                for i in range(n):
                    if check(l,i,path):
                        dfs(path+[i])
        dfs([])
        return len(res)
