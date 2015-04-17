__author__ = 'effy'
# -*- coding: utf-8 -*-
'''
Given a string S and a string T, count the number of distinct subsequences of T in S.

A subsequence of a string is a new string which is formed from the original string by deleting some
(can be none) of the characters without disturbing the relative positions of the remaining characters.
(ie, "ACE" is a subsequence of "ABCDE" while "AEC" is not).

Here is an example:
S = "rabbbit", T = "rabbit"

Return 3.
'''
'''
 这道题首先引用我忘记在哪里看到的一句话：

 "When you see string problem that is about subsequence or matching,
 dynamic programming method should come to your mind naturally. "

 所以这种类型题可以多往DP思考思考。

 首先设置动态规划数组dp[i][j]，表示S串中从开始位置到第i位置与T串从开始位置到底j位置匹配的子序列的个数。

 如果S串为空，那么dp[0][j]都是0；

 如果T串为空，那么dp[i][j]都是1，因为空串为是任何字符串的字串。

 可以发现规律，dp[i][j] 至少等于 dp[i][j-1]。
 所以递推公式是怎样的呢，既然知道了他是2D的，所以就强行的找找dp[i][j]和dp[i-1][j] dp[i-1][j-1], dp[i][j-1]这种的关系

 dp[i-1][j] --> dp[i][j]
    当固定T不变S增加一位时，假设这时候S多增加的一位和之前以及现有的T的最后一位不同，那么表示增加的这一个char不能增加unique
    子串。也就是等于dp[i-1][j]
    然后假设多增加的一位和T的最后一位相同，那么这是子串的选择来了 a. 可以删除新增的char，只用前面的S字符串，那么就
    是 dp[i-1][j]. b. 可以不删除新增的char， 那么T的最后一位已经由S新增的最后一位保证了，那么只需要关心S和T的前i-1, j-1
    位就可以了 也就是 dp[i-1][j-1]

 所以递推公式是如果S的第i位等于T的第j位, dp[i][j] = dp[i-1][j-1] + dp[i-1][j], 如果不等, dp[i][j] = dp[i-1][j]
 注意，建立一个初始的m*n 2D array，另，注意设置边界条件。


 当i=2，j=1时，S 为 ra，T为r，T肯定是S的子串；这时i=2，j=2时，S为ra，T为rs，T现在不是S的子串，当之前一次是子串所以现在计数为1.


同时，如果字符串S[i-1]和T[j-1]（dp是从1开始计数，字符串是从0开始计数）匹配的话，dp[i][j]还要加上dp[i-1][j-1]

 例如对于例子： S = "rabbbit", T = "rabbit"

 当i=2，j=1时，S 为 ra，T为r，T肯定是S的子串；当i=2，j=2时，S仍为ra，T为ra，这时T也是S的子串，所以子串数在dp[2][1]基础上加dp[1][1]。
'''
class Solution:
    # @param S, a string
    # @param T, a string
    # @return an integer
    def numDistinct(self, S, T):
        lenT,lenS=len(T), len(S)
        if lenT == 0:
            return lenS+1
        dp = [[0 for i in range(lenT+1)] for j in range(lenS+1)]
        ##当T长度为0时，T是任意S前x位的子串，且为1
        for i in range(lenS+1):
            dp[i][0]=1
        for i in range(1,lenS+1):
            ## T will always be shorter than S
            for j in range(1,min(i+1,lenT+1)):
                ## if the last character of current S and T are then same
                if S[i-1] == T[j-1]:
                    dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
                ## if the last character is not the same
                else:
                    dp[i][j] = dp[i-1][j]
        return dp[-1][-1]
x = Solution()
print x.numDistinct("rabbbit", "rabbit")
