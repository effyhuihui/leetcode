__author__ = 'effy'
'''
Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Your goal is to reach the last index in the minimum number of jumps.

For example:
Given array A = [2,3,1,1,4]

The minimum number of jumps to reach the last index is 2. (Jump 1 step from index 0 to 1,
then 3 steps to the last index.)
'''

class Solution_dp:
    # @param A, a list of integers
    # @return an integer
    def jump(self, A):
         maxint = 1000000
         dp = [ maxint for i in range(len(A)) ]
         dp[0] = 0
         for i in range(1, len(A)):
             for j in range(i):
                 if A[j] >= (i - j):
                     dp[i] = min(dp[i], dp[j] + 1)
         return dp[len(A) - 1]
    # dp is time limited exceeded!


class Solution_greedy:
# We use "last" to keep track of the maximum distance that has been reached
# by using the minimum steps "ret", whereas "curr" is the maximum distance
# that can be reached by using "ret+1" steps. Thus,curr = max(curr, i+A[i]) where 0 <= i <= last.
    def jump(self, A):
        ret = 0
        last = 0
        curr = 0
        for i in range(len(A)):
            if i > last:
                last = curr
                ret += 1
            curr = max(curr, i+A[i])
        return ret