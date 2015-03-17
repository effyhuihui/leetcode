__author__ = 'effy'
'''
Given a sorted array of integers, find the starting and ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].

For example,
Given [5, 7, 7, 8, 8, 10] and target value 8,
return [3, 4].
'''
class Solution:
    # @param A, a list of integers
    # @param target, an integer to be searched
    # @return a list of length 2, [index1, index2]
    def searchRange(self, A, target):
        n = len(A)
        start = 0
        end = n - 1
        while start <= end:
            mid = (start+end)/2
            if A[mid] == target:
                break
            elif A[mid] < target:
                start = mid + 1
            else:
                end = mid - 1
        if start > end:
            return [-1,-1]
        else:
            start = end = mid
            while start >= 0 and A[start] == target:
                start -= 1
            while end < n and A[end] == target:
                end += 1
            return [start+1, end-1]

a = Solution()
print a.searchRange([5, 7, 7, 8, 8, 10],8)