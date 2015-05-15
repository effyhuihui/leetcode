__author__ = 'effy'

'''
Implement int sqrt(int x).

Compute and return the square root of x.

Tag : Binary Search
'''

class Solution:
    # @param x, an integer
    # @return an integer
    def mySqrt(self, x):
        if x == 0:
            return 0
        if x == 1:
            return 1
        start = 1
        end = x/2
        while start <= end:
            mid = (start + end)/2
            if mid*mid <= x and (mid+1)*(mid+1) > x:
                return mid
            elif mid*mid < x:
                start = mid + 1
            elif mid*mid > x:
                end = mid - 1
        return mid



class Solution_secondTime:
    # @param x, an integer
    # @return an integer
    def mySqrt(self, x):
        start, end = 0, x
        while start<=end:
            mid = (start+end)//2
            if mid*mid<=x and (mid+1)*(mid+1) > x:
                return mid
            elif mid*mid < x:
                start = mid+1
            else:
                end = mid -1
        return mid
a = Solution()
print a.sqrt(0)

