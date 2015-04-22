__author__ = 'effy'
'''
A message containing letters from A-Z is being encoded to numbers using the following mapping:

'A' -> 1
'B' -> 2
...
'Z' -> 26
Given an encoded message containing digits, determine the total number of ways to decode it.

For example,
Given encoded message "12", it could be decoded as "AB" (1 2) or "L" (12).

The number of ways decoding "12" is 2.

trasition equation is:
if s[i-1] > 0:
    dp[i] += dp[i-1]
if 10<s[i-2:i] <= 26:
    dp[i] += dp[i-2]
'''
class Solution:
    # @param s, a string
    # @return an integer
    def numDecodings(self, s):
        l = len(s)
        if l == 0 or int(s[0])<=0:
            return 0
        dp = [0 for i in range(l+1)]
        dp[0], dp[1] = 1,1
        for i in range(2,l+1):
            if int(s[i-1])>0:
                dp[i] += dp[i-1]
            if int(s[i-2:i])<=26 and int(s[i-2:i]) >= 10:
                dp[i] += dp[i-2]
        return dp[-1]
x = Solution()
print x.numDecodings("0")







































