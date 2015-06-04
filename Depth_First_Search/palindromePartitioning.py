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



class Solution_secondround:
    # @param s, a string
    # @return a list of lists of string
    def partition(self, s):
        res = []
        l = len(s)
        ## is_palindrome[i][j] represents from whether s[i:j+1] is a valid palindrom
        is_palindrome=[ [False for i in range(l)] for j in range(l)]
        for i in range(l):
            for j in range(i+1):
                is_palindrome[j][i] = s[i] == s[j] and ((i - j < 2 ) or is_palindrome[ j+ 1][i - 1])

        def dfs(index,path):
            print path, index
            if index == l:
                res.append(path)
            else:
                for i in range(index,l):
                    if is_palindrome[index][i]:
                        dfs(i+1, path+[s[index:i+1]])
        dfs(0,[])
        return res

x = Solution_dfs()
print x.partition("aab")






















