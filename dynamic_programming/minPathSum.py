__author__ = 'effy'
'''
Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum
of all numbers along its path.

Note: You can only move either down or right at any point in time.
'''

'''
min, max problem, think about DP
min_path_sum(i,j)=min(min_path_sum(i-1,j), min_path_sum(i,j-1)) + grid(i,j)
'''
class Solution:
    # @param grid, a list of lists of integers
    # @return an integer
    def minPathSum(self, grid):
        m,n = len(grid), len(grid[0])
        min_sum = [[0]*n for i in range(m)]
        min_sum[0][0] = grid[0][0]
        for i in range(1,m):
            min_sum[i][0]=grid[i][0]+min_sum[i-1][0]
        for i in range(1,n):
            min_sum[0][i] = grid[0][i] + min_sum[0][i-1]
        #print min_sum
        for i in range(1,m):
            for j in range(1,n):
                min_sum[i][j] = min(min_sum[i-1][j], min_sum[i][j-1])+grid[i][j]
        return min_sum[-1][-1]


class Solution_secondround:
    # @param grid, a list of lists of integers
    # @return an integer
    def minPathSum(self, grid):
        m,n = len(grid),len(grid[0])
        min_sum = [ [0 for i in range(n)] for j in range(m)]
        min_sum[0][0] = grid[0][0]
        for i in range(1,m):
            min_sum[i][0] = min_sum[i-1][0]+grid[i][0]
        for i in range(1,n):
            min_sum[0][i] = min_sum[0][i-1] + grid[0][i]
        for i in range(1,m):
            for j in range(1,n):
                min_sum[i][j] = min(min_sum[i-1][j], min_sum[i][j-1])+grid[i][j]
        return min_sum[-1][-1]


x = Solution()
a = [[1,3,5],[2,4,6],[1,2,3],[0,0,1]]
print x.minPathSum(a)


