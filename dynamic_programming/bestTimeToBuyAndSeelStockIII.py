__author__ = 'effy'
# -*- coding: utf-8 -*-
'''
Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete at most two transactions.

Note:
You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).
解法很巧妙，有点动态规划的意思：开辟两个数组f1和f2，f1[i]表示在price[i]之前进行一次交易所获得的最大利润，f2[i]表示在price[i]之后
进行一次交易所获得的最大利润。则f1[i]+f2[i]的最大值就是所要求的最大值，而f1[i]和f2[i]的计算就需要动态规划了，看代码不难理解。
'''

class Solution:
    # @param prices, a list of integer
    # @return an integer
    def maxProfit(self, prices):
        l = len(prices)
        if l == 0:
             return 0
        pre_profit = [0 for i in range(l)]
        post_profit = [0 for i in range(l)]

        current_low = prices[0]
        pre_profit[0] = 0
        for i in range(1,l):
            current_low = min(current_low,prices[i])
            pre_profit[i] = max(pre_profit[0],prices[i]-current_low)

        current_high = prices[-1]
        post_profit[-1] = 0
        for i in range(l-2,-1,-1):
            current_high = max(current_high, prices[i])
            post_profit[i] = max(post_profit[i+1], current_high-prices[i])

        total_profit = [ pre_profit[i]+post_profit[i] for i in range(l)]
        return max(total_profit)


class Solution_secondround:
    # @param prices, a list of integer
    # @return an integer
    def maxProfit(self, prices):
        l = len(prices)
        if l == 0:
            return 0
        pre_profit = [0 for i in range(l)]
        post_profit = [0 for i in range(l)]
        min_price=prices[0]
        for i in range(1,l):
            min_price = min(prices[i], min_price)
            pre_profit[i] = max(pre_profit[i-1], prices[i]-min_price)
        max_price = prices[-1]
        for i in range(l-2,-1,-1):
            max_price = max(max_price, prices[i])
            post_profit[i] = max(post_profit[i+1], max_price-prices[i])
        max_profit = 0
        for i in range(l):
            max_profit = max(pre_profit[i] + post_profit[i], max_profit)
        return max_profit




class Solution_3rd:
    # @param prices, a list of integer
    # @return an integer
    def maxProfit(self, prices):
        if not prices:
            return 0
        pre_max, post_max = [0 for i in range(len(prices))], [0 for i in range(len(prices))]
        current_min, max_profit = prices[0], 0
        for i in range(1,len(prices)):
            current_min = min(current_min, prices[i])
            pre_max[i] =max(pre_max[i-1], prices[i]-current_min)
        current_max, max_profit = prices[-1], 0
        for i in range(len(prices)-2,-1,-1):
            current_max = max(prices[i], current_max)
            post_max[i] = max(post_max[i+1], current_max-prices[i])
        global_max = 0
        for i in range(len(pre_max)):
            global_max = max(global_max, pre_max[i]+post_max[i])
        return global_max