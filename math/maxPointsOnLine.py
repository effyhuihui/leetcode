__author__ = 'effy'
# -*- coding:utf-8 -*-
'''
Given n points on a 2D plane, find the maximum number of points that lie on the same straight line.

找到平面上在一条直线上最多的点。点在同一条直线上意味着这些点的斜率和截距是一样的。
那么用两重for loop，每次固定一个点进行遍历，这样的话只要斜率一样，必定在通一条直线上~
这里有几个需要考虑的要点：1，有可能是斜率无穷大。2，有可能有相同的点，比如[(1,2),(1,2)]。
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



class Solution_secondround:
    # @param points, a list of Points
    # @return an integer
    def maxPoints(self, points):
        res = -1
        l = len(points)
        if l <3:
            return l
        for i in range(l):
            ## create a line map given one node
            line_map = {'inf':0}
            same_point = 1
            for j in range(i+1,l):
                x1,y1 = points[i].x, points[i].y
                x2,y2 = points[j].x, points[j].y
                if x1 == x2 and y1 == y2:
                    same_point +=1
                elif x1 == x2:
                    line_map['inf'] += 1
                else:
                    slope = 1.0*(y1-y2)/(x1-x2)
                    line_map[slope] = line_map.get(slope,0)+1
            res = max(res, max(line_map.values())+same_point)
        return res