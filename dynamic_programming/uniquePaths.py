__author__ = 'effy'
# -*- coding: utf-8 -*-
'''
A robot is located at the top-left corner of a m x n grid.

The robot can only move either down or right at any point in time.
The robot is trying to reach the bottom-right corner of the grid.

How many possible unique paths are there?
m and n will be at most 100.
'''
'''
how many possible --- dp的标志。。。所以重点是找到状态转移方程。
Let f(m,n) be the possible ways to get to (m,n)
f(m,n) = f(m-1,n) + f(m,n-1)
毫无优化的方法可以是maintain一个m*n的2d arrary， 优化过memory的方法
可以用recursion 只需要maintain两个当前concern的variable
'''
class Solution:
    # @return an integer
    def uniquePaths(self, m, n):
        ways = [[0]*n for i in range(m)]
        ## all grids in first row and first column only have one way to get there
        for i in range(n):
            ways[0][i] = 1
        for i in range(m):
            ways[i][0] = 1
        for i in range(1,n):
            for j in range(1,m):
                ways[j][i] = ways[j-1][i] + ways[j][i-1]
        return ways[-1][-1]

    def uniquePaths_opt(self,m,n):
        print m,n
        if m == 1 or n == 1:
            print "yes"
            return 1
        else:
            return self.uniquePaths_opt(m-1,n) + self.uniquePaths_opt(m,n-1)
x = Solution()
print x.uniquePaths_opt(23,12)
