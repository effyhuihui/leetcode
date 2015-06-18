__author__ = 'effy'
class Solution:
    def longestPalindrome(self, s):
        l = len(s)
        def helper(start,end):
            while start>=0 and end<l and s[start] == s[end]:
                start-=1
                end+=1
            return s[start+1:end]
        longest = ''
        for i in range(l):
            odd,even = helper(i,i), helper(i,i+1)
            if max(len(odd), len(even)) > len(longest):
                if len(odd)>len(even):
                    longest = odd
                else:
                    longest = even
        return longest


class Solution_TLE:
    # @param {string} s
    # @return {string}
    def longestPalindrome(self, s):
        l = len(s)
        ispalindrom = [ [False for i in range(l)] for j in range(l)]
        maxlen = 1
        for i in range(l):
            for j in range(i+1):
                if (i-j<2 or ispalindrom[j+1][i-1]) and s[i] == s[j]:
                    ispalindrom[j][i] = True
                    maxlen = max(maxlen,i-j+1)
        return maxlen