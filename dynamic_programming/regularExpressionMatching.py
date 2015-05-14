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
'''
TLE
'''
class Solution_recursion:
    # @return a boolean
    def isMatch(self, s, p):
        if len(p)==0:
            return len(s)==0
        if len(p)==1 or p[1]!='*':
            if len(s)==0 or (s[0]!=p[0] and p[0]!='.'):
                return False
            return self.isMatch(s[1:],p[1:])
        else:
            ## The opposite condition of 'if' is
            ## len(p) >=2 AND p[1] == '*'
            i=-1
            length=len(s)
            ## p[0]=='.' or p[0]==s[i] this means current s[i] matches p[0:2]'s requirement
            while i<length and (i<0 or p[0]=='.' or p[0]==s[i]):
                if self.isMatch(s[i+1:],p[2:]):
                    return True
                i+=1
            return False


class Solution_dp:
    def isMatch(self,s,p):
        l_s, l_p = len(s), len(p)
        ## dp[i][j] represent whether s[:i+1] and p[:j+1] can match
        ## i.e. whether substring s with length i from start matches
        ## substring p with length j from start
        dp = [[False for i in range(l_p+1)] for j in range(l_s+1)]
        ### border conditions, if s == '' and p=='', they matches
        dp[0][0] = True
        for i in range(1, l_p+1):
            ## Notice that '*' will not appear alone, it always appear in pair.
            ## So if current p[i-1] == '*', then dp[0][i] equals to dp[0][i-2],
            ## because 'x*' can match empty string!!!!!!!
            ## Also notice that dp[0][1] will always be False, because if p only have length of 1,
            ## it will only be a character or '.' both require one character in s
            if p[i-1] == '*':
                if i >=2:
                    dp[0][i] = dp[0][i-2]

        for i in range(1,l_s+1):
            for j in range(1,l_p+1):
                ## if current p is '.', then s[i-1] definitely matches p[j-1]
                ## so we only cares whether previous s[:i-1] matches p[:j-1], which is
                ## dp[i-1][j-1]. Pay attention that dp[i][j] is whether s[:i] matches p[:j]
                ## s[:i] is until s[i-1], p[:j] is until p[j-1]
                if p[j-1]=='.':
                    dp[i][j]=dp[i-1][j-1]
                ## if current p is '*' then if one of three conditions occurs, then it is True
                ## 1. dp[i][j-1] is True (meaning if * is one, it matches)
                ## 2. dp[i][j-2] is True (since * can always be 0)
                ## 3. dp[i-1][j] and (s[i-1]==p[j-2] or p[j-2]=='.') is True (meaning that only if
                #          until s[i-2] it matches p until current char, ALONG WITH a. s current char matches
                #          p char before '*'--which implies s[i-1]==s[i-2], * number plus one, OR p char
                #          before current '*' is '.' -- in this case '*' only uses once)
                elif p[j-1]=='*':
                    dp[i][j]=dp[i][j-1] or dp[i][j-2] or (dp[i-1][j] and (s[i-1]==p[j-2] or p[j-2]=='.'))
                ## if current p is regular character, then just matches the current one character
                else:
                    dp[i][j]=dp[i-1][j-1] and s[i-1]==p[j-1]
        return dp[l_s][l_p]



###############################
'''
reduced 2d memory to 1d
'''
class Solution_other_dp:
    # @return a boolean
    def isMatch(self, s, p):
        previousRow = [True]
        for i in range(0, len(p)):
            if p[i]=='*':
                previousRow.append(previousRow[i-1])
            else:
                previousRow.append(False)

        for letter in range(0,len(s)):
            actualRow = [False];
            for i in range(0, len(p)):
                if p[i]=='*':
                    temp = actualRow[i-1] or (previousRow[i+1] and (p[i-1]==s[letter] or p[i-1]=='.'))
                elif p[i] == '.':
                    temp = previousRow[i]
                else:
                    temp = previousRow[i] and p[i]==s[letter]
                actualRow.append(temp)
            previousRow = actualRow
        return previousRow[len(p)]























