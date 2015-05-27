__author__ = 'effy'
'''
Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

Note:
You may assume that nums1 has enough space (size that is greater or equal to m + n) to hold additional elements
from nums2. The number of elements initialized in nums1 and nums2 are m and n respectively.
'''

class Solution_secondround:
    # @param {integer[]} nums1
    # @param {integer} m
    # @param {integer[]} nums2
    # @param {integer} n
    # @return {void} Do not return anything, modify nums1 in-place instead.
    def merge(self, nums1, m, nums2, n):
        nums1 += [0 for i in range(n)]
        cur1, cur2 = m-1, n-1
        curnew = m+n-1
        while cur1 >=0 and cur2 >=0:
            if nums1[cur1] >= nums2[cur2]:
                nums1[curnew] = nums1[cur1]
                cur1 -= 1
            else:
                nums1[curnew] = nums2[cur2]
                cur2 -= 1
            curnew -= 1
        while cur2>=0:
            nums1[:curnew+1] = nums2[:cur2+1]
        return nums1


