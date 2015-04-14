__author__ = 'effy'
'''
Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (ie, buy one and sell one share of the stock),
design an algorithm to find the maximum profit.
'''
'''
maintain two variables, one is the current low, which means the lowest price so far
the other is max profit, which means the max profit so far.
maxProfit = max(maxProfit, current-current_lowest)
'''
class Solution:
    # @param prices, a list of integer
    # @return an integer
    def maxProfit(self, prices):
        if len(prices) == 0 :
            return 0
        current_lowest = prices[0]
        maxProfit = 0
        for i in range(1,len(prices)):
            current_lowest = min(current_lowest,prices[i])
            maxProfit = max(maxProfit, prices[i]-current_lowest)
        return maxProfit