__author__ = 'effy'
'''
Given a string s, partition s such that every substring of the partition is a palindrome.

Return all possible palindrome partitioning of s.

For example, given s = "aab",
Return

  [
    ["aa","b"],
    ["a","a","b"]
  ]

all combinations, use dfs
'''



class Solution_dfs:
    # @param s, a string
    # @return a list of lists of string
    def partition(self, s):
        res = []
        def isPalindrome(s):
            l = len(s)
            for i in range(l//2):
                if s[i] != s[l-i-1]:
                    return False
            return True
        def dfs(s, path):
            if not s:
                res.append(path)
            else:
                l = len(s)
                for i in range(l):
                    if isPalindrome(s[:i+1]):
                        dfs(s[i+1:], path+[s[:i+1]])
        dfs(s,[])
        return res

x = Solution_dfs()
print x.partition("aab")






















