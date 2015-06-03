# -*- coding: utf-8 -*-
__author__ = 'effy'
'''
Given an unsorted array, find the maximum difference between the successive elements in its sorted form.

Try to solve it in linear time/space.

Return 0 if the array contains less than 2 elements.

You may assume all elements in the array are non-negative integers and fit in the 32-bit signed integer range.


Thought :
http://bookshadow.com/weblog/2014/12/14/leetcode-maximum-gap/
Bucket sort
解题思路：
基数排序（radix sort）/桶排序（bucket sort）

官方版（桶排序）：
假设有N个元素A到B。

那么最大差值不会小于ceiling[(B - A) / (N - 1)] ---> （这是每两个元素间隔都是一样的时候）

令bucket（桶）的大小len = ceiling[(B - A) / (N - 1)]，则最多会有(B - A) / len + 1个桶

对于数组中的任意整数K，很容易通过算式loc = (K - A) / len找出其桶的位置，然后维护每一个桶的最大值和最小值

由于同一个桶内的元素之间的差值至多为len - 1，因此最终答案不会从同一个桶中选择。

对于每一个非空的桶p，找出下一个非空的桶q，则q.min - p.max可能就是备选答案。返回所有这些可能值中的最大值。
'''
'''
below is O(nlogn)
'''
class Solution:
    # @param num, a list of integer
    # @return an integer
    def maximumGap(self, num):
        n = len(num)
        if n < 2:
            return 0
        num.sort()
        diff = 0
        for i in range(1,n):
            diff = max((num[i] - num[i-1]),diff)
        return diff

class Solution_bucket_sort:
     # @param numss: a list of integers
     # @return: the maximum difference
    def maximumGap(self, nums):
        if len(nums) < 2:
            return 0

        # Init bucket.
        max_val, min_val = max(nums), min(nums)
        gap = max(1, (max_val - min_val) / (len(nums) - 1))
        bucket_size = (max_val - min_val) / gap + 1
        bucket = [{'min':float("inf"), 'max':float("-inf")} \
                    for _ in xrange(bucket_size)]

        # Find the bucket where the n should be put.
        for n in nums:
            # min_val / max_val is in the first / last bucket.
            if n in (max_val, min_val):
                continue
            i = (n - min_val) / gap
            bucket[i]['min'] = min(bucket[i]['min'], n)
            bucket[i]['max'] = max(bucket[i]['max'], n)

        # Count each bucket gap between the first and the last bucket.
        # if all numbers are evenly distributed, then the minimum max gap occurs
        # which is the 'gap' variable
        max_gap, pre_bucket_max = 0, min_val
        for i in xrange(bucket_size):
            # Skip the bucket it empty.
            if bucket[i]['min'] == float("inf") and \
                bucket[i]['max'] == float("-inf"):
                continue
            max_gap = max(max_gap, bucket[i]['min'] - pre_bucket_max)
            pre_bucket_max = bucket[i]['max']
        # Count the last bucket.
        max_gap = max(max_gap, max_val - pre_bucket_max)

        return max_gap