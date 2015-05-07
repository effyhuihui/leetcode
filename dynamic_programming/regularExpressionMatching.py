__author__ = 'effy'
# -*- coding: utf-8 -*-
'''
Implement regular expression matching with support for '.' and '*'.

'.' Matches any single character.
'*' Matches zero or more of the preceding element.

The matching should cover the entire input string (not partial).

The function prototype should be:
bool isMatch(const char *s, const char *p)

Some examples:
isMatch("aa","a") → false
isMatch("aa","aa") → true
isMatch("aaa","aa") → false
isMatch("aa", "a*") → true
isMatch("aa", ".*") → true
isMatch("ab", ".*") → true
isMatch("aab", "c*a*b") → true
'''
'''
正则表达式匹配的判断。网上很多的解法是用递归做的，用java和c++都可以过，但同样用python就TLE，说明这道题其实考察的不是递归。
而是动态规划，使用动态规划就可以AC了。这里的'*'号表示重复前面的字符，注意是可以重复0次的。

先来看递归的解法：

如果P[j+1]!='*':if S[i] == P[j]=>匹配下一位(i+1, j+1); elif S[i]!=P[j]=>匹配失败；

如果P[j+1]=='*':S[i]==P[j]=>匹配下一位(i+1, j+2)或者(i, j+2); elif S[i]!=P[j]=>匹配下一位(i,j+2)。

匹配成功的条件为S[i]=='\0' && P[j]=='\0'。


'''
class Solution_recursion:
    # @return a boolean
    def isMatch(self, s, p):
        len_s,len_p = len(s), len(p)
        def dfs(i,j):
            if i == len_s:
                return j == len_p
            if p[j] != "." and p[j] != "*":
               if s[i] != p[j]:
                   return False
               else:
                   dfs(i+1,j+1)
            elif p[j] == ".":
                if j+1 == len_p or p[j+1] != "*":
                    dfs(i+1,j+1)
                else:
                    pass

class Solution:
    # @return a boolean
    def isMatch(self, s, p):
        if len(p)==0:
            return len(s)==0
        if len(p)==1 or p[1]!='*':
            if len(s)==0 or (s[0]!=p[0] and p[0]!='.'):
                return False
            return self.isMatch(s[1:],p[1:])
        else:
            i=-1
            length=len(s)
            while i<length and (i<0 or p[0]=='.' or p[0]==s[i]):
                if self.isMatch(s[i+1:],p[2:]):
                    return True
                i+=1
            return False




class Solution:
    # @return a boolean
    def isMatch(self, s, p):
        dp = {}
        def dfs(i, j):
            if (i,j) in dp:
                return dp[(i,j)]
            if j == len(p):
                return i == len(s)

            if j < len(p)-1 and p[j+1] == '*':
                if dfs(i, j+2):
                    dp[(i,j)] = True
                    return True
                for k in range(i, len(s)):
                    if s[k] == p[j] or p[j] == '.':
                        if dfs(k+1, j+2):
                            dp[(i,j)] = True
                            return True
                    else:
                        break
            elif i < len(s) and (s[i] == p[j] or p[j] == '.'):
                return dfs(i+1, j+1)

            dp[(i,j)] = False
            return False

        return dfs(0, 0)























