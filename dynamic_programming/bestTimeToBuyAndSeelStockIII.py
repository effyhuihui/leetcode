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
        length=len(prices)
        if length==0: return 0
        f1=[0 for i in range(length)]
        f2=[0 for i in range(length)]

        minV=prices[0]; f1[0]=0
        for i in range(1,length):
            minV=min(minV, prices[i])
            f1[i]=max(f1[i-1],prices[i]-minV)

        maxV=prices[length-1]; f2[length-1]=0
        for i in range(length-2,-1,-1):
            maxV=max(maxV,prices[i])
            f2[i]=max(f2[i+1],maxV-prices[i])

        res=0
        for i in range(length):
            if f1[i]+f2[i]>res: res=f1[i]+f2[i]
        return res

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


