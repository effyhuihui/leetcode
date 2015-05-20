# -*- coding: utf-8 -*-
'''
A peak element is an element that is greater than its neighbors.

Given an input array where num[i] ≠ num[i+1], find a peak element and return its index.

The array may contain multiple peaks, in that case return the index to any one of the peaks is fine.

You may imagine that num[-1] = num[n] = -∞.

For example, in array [1, 2, 3, 1], 3 is a peak element and your function should return the index number 2.
'''

class Solution:
    # @param num, a list of integer
    # @return an integer
    '''
    Of course it could be done in O(N) with a linear scan, but it could be faster
    This is an implementation of binary search

    Binary search approach is crucial to keep the following variables:
    1. start, mid ,end to indicate which half is of current concern
    2. comparison conditions to determine whether to move to left half or right half
    Keep in mind that it is very import to avoid the while loop to be infinite
    When assigning start = mid or end = mid mid = (start+end)/2, it might not change
    if start = mid or end = mid already! remember to add/minus 1 when reassign start
    end to new index
    '''
    def findPeakElement(self, num):
        n = len(num)
        if n == 1:
            return 0
        start = 0
        end = n-1
        while start <= end:
            mid = (end+start)/2
            left_index = max(0,mid -1)
            right_index = min(mid+1,n-1)
            left = num[mid] - num[left_index]
            right = num[mid] - num[right_index]
            if left > 0 and right > 0:
                break
            elif left >= 0 and right <= 0:
                start = mid + 1
            else:
                end = mid - 1
        return mid



class Solution_secondround:
    # @param num, a list of integer
    # @return an integer
    def findPeakElement(self, num):
        l = len(num)
        start, end = 0, l-1
        while start<= end:
            mid = (start+end)/2
            left,right = max(0,mid-1), min(l-1, mid+1)
            ## garautee a peak which is not a left most or right most element
            if num[left]<num[mid]   and num[right]< num[mid]:
                return mid
            ## increasing order from left
            if num[mid]>=num[left] and num[mid]<=num[right]:
                start = mid+1
            else:
                end = mid-1
        return mid


a = Solution()
print a.findPeakElement([5,4,3,2])