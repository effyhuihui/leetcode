__author__ = 'effy'
# -*- coding:utf-8 -*-
'''
Implement wildcard pattern matching with support for '?' and '*'.

'?' Matches any single character.
'*' Matches any sequence of characters, '*' is not times any more, and need not to appear in pair
 (including the empty sequence, i.e. * = asd, * = '').

The matching should cover the entire input string (not partial).

The function prototype should be:
bool isMatch(const char *s, const char *p)

Some examples:
isMatch("aa","a") → false
isMatch("aa","aa") → true
isMatch("aaa","aa") → false
isMatch("aa", "*") → true
isMatch("aa", "a*") → true
isMatch("ab", "?*") → true
isMatch("aab", "c*a*b") → false
'''

class Solution_dp:
    # @param s, an input string
    # @param p, a pattern string
    # @return a boolean
    def isMatch(self, s, p):
        m,n = len(s), len(p)
        dp = [ [False for i in range(n+1)] for j in range(m+1)]
        dp[0][0] = True
        for i in range(1,n+1):
            dp[0][i] = dp[0][i-1] and p[i-1] =='*'

        for i in range(1,m+1):
            for j in range(1,n+1):
                if p[j-1] != '*':
                    dp[i][j] = dp[i-1][j-1] and (p[j-1] == s[i-1] or p[j-1]=='?')
                else:
                    '''
                    * matches empty or the last char in s
                    '''
                    dp[i][j] = dp[i-1][j] or dp[i][j-1]
        return dp[-1][-1]


class Solution_recursion:
    # @return a boolean
    def isMatch(self, s, p):
        if not p or not s:
            return not s and not p
        if p[0] != '*':
            if p[0] == s[0] or p[0] == '?':
                return self.isMatch(s[1:], p[1:])
            else:
                return False
        else:
            i = 0
            while i<=len(s):
                if self.isMatch(s[i:], p[1:]):
                    return True
                i+=1
            return False


class Solution_recur_3rd:
    def isMatch(self, s, p):
        if len(s) == 0:
            return len(p) == 0 or (len(p) == 1 and p[0]=='*')
        if len(p) == 0:
            return False
        else:
            if p[0] == '?' or (p[0] == s[0]):
                return self.isMatch(s[1:], p[1:])
            elif p[0] == '*':
                for i in range(len(s)+1):
                    if self.isMatch(s[:i],p[1:]):
                        return True
                return  False
            else:
                return False


class Solution_dp_3rd:
    def isMatch(self, s, p):
        m,n = len(s), len(p)
        dp = [ [False for i in range(n+1)] for j in range(m+1)]
        dp[0][0] = True
        for i in range(1,n+1):
            dp[0][i] = dp[0][i-1] and p[i-1] =='*'
        for i in range(1,m+1):
            for j in range(1,n+1):
                if p[n-1] != '*':
                    dp[i][j] = (p[n-1] == '?' or s[m-1] == p[n-1]) and  dp[i-1][j-1]
                else:
                    dp[i][j] =dp[i-1][j-1] or dp[i][j-1]
        return dp[-1][-1]

