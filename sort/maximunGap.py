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
