__author__ = 'effy'
'''
Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary).

You may assume that the intervals were initially sorted according to their start value.

Example 1:
Given intervals [1,3],[6,9], insert and merge [2,5] in as [1,5],[6,9].

Example 2:
Given [1,2],[3,5],[6,7],[8,10],[12,16], insert and merge [4,9] in as [1,2],[3,10],[12,16].

This is because the new interval [4,9] overlaps with [3,5],[6,7],[8,10].
'''
class Interval:
     def __init__(self, s=0, e=0):
         self.start = s
         self.end = e

class Solution:
    # @param intervals, a list of Intervals
    # @param newInterval, a Interval
    # @return a list of Interval
    def insert(self, intervals, newInterval):
        intervals.append(newInterval)
        new = sorted(intervals, key=lambda x: x.start)
        res = []
        cur = 0
        n = len(new)
        while cur < n:
            merge = new[cur]
            while cur < n-1 and merge.end >=new[cur+1].start:
                merge = Interval(merge.start, max(merge.end, new[cur+1].end))
                cur += 1
            res.append(merge)
            cur += 1
        return res
'''

from left merge to right
'''
class Solution_secondround:
    # @param intervals, a list of Intervals
    # @param newInterval, a Interval
    # @return a list of Interval
    def insert(self, intervals, newInterval):
        intervals.append(newInterval)
        intervals.sort(key=lambda x:x.start)
        l = len(intervals)
        res = []
        cur = intervals[0]
        for i in range(1,l):
            if cur.end >= intervals[i].start:
                cur = Interval(min(cur.start,intervals[i].start), max(cur.end, intervals[i].end))
            else:
                res.append(cur)
                cur = intervals[i]
        res.append(cur)
        return res

'''

from right merge to left
'''
class Solution_secondround2:
    # @param intervals, a list of Intervals
    # @param newInterval, a Interval
    # @return a list of Interval
    def insert(self, intervals, newInterval):
        intervals.append(newInterval)
        intervals.sort(key=lambda x:x.start)
        l = len(intervals)
        res = []
        for i in range(l-1,-1,-1):
            cur = intervals[i]
            if res == []:
                res.append(cur)
            else:
                while res and cur.end >= res[-1].start:
                    last = res.pop()
                    cur = Interval(min(cur.start,last.start), max(cur.end, last.end))
                res.append(cur)
        return sorted(res, key=lambda x: x.start)

