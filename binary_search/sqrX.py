__author__ = 'effy'

'''
Implement int sqrt(int x).

Compute and return the square root of x.

Tag : Binary Search
'''

class Solution:
    # @param x, an integer
    # @return an integer
    def sqrt(self, x):
        if x == 1:
            return 1
        start = 1
        end = x/2
        mid = (start+end)/2
        while start < end:
            if mid*mid <= x and (mid+1)*(mid+1) > x:
                return mid
            elif mid*mid < x and (mid+1)*(mid+1) <= x:
                start = mid + 1
            elif mid*mid > x:
                end = mid - 1
            mid = (start + end)/2
        return mid

a = Solution()
print a.sqrt(12)

