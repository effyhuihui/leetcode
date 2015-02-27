'''
Given an unsorted integer array, find the first missing positive integer.

For example,
Given [1,2,0] return 3,
and [3,4,-1,1] return 2.

Your algorithm should run in O(n) time and uses constant space.
'''

class Solution:
    # @param A a list of integers
    # @return nothing, sort in place
    def firstMissingPositive(self, A):
        n = len(A)
        if n == 0:
            return 1
        for i in range(n):
            '''
            swap element within for loop : should be very careful about when i can be 
            advanced for 1!!! sometimes need a while loop to control
            '''
            num = A[i]
            while A[i] <= n and A[i] >= 1 and A[i] != i+1:
                '''
                In an array of length n, the most filled case for positive integers
                starts from 1 to n, need to put valid positive integers ([1,n]) to
                their belonged places.
                '''
                A[i] = A[num-1]
                A[num-1] = num
                num = A[i]
        ## after putting positive integers to where they belong, go through the whole
        ## array and find the first one that is not valid
        for i in range(n):
            if A[i] != i+1:
                return i+1
        return n+1