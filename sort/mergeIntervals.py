__author__ = 'effy'
'''
Given a collection of intervals, merge all overlapping intervals.

For example,
Given [1,3],[2,6],[8,10],[15,18],
return [1,6],[8,10],[15,18].
'''

# Definition for an interval.
class Interval:
     def __init__(self, s=0, e=0):
         self.start = s
         self.end = e

class Solution:
    # @param intervals, a list of Interval
    # @return a list of Interval
    def merge(self, intervals):
        new = sorted(intervals,key=lambda x:x.start)
        n = len(new)
        if n <= 1:
            return intervals
        merged= []
        cur = intervals[0]
        for i in range(1,n):
            next = new[i]
            if cur.end >= next.start:
                cur = Interval(cur.start, max(next.end, cur.end))
            else:
                '''
                only when cur can not be further merged, can it be appended into merged
                final list.
                '''
                merged.append(cur)
                cur = next
        merged.append(cur)
        return merged


class Solution2:
    # @param intervals, a list of Interval
    # @return a list of Interval
    def merge(self, intervals):
        new = sorted(intervals,key=lambda x:x.start)
        res = []
        cur = 0
        n = len(new)
        while cur<n:
            merge = new[cur]
            while cur<n-1 and merge.end >= new[cur+1].start:
                merge = Interval(merge.start, max(new[cur+1].end,merge.end))
                cur += 1
            res.append(merge)
            cur+=1
        return res

a = Interval(1,4)
b = Interval(0,2)
c = Interval(3,5)
d = Interval(15,18)
x=Solution()
t = x.merge([a,b,c])
for i in t:
    print i.start, i.end