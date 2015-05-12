__author__ = 'effy'
# -*- coding:utf-8 -*-
'''
Given n points on a 2D plane, find the maximum number of points that lie on the same straight line.
不考虑截距....
找到平面上在一条直线上最多的点。点在同一条直线上意味着这些点的斜率是一样的，那么可以考虑使用哈希表来解决，
{斜率：[点1，点2]}这样的映射关系。这里有几个需要考虑的要点：1，有可能是斜率无穷大。2，有可能有相同的点，比如[(1,2),(1,2)]。
'''
class Point:
     def __init__(self, a=0, b=0):
         self.x = a
         self.y = b

class Solution:
    # @param points, a list of Points
    # @return an integer
    def maxPoints(self, points):
        length = len(points)
        if length < 3: return length
        res = -1
        for i in range(length):
            slope = {'inf': 0}
            samePointsNum = 1
            for j in range(i+1, length):
                if points[i].x == points[j].x and points[i].y != points[j].y:
                    slope['inf'] += 1
                elif points[i].x != points[j].x:
                    k = 1.0 * (points[i].y - points[j].y) / (points[i].x - points[j].x)
                    slope[k] = slope.get(k,0)+1
                else:
                    samePointsNum += 1
            res = max(res, max(slope.values()) + samePointsNum)
        return res