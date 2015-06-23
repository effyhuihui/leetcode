__author__ = 'effy'
'''
Given a string s and a dictionary of words dict, add spaces in s to construct a sentence where each word is a
valid dictionary word.

Return all such possible sentences.

For example, given
s = "catsanddog",
dict = ["cat", "cats", "and", "sand", "dog"].

A solution is ["cats and dog", "cat sand dog"].
'''
'''
pure dfs will cause TLE
'''
class Solution_dfs:
    # @param s, a string
    # @param wordDict, a set<string>
    # @return a string[]
    def wordBreak(self, s, wordDict):
        res = []
        def dfs(substring, path):
            l = len(substring)
            for i in range(1,l+1):
                if substring[:i] in wordDict:
                    dfs(substring[i:], path+ " " +substring[:i])
        dfs(s, '')
        return res

#x = Solution_dfs()
#print x.wordBreak("catsanddog", ["cat", "cats", "and", "sand", "dog"])
'''
dp[i][j] represent whether s[i:j] is in wordDict
The concept is wrong, why? becasue it is not making too much difference if only reduce the time of checking a word
in dict, this is not the bottle neck

'''
class Solution_dp:
    # @param s, a string
    # @param wordDict, a set<string>
    # @return a string[]
    def wordBreak(self, s, wordDict):
        res = []
        l = len(s)
        ## dp[i] represent whether s[i:] os word breakable. the reason why to maintain this is becasue
        ## if s[:i] is in wordDict, then first check dp[i], if it is False, then skip.
        dp = [False for i in range(l+1)]
        dp[l] = True
        for i in range(l-1,-1,-1):
            for j in range(l,i,-1):
                if dp[j] and s[i:j] in wordDict:
                    dp[i] = True
                    break
        def dfs(i,path):
            if dp[i]:
                if i>=l:
                    res.append(path.lstrip())
                else:
                    for j in range(i+1,l+1):
                        if s[i:j] in wordDict:
                            dfs(j,path+" "+s[i:j])
        dfs(0,'')
        return res

class Solution_secondround:
    # @param s, a string
    # @param wordDict, a set<string>
    # @return a string[]
    def wordBreak(self, s, wordDict):
        dp = [[] for i in range(len(s)+1)]
        for i in range(1,len(s)+1):
            for j in range(i):
                if s[j:i] in wordDict and (j ==0 or s[j] !=[]):
                    if j != 0:
                        dp[i]+= [word + ' '+s[j:i] for word in dp[j]]
                    else:
                        dp[i]+=[s[j:i]]
        return dp[-1]

x = Solution_secondround()
print x.wordBreak("catsanddog", ["cat", "cats", "and", "sand", "dog"])
print x.wordBreak("aaaaaaa", ["aaaa","aa","a"])
print x.wordBreak("ab", ["a", "b"])