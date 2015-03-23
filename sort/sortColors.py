__author__ = 'effy'
'''
Given an array with n objects colored red, white or blue, sort them so that objects of the same color are
adjacent, with the colors in the order red, white and blue.

Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.

Note:
You are not suppose to use the library's sort function for this problem.
'''
class Solution:
    # @param A a list of integers
    # @return nothing, sort in place
    def sortColors(self, A):
        N, i = len(A), 0
        nextRed = 0
        nextBlue = N-1
        while i <= nextBlue:
            if A[i] == 0:
                ## swap 0 and anything else
                A[i] = A[nextRed]
                A[nextRed] = 0
                nextRed += 1
                i += 1
            elif A[i] == 1:
                i += 1
            else:
                A[i] = A[nextBlue]
                A[nextBlue] = 2
                nextBlue -=1
        return A