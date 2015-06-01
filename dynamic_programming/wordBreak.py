__author__ = 'effy'
# -*- coding: utf-8 -*-
'''
Given a string s and a dictionary of words dict, determine if s can be segmented
into a space-separated sequence of one or more dictionary words.

For example, given
s = "leetcode",
dict = ["leet", "code"].

Return true because "leetcode" can be segmented as "leet code".
这道题考察的显然不是dfs，为什么？因为这道题不需要给出如何分割的答案，只需要判断是否可以分割为字典中的单词即可。我们考虑使用动态规划，
这个思路看代码的话不难，用python写起来也比较清晰。
'''
## 纯recursion会超时
class Solution_recursion:
    # @param s, a string
    # @param wordDict, a set<string>
    # @return a boolean
    def wordBreak(self, s, wordDict):
        if s == None:
            return True
        if s in wordDict:
            return True
        else:
            l = len(s)
            for i in range(l):
                if self.wordBreak(s[:i], wordDict) and self.wordBreak(s[i:], wordDict):
                    return True
            return False

class Solution_dp:
    # @param s, a string
    # @param wordDict, a set<string>
    # @return a boolean
    def wordBreak(self, s, wordDict):
        l = len(s)
        ## dp[i] represent s[0:i] is "word breakable"
        dp = [False for i in range(l+1)]
        dp[0] = True
        def helper(s,wordDict):
            l == len(s)
            if l == 0:
                return True
            for i in range(l):
                if dp[i] and s[i:] in wordDict:
                    return True
            return False
        for i in range(1,l+1):
            dp[i]=helper(s[:i], wordDict)
        return dp[-1]



class Solution_recursion_secondround:
    # @param s, a string
    # @param wordDict, a set<string>
    # @return a boolean
    def wordBreak(self, s, wordDict):
        if s == '':
            return True
        if s in wordDict:
            return True
        for i in range(1,len(s)+1):
            if s[:i] in wordDict:
                if self.wordBreak(s[i:], wordDict):
                    return True
        return False

class Solution_secondround:
    # @param s, a string
    # @param wordDict, a set<string>
    # @return a boolean
    def wordBreak(self, s, wordDict):
        dp = [False for i in range(len(s)+1)]
        dp[0] = True
        for i in range(1,len(s)+1):
            for j in range(i):
                if dp[j] and (s[j:i] in wordDict or s[j:i] == ''):
                    dp[i] = True
                    break
        return dp[-1]
x = Solution_dp()
print x.wordBreak("a",[])