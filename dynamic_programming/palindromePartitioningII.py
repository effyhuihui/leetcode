__author__ = 'effy'
# -*- coding: utf-8 -*-
'''
Given a string s, partition s such that every substring of the partition is a palindrome.

Return the minimum cuts needed for a palindrome partitioning of s.

For example, given s = "aab",
Return 1 since the palindrome partitioning ["aa","b"] could be produced using 1 cut.

由于这次不需要穷举出所有符合条件的回文分割，而是需要找到一个字符串s回文分割的最少分割次数，分割出来的字符串都是回文字符串。
求次数的问题，不需要dfs，用了也会超时，之前的文章说过，求次数要考虑动态规划（dp）。对于程序的说明：
p[i][j]表示从字符i到j(相当于s[i:j+1])是否为一个回文字符串。dp[i]表示s[i:]在最少的分割次数下，有多少个回文字符串，即分割次数+1。

对于 p[i][j] 状态转移方程是：
p[i][j] = (p[i+1][j-1] and s[i] == s[j]) or (s[i] == s[j] and j-i<2)
'''
class Solution_online:
    # @param s, a string
    # @return an integer
    # @dfs time out
    # @dp is how many palindromes in the word
    def minCut(self, s):
        dp = [0 for i in range(len(s)+1)]
        p = [[False for i in range(len(s))] for j in range(len(s))]
        for i in range(len(s)+1):
            dp[i] = len(s) - i
        for i in range(len(s)-1, -1, -1):
            for j in range(i, len(s)):
                ##假设从i开始向后分割， 从i开始向后找j，如果p[i][j] 是一个palindrome，那么以i到j为第一个分割的字符的话
                ## 此时的最小分割数量就是d[j+1]+1，遍历所有可能的j，找出最小的次数就是dp[i]
                if s[i] == s[j] and (((j - i) < 2) or p[i+1][j-1]):
                    p[i][j] = True
                    dp[i] = min(1+dp[j+1], dp[i])
        return dp[0]-1

class Solution_linlin:
    # @param s, a string
    # @return an integer
    def minCut(self, s):
        if s == '':
            return 0
        n = len(s)
        cuts = range(n)
        par = [[False]*n for i in range(n)]
        for i in range(n):
            par[i][i] = True

        for i in range(len(s)):
            for j in range(i+1):
                if s[j] == s[i]:
                    if j == i-1 or (j+1 <= i-1 and par[j+1][i-1]):
                        par[j][i] = True
                if par[j][i]:
                    if j == 0:
                        cuts[i] = 0
                        break
                    cuts[i] = min(cuts[i], cuts[j-1]+1)

        return cuts[-1]



class Solution_mine:
    # @param s, a string
    # @return an integer
    def minCut(self, s):
        l = len(s)
        ## cuts[i] 表示前i个字符最小有几个cuts
        cuts = [i for i in range(l+1)]
        ## isPalindrome[i][j] is whether s[i:j+1] is palindrome
        isPalindrom = [[False for i in range(l)] for j in range(l)]
        ## set restriction conditions
        for i in range(l):
            isPalindrom[i][i] = True

        for i in range(l):
            for j in range(0,i+1):
                ## if s[j:i+1] is palindrome, then if cut s[j:i+1], then local min is
                ## cuts[j]+1
                if s[i] == s[j] and  (i-j<2 or isPalindrom[j+1][i-1]):
                    isPalindrom[j][i] = True
                    cuts[i+1] = min(cuts[i+1], 1+cuts[j])
        return cuts[-1]-1
x = Solution_mine()
print x.minCut("a")




