__author__ = 'effy'
'''
ollow up for "Unique Paths":

Now consider if some obstacles are added to the grids. How many unique paths would there be?

An obstacle and empty space is marked as 1 and 0 respectively in the grid.

For example,
There is one obstacle in the middle of a 3x3 grid as illustrated below.

[
  [0,0,0],
  [0,1,0],
  [0,0,0]
]
The total number of unique paths is 2.

'''
'''
same as unique path 1, something worth noticing:
1. to initialize border(row 1 and col 1), if there is obstacle, then the rest ways are 0
2. during iterating through the grid, if current value is 1, then ways[i][j] = 0
'''
class Solution:
    # @param obstacleGrid, a list of lists of integers
    # @return an integer
    def uniquePathsWithObstacles(self, obstacleGrid):
        m,n = len(obstacleGrid),len(obstacleGrid[0])
        ways = [[0]*n for i in range(m)]
        for i in range(n):
            if obstacleGrid[0][i] == 1:
                break
            else:
                ways[0][i] = 1
        for i in range(m):
            if obstacleGrid[i][0] == 1:
                break
            else:
                ways[i][0] = 1
        for i in range(1,m):
            for j in range(1,n):
                if obstacleGrid[i][j] == 0:
                    ways[i][j] = ways[i-1][j]+ways[i][j-1]
                else:
                    ways[i][j] = 0
        return ways[-1][-1]


class Solution_secondround:
    # @param obstacleGrid, a list of lists of integers
    # @return an integer
    def uniquePathsWithObstacles(self, obstacleGrid):
        m,n=len(obstacleGrid), len(obstacleGrid[0])
        dp = [ [0 for i in range(n)] for j in range(m)]
        if obstacleGrid[0][0] == 1:
            return 0
        else:
            dp[0][0] = 1
        for i in range(1,n):
            if obstacleGrid[0][i] != 1:
                dp[0][i] = dp[0][i-1]
            else:
                dp[0][i] = 0
        for i in range(1,m):
            if obstacleGrid[i][0] != 1:
                dp[i][0] = dp[i-1][0]
            else:
                dp[i][0] = 0
        for i in range(1,m):
            for j in range(1,n):
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0
                else:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[-1][-1]
