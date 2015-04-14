__author__ = 'effy'
'''
You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps.
In how many distinct ways can you climb to the top?
'''
'''
Let f(n) be the number of ways of n stairs
transition function is f(n) = f(n-1) + f(n-2)   --- advance one or two steps to reach current state
'''

class Solution:
    # @param n, an integer
    # @return an integer
    ## this is without optimization, memory is not mininized
    def climbStairs(self, n):
        ## 0 stairs and 1 stairs is 1 respectively, as initial status
        dp = [1,1]
        for i in range(2,n+1):
            ways = dp[i-1] + dp[i-2]
            dp.append(ways)
        return dp[-1]
    ## no list
    def climbStairs_optimize(self, n):
        ## 0 stairs and 1 stairs is 1 respectively, as initial status
        one_prior, two_prior,current  = 1,1,1
        for i in range(2,n+1):
            current = one_prior + two_prior
            two_prior = one_prior
            one_prior = current
        return current
