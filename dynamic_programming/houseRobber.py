__author__ = 'effy'
# -*- coding: utf-8 -*-
'''
You are a professional robber planning to rob houses along a street.
Each house has a certain amount of money stashed,
the only constraint stopping you from robbing each of them is that
adjacent houses have security system connected and it will automatically contact the police
if two adjacent houses were broken into on the same night.

Given a list of non-negative integers representing the amount of money of each house,
determine the maximum amount of money you can rob tonight without alerting the police.
'''

'''
max problem , DP, transition equation, Let dp(n) be the max money robbed if there are n houses
状态转移方程：

dp[i] = max(dp[i - 1], dp[i - 2] + money[i]) (i starts with 1) -- money[i] = num[i-1]

其中，dp[i]表示打劫到第i间房屋时累计取得的金钱最大值。

时间复杂度O(n)，空间复杂度O(n)
'''
class Solution:
    # @param num, a list of integer
    # @return an integer
    def rob(self, num):
        l = len(num)
        if l == 0:
            return 0
        total = [0]*(len(num)+1)
        ## total[0] is safe guard for num[1], since dp[2] = max(dp[1], dp[0]+num[1])
        ## take [2,1,1,2] for example ;)
        total[1] = num[0]
        for i in range(2,l+1):
            ## rob till i th house, the max profit is max(total[i-1], total[i-2] + current house money)
            ## remember num and total has 1 difference in index
            total[i] = max(total[i-1], total[i-2]+num[i-1])
        return total[-1]

'''
时间复杂度O(1)，空间复杂度O(n)
'''
class Solution_optimized:
    def rob(self, num):
        l = len(num)
        if l == 0 :
            return 0
        ## assign current to protect if num only has one house
        one_before, current = num[0], num[0]
        two_before = 0
        for i in range(1,l):
            current = max(two_before+num[i], one_before)
            two_before = one_before
            one_before = current
        return current


x = Solution_optimized()
print x.rob([1,1])