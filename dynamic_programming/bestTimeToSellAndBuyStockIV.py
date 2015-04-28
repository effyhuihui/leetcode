__author__ = 'effy'
#-*- coding: utf-8 -*-
'''
Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete at most k transactions.

Note:
You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).

http://www.cnblogs.com/maples7/p/4350047.html

将会maintain两个2D dp。
local_dp[i][j]表示从0-i时间内，最多交易j次并且最后一次在i时间卖出的最佳收益。(j<=i)
global_dp[i][j]表示从0-i时间内，最多交易j次的全局最佳收益。(j<=i)

两个dp的状态转移方程分别为(diff 为prices[i] - prices[i-1])
local[i][j] = max(global[i-1][j-1] + max(diff,0), local[i-1][j]+diff)
上述方程比较两个量的大小：
①全局到i-1天进行j-1次交易，然后加上今天的交易（如果今天的交易赚钱的话）。
②取局部第i-1天进行j次交易，然后加上今天的差值（local[i-1][j]是第i-1天卖出的交易，它加上diff后变成第i天卖出，并不会增加交易次数。
无论diff是正还是负都要加上，否则就不满足local[i][j]必须在最后一天卖出的条件了）
global[i][j] = max(local[i][j], global[i-1][j])
上述方程比较两个量的大小：①当前局部最大值；②过往全局最大值
'''
class Solution:
    # @param {integer} k
    # @param {integer[]} prices
    # @return {integer}
    def maxProfit(self, k, prices):
        def noKLimit(prices):
            sum = 0
            for i in range(1,l):
                sum += max(0, prices[i]-prices[i-1])
            return sum
        l = len(prices)
        if l < 2:
            return 0
        if k >= l//2:
            return noKLimit(prices)
        local_dp = [[0 for i in range(l)] for j in range(l)]
        global_dp =[[0 for i in range(l)] for j in range(l)]
        for i in range(1,l):
            local_dp[i][1] = max(prices[i]-prices[0],0)
        for i in range(1,l):
            global_dp[i][1] = max(global_dp[i-1][1], local_dp[i][1])

        for i in range(1,l):
            for j in range(1,min(i+1,k*2)):
                diff = prices[i]-prices[i-1]
                local_dp[i][j] = max(global_dp[i-1][j-1]+max(0,diff), local_dp[i-1][j] + diff)
                global_dp[i][j] = max(local_dp[i][j], global_dp[i-1][j])
        return global_dp[-1][min(l-1,k)]















