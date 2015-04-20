__author__ = 'effy'
# -*- coding: utf-8 -*-
'''
Given s1, s2, s3, find whether s3 is formed by the interleaving of s1 and s2.

For example,
Given:
s1 = "aabcc",
s2 = "dbbca",

When s3 = "aadbbcbcac", return true.
When s3 = "aadbbbaccc", return false.
'''
'''
dp[i][j]表示s1[0...i-1]和s2[0...j-1]是否可以拼接为s3[0...i+j-1]，可以拼接为true，不可以拼接为false。
状态转移方程为:
dp[i][j] = (dp[i-1][j] and s1[i-1] == s3[i+j-1]) or (dp[i][j-1] and s2[j-1] == s3[i+j-1])
'''
class Solution:
    # @param s1, a string
    # @param s2, a string
    # @param s3, a string
    # @return a boolean
    def isInterleave(self, s1, s2, s3):
        l_s1, l_s2, l_s3 = len(s1),len(s2), len(s3)
        if l_s1+l_s2 != l_s3:
            return False
        char_total, char_s3 = sorted(list(s1)+list(s2)), sorted(list(s3))
        if char_s3 != char_total:
            return False
        dp = [[False for i in range(l_s1+1)] for j in range(l_s2+1)]
        dp[0][0] = True
        for i in range(1,l_s1+1):
            dp[0][i] = dp[0][i-1] and s1[i-1] == s3[i-1]
        for i in range(1,l_s2+1):
            dp[i][0] = dp[i-1][0] and s2[i-1] == s3[i-1]

        for i in range(1, l_s2+1):
            for j in range(1, l_s1+1):
                dp[i][j] = (dp[i-1][j] and s2[i-1] == s3[i+j-1]) or (dp[i][j-1] and s1[j-1] == s3[i+j-1])
        return dp[-1][-1]


x = Solution()
print x.isInterleave("aabcc", "dbbca", "aadbbbaccc")























