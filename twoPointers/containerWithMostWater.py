# -*- coding: utf-8 -*-
__author__ = 'effy'
'''
Given n non-negative integers a1, a2, ..., an, where each represents a point at coordinate (i, ai).
n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0).
Find two lines, which together with x-axis forms a container, such that the container contains
the most water.

Note: You may not slant the container.

Greedy algorithm
木桶原理大家肯定都知道，水盛多少取决于最短的杯壁，所以此题还可以引申为往围成的区域内放矩形，怎样使得矩形面积最大。

复杂度为O（n）的思想是贪心原理，先从底边最大的情况考虑，计算最大面积后，此时要将底边长度减1，只需要将杯壁较短的那一边
移动一个单位距离，得到的解必定优于杯壁较长那边移动的情况。这样保证每次移动都得到的是局部最优解。

greedy算法不一定能解决所有问题，比如largest histogram若用贪心算法结果就是错的。
'''
class Solution:
    # @return an integer
    def maxArea(self, height):
        left, right = 0, len(height)-1
        max_area = 0
        while left < right:
            area = (right-left)*min(height[left], height[right])
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
            max_area = max(area, max_area)
        return max_area


class Solution_secondround:
    # @return an integer
    def maxArea(self, height):
        start, end =0,len(height)-1
        max_area = 0
        while start<end:
            local_max = (end-start)*min(height[start], height[end])
            max_area = max(local_max, max_area)
            if height[start]<height[end]:
                start += 1
            else:
                end -= 1
        return max_area
