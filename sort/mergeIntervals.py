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


'''
it matters to merge from left to right or right to left
after merge, it newly merged interval can not be inserted immediately, only insert
when there is no further merge needed.
'''

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


class Solution_secondround:
    # @param intervals, a list of Interval
    # @return a list of Interval
    def merge(self, intervals):
        intervals.sort(key=lambda x: x.start)
        stack = []
        l = len(intervals)
        for i in range(l-1,-1,-1):
            cur_interval = intervals[i]
            if not stack:
                stack.append(cur_interval)
            else:
                ## merge conditions as follows
                ## also, one merge might affect previous intervals.
                ## e.g.[(1,10),(2,3),(4,5),(6,7),(8,9)]
                while stack and cur_interval.end>=stack[-1].start:
                    last = stack.pop()
                    cur_interval = Interval(min(cur_interval.start,last.start),max(cur_interval.end, last.end))
                stack.append(cur_interval)
        return stack



a = Interval(1,4)
b = Interval(0,2)
c = Interval(3,5)
d = Interval(15,18)
x=Solution()
t = x.merge([a,b,c])
for i in t:
    print i.start, i.end