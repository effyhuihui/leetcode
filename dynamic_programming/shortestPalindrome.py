__author__ = 'effy'
'''
Given a string S, you are allowed to convert it to a palindrome by adding characters in front of it.
Find and return the shortest palindrome you can find by performing this transformation.

For example:

Given "aacecaaa", return "aaacecaaa".

Given "abcd", return "dcbabcd".

'''
class Solution:
    # @param {string} s
    # @return {string}
    def shortestPalindrome(self, s):
        l=len(s)
        A = s[::-1]+s
        isPalindrome = [ [False for i in range(2*l)] for j in range(2*l)]
        for i in range(2*l):
            for j in range(i+1):
                if A[i] == A[j] and (i-j<2 or isPalindrome[j+1][i-1]):
                    isPalindrome[j][i] = True
        i = l
        while i >=0:
            print isPalindrome[i][2*l-1]
            if isPalindrome[i][2*l-1]:
                break
            i -= 1
        return A[i:]

x = Solution()
#print x.shortestPalindrome('a')